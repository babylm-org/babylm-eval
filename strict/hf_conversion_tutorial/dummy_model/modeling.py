from __future__ import annotations

import torch
from torch import nn
from transformers.activations import gelu_new
import math
from torch import _softmax_backward_data as _softmax_backward_data
import torch.nn.functional as F
from .model_configuration import ModelConfig

from transformers.modeling_utils import PreTrainedModel
from transformers.modeling_outputs import (
    BaseModelOutput,
    CausalLMOutput
)

from typing import Optional, Union

# YOUR MODEL CLASSES GOES HERE


class MaskedSoftmax(torch.autograd.Function):
    @staticmethod
    def forward(self, x: torch.Tensor, mask: torch.BoolTensor, dim: int):
        self.dim = dim
        x.masked_fill_(mask, float('-inf'))
        x = torch.softmax(x, self.dim)
        x.masked_fill_(mask, 0.0)
        self.save_for_backward(x)
        return x

    @staticmethod
    def backward(self, grad_output: torch.Tensor):
        output, = self.saved_tensors
        inputGrad = _softmax_backward_data(grad_output, output, self.dim, output.dtype)
        return inputGrad, None, None


class GeGLU(nn.Module):
    def forward(self, x):
        x, gate = x.chunk(2, dim=-1)
        x = x * gelu_new(gate)
        return x


class RotaryPositionalEmbeddings(nn.Module):

    def __init__(self, config: ModelConfig):

        super().__init__()
        head_size = config.hidden_size // config.num_attention_heads
        assert head_size % 2 == 0
        max_seq_len = config.max_sequence_length

        thetas = torch.tensor([1/(config.rope_theta**((2*i)/head_size)) for i in range(head_size // 2)])
        pos = torch.arange(max_seq_len)
        m_theta = torch.einsum('n, d -> nd', pos, thetas)
        m_theta = torch.stack([m_theta, m_theta], dim=-1).reshape(max_seq_len, head_size)[None, None, :, :]
        self.cos_matrix = m_theta.cos()
        self.sin_matrix = m_theta.sin()

    def forward(self, x: torch.Tensor) -> torch.Tensor:

        seq_len = x.shape[-2]

        cos_matrix = self.cos_matrix[:, :, :seq_len, :]
        sin_matrix = self.sin_matrix[:, :, :seq_len, :]

        x_rotate_half = torch.stack([-x[..., x.size(-1) // 2:], x[..., :x.size(-1) // 2]], dim=-1).reshape_as(x)

        out = x * cos_matrix + x_rotate_half * sin_matrix

        return out


class SelfAttention(nn.Module):

    def __init__(self, config: ModelConfig):
        """
        """
        super().__init__()

        if config.hidden_size % config.num_attention_heads != 0:
            raise ValueError(f"The QK size {config.qk_size} is not a multiple of the number of attention heads {config.num_attention_heads}")

        self.hidden_size = config.hidden_size
        self.num_heads = config.num_attention_heads
        self.head_size = self.hidden_size // self.num_heads

        self.in_proj_qkv = nn.Linear(self.hidden_size, 3*self.hidden_size, bias=config.attention_bias)
        self.out_proj = nn.Linear(self.hidden_size, self.hidden_size, bias=config.attention_bias)

        self.pre_norm = nn.LayerNorm(self.hidden_size, eps=config.layernorm_eps, elementwise_affine=config.attention_layernorm_learned)

        self.positional_embeddings = RotaryPositionalEmbeddings(config)

        self.attention_probs_dropout = nn.Dropout(config.attention_probabilities_dropout_p)
        self.attention_dropout = nn.Dropout(config.attention_dropout_p)

        self.scale = 1.0 / math.sqrt(self.head_size)
        self.initialize(config.attention_bias)

    def initialize(self, attention_bias: bool):
        """
        """
        std = math.sqrt(2.0 / (5.0 * self.hidden_size))
        nn.init.trunc_normal_(self.in_proj_qkv.weight, mean=0.0, std=std, a=-2*std, b=2*std)
        nn.init.trunc_normal_(self.out_proj.weight, mean=0.0, std=std, a=-2*std, b=2*std)
        if attention_bias:
            self.in_proj_qkv.bias.data.zero_()
            self.out_proj.bias.data.zero_()

    def attention_operation(self: SelfAttention, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """
        """
        attention_probs: torch.Tensor = torch.matmul(query, key.transpose(2, 3) * self.scale)
        attention_probs = MaskedSoftmax.apply(attention_probs, attention_mask, -1)
        attention_output: torch.Tensor = torch.matmul(attention_probs, value)

        return attention_output.transpose(1, 2), attention_probs

    def forward(self, hidden_states: torch.Tensor,  attention_mask: torch.Tensor) -> torch.Tensor:
        """
        """
        batch_size, query_len, hidden_size = hidden_states.size()
        key_len = query_len

        if attention_mask is None:
            attention_mask = torch.ones(query_len, key_len, dtype=torch.bool, device=hidden_states.device).triu(diagonal=1).unsqueeze(0).unsqueeze(0)

        hidden_states = self.pre_norm(hidden_states)
        query, key, value = self.in_proj_qkv(hidden_states).chunk(3, dim=-1)  # shape: [B, S, D]

        query = query.reshape(batch_size, query_len, self.num_heads, self.head_size).transpose(1, 2)
        key = key.reshape(batch_size, key_len, self.num_heads, self.head_size).transpose(1, 2)
        value = value.reshape(batch_size, key_len, self.num_heads, self.head_size).transpose(1, 2)

        query = self.positional_embeddings(query)
        key = self.positional_embeddings(key)

        attention_output, attention_probs = self.attention_operation(query, key, value, attention_mask)

        attention_output = attention_output.reshape(batch_size, key_len, self.num_heads * self.head_size)

        attention_output = self.out_proj(attention_output)
        attention_output = self.attention_out_dropout(attention_output)

        return attention_output, attention_probs


class FeedForward(nn.Module):

    def __init__(self, config: ModelConfig):
        """
        """
        super().__init__()
        intermediate_size = config.intermediate_size
        hidden_size = config.hidden_size

        # FFN layer
        self.mlp = nn.Sequential(
            nn.LayerNorm(hidden_size, eps=config.layernorm_eps, elementwise_affine=config.mlp_layernorm_learned),
            nn.Linear(hidden_size, 2*intermediate_size, bias=config.mlp_bias),
            GeGLU(),
            nn.Linear(intermediate_size, hidden_size, bias=config.mlp_bias),
            nn.Dropout(config.mlp_dropout_p)
        )

        self.initialize(hidden_size, config.mlp_bias)

    def initialize(self, hidden_size: int, bias: bool):
        """
        """
        std = math.sqrt(2.0 / (5.0 * hidden_size))
        nn.init.trunc_normal_(self.mlp[1].weight, mean=0.0, std=std, a=-2*std, b=2*std)
        nn.init.trunc_normal_(self.mlp[-2].weight, mean=0.0, std=std, a=-2*std, b=2*std)
        if bias:
            self.mlp[1].bias.data.zero_()
            self.mlp[-2].bias.data.zero_()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        """
        return self.mlp(x)


class CausalHead(nn.Module):

    def __init__(self, config: ModelConfig, word_embedding: nn.Parameter):
        """
        """
        super().__init__()

        hidden_size = config.hidden_size

        self.lm_head = nn.Sequential(
            nn.LayerNorm(hidden_size, eps=config.layernorm_eps, elementwise_affine=config.lm_head_layernorm_learned),
            nn.Linear(hidden_size, word_embedding.size(0))  # word_embedding.size(0) == vocab_size
        )

        self.initialize(hidden_size, word_embedding)

    def initialize(self, hidden_size: int, word_embedding: nn.Parameter):
        """
        """
        self.lm_head[-1].weight = word_embedding
        self.lm_head[-1].bias.data.zero_()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        """
        return self.lm_head(x)


class Embedding(nn.Module):

    def __init__(self, config: ModelConfig):
        """
        """
        super().__init__()

        self.word_embedding = nn.Embedding(config.vocab_size, config.hidden_size)
        self.word_norm = nn.LayerNorm(config.hidden_size, eps=config.layernorm_eps, elementwise_affine=config.embedding_layernorm_learned)

        self.dropout = nn.Dropout(config.embedding_dropout_prob)

        self.initialize(config.hidden_size)

    def initialize(self, hidden_size: int):
        """
        """
        std = math.sqrt(2.0 / (5.0 * hidden_size))
        nn.init.trunc_normal_(self.word_embedding.weight, mean=0.0, std=std, a=-2*std, b=2*std)

    def forward(self, input_tokens: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """
        """
        word_embeddings = self.dropout(self.word_norm(self.word_embedding(input_tokens)))

        return word_embeddings


class Layer(nn.Module):

    def __init__(self: Layer, config: ModelConfig):
        """
        """
        super().__init__()
        self.self_attention = SelfAttention(config)
        self.mlp = FeedForward(config)

    def forward(self: Layer, x: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
        """
        """
        attention, attention_probs = self.self_attention(x, attention_mask)
        x = x + attention
        x = x + self.mlp(x)

        return x, attention_probs


# END OF YOUR MODEL CLASSES
# START OF HUGGINGFACE WRAPPERS


class MyModelPreTrainedModel(PreTrainedModel):
    config_class = ModelConfig
    supports_gradient_checkpointing = False
    base_model_prefix = "model"

    def _set_gradient_checkpointing(self, module, value=False):
        raise NotImplementedError("Gradient checkpointing is not supported by this model")

    def _init_weights(self, module):
        std = math.sqrt(2.0 / (5.0 * self.hidden_size))

        if isinstance(module, nn.Linear):
            nn.init.trunc_normal_(module.weight.data, mean=0.0, std=std, a=-2*std, b=2*std)
            if module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.Embedding):
            nn.init.trunc_normal_(module.weight.data, mean=0.0, std=std, a=-2*std, b=2*std)
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)


class MyModel(MyModelPreTrainedModel):

    def __init__(self, config: ModelConfig, **kwargs):
        super().__init__(config, **kwargs)
        self.config = config
        self.hidden_size = config.hidden_size

        self.embedding = Embedding(config)
        self.layers = nn.ModuleList([Layer(config) for _ in range(config.num_layers)])

    def get_input_embeddings(self):
        return self.embedding.word_embedding

    def set_input_embeddings(self, value):
        self.embedding.word_embedding = value

    def get_contextualized_embeddings(self, input_ids: torch.Tensor, attention_mask: Optional[torch.Tensor] = None) -> list[torch.Tensor]:
        """
        """
        input_shape = input_ids.size()

        batch_size, seq_length = input_shape

        if attention_mask is None:
            attention_mask = input_ids.new_ones((seq_length, seq_length), dtype=torch.bool).triu(diagonal=1).unsqueeze(0).unsqueeze(0)

        if attention_mask is not None:
            attention_mask = ~attention_mask.bool()

            if len(attention_mask.size()) == 2:
                attention_mask = attention_mask.unsqueeze(1).unsqueeze(2)
            elif len(attention_mask.size()) == 3:
                attention_mask = attention_mask.unsqueeze(1)

            attention_mask = attention_mask | input_ids.new_ones((seq_length, seq_length), dtype=torch.bool).triu(1).unsqueeze(0).unsqueeze(0)

        static_embeddings = self.embedding(input_ids)
        contextualized_embeddings = [static_embeddings]
        attention_probs = []
        for layer in self.layers:
            layer_embeddings, layer_attention_probs = layer(contextualized_embeddings[-1], attention_mask)
            contextualized_embeddings.append(layer_embeddings)
            attention_probs.append(layer_attention_probs)
        last_layer = contextualized_embeddings[-1]
        return last_layer, contextualized_embeddings, attention_probs

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        output_hidden_states: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        **kwargs
    ) -> Union[tuple[torch.Tensor], BaseModelOutput]:
        """
        """
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        sequence_output, contextualized_embeddings, attention_probs = self.get_contextualized_embeddings(input_ids, attention_mask)

        if not return_dict:
            return (
                sequence_output,
                *([contextualized_embeddings] if output_hidden_states else []),
                *([attention_probs] if output_attentions else [])
            )

        return BaseModelOutput(
            last_hidden_state=sequence_output,
            hidden_states=contextualized_embeddings if output_hidden_states else None,
            attentions=attention_probs if output_attentions else None
        )

# To do Masked Language Modeling instead, you can replace MyModelForCausalLM by MyModelForMaskedLM
# and change the output type from CausalLMOutput to MaskedLMOutput.


class MyModelForCausalLM(MyModelPreTrainedModel):
    _keys_to_ignore_on_load_unexpected = ["lm_head"]

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.model = MyModel(config, **kwargs)
        self.vocab_size = config.vocab_size
        self.lm_head = CausalHead(config, self.model.embedding.word_embedding.weight)
        self.hidden_size = config.hidden_size

    def get_output_embeddings(self):
        return self.lm_head.lm_head[-1].weight

    def set_output_embeddings(self, new_embeddings):
        self.lm_head.lm_head[-1].weight = new_embeddings

    def get_input_embeddings(self):
        return self.model.embedding.word_embedding

    def set_input_embeddings(self, value):
        self.model.embedding.word_embedding = value

    def set_decoder(self, decoder):
        self.model = decoder

    def get_decoder(self):
        return self.model

    def can_generate(self):
        return True

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        token_type_ids: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.Tensor] = None,
        output_hidden_states: Optional[bool] = None,
        output_attentions: Optional[bool] = None,
        return_dict: Optional[bool] = None,
        labels: Optional[torch.LongTensor] = None,
        **kwargs
    ) -> Union[tuple, CausalLMOutput]:

        sequence_output, contextualized_embeddings, attention_probs = self.model.get_contextualized_embeddings(input_ids, attention_mask)
        subword_prediction = self.lm_head(sequence_output)

        loss = None
        if labels is not None:
            labels_flatten = labels[:, 1:].flatten()
            subword_prediction_flatten = subword_prediction[:, :-1].flatten(0, 1)
            loss = F.cross_entropy(subword_prediction_flatten, labels_flatten)

        if not return_dict:
            output = (
                subword_prediction,
                *([contextualized_embeddings] if output_hidden_states else []),
                *([attention_probs] if output_attentions else [])
            )
            return ((loss,) + output) if loss is not None else output

        return CausalLMOutput(
            loss=loss,
            logits=subword_prediction,
            hidden_states=contextualized_embeddings if output_hidden_states else None,
            attentions=attention_probs if output_attentions else None
        )
