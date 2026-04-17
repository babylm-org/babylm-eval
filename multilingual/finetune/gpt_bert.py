import torch
import torch.nn as nn
from transformers import AutoModelForMaskedLM, PreTrainedModel, AutoConfig
from transformers.modeling_outputs import SequenceClassifierOutput


def _normalize_mask_tensor(mask):
    if mask.dtype == torch.bool:
        if mask.numel() == 0:
            return mask
        true_fraction = mask.float().mean().item()
        if true_fraction > 0.5:
            mask = ~mask
    else:
        mask = mask <= 0
    return mask.to(torch.bool)


def _ensure_valid_rows(mask):
    row_masked = mask.all(dim=-1)
    if row_masked.any():
        idx = row_masked.nonzero(as_tuple=False)
        mask[idx[:, 0], idx[:, 1], idx[:, 1]] = False
    return mask


def _build_babylm_attention_mask(input_ids, attention_mask):
    batch_size, seq_len = input_ids.shape[:2]
    device = input_ids.device
    if attention_mask is None:
        mask = torch.zeros(batch_size, seq_len, seq_len, dtype=torch.bool, device=device)
    else:
        mask = attention_mask
        if mask.dim() == 0:
            mask = mask.unsqueeze(0)
        if mask.dim() == 1:
            mask = mask.unsqueeze(0)
        if mask.dim() == 2:
            mask = _normalize_mask_tensor(mask)
            mask = mask.unsqueeze(1) | mask.unsqueeze(2)
        elif mask.dim() == 3:
            if mask.size(1) == 1 and mask.size(2) == seq_len:
                mask = _normalize_mask_tensor(mask.squeeze(1))
                mask = mask.unsqueeze(1) | mask.unsqueeze(2)
            elif mask.size(1) == seq_len and mask.size(2) == 1:
                mask = _normalize_mask_tensor(mask.squeeze(2))
                mask = mask.unsqueeze(1) | mask.unsqueeze(2)
            else:
                mask = _normalize_mask_tensor(mask)
        elif mask.dim() == 4:
            if mask.size(1) == 1:
                mask = mask[:, 0]
            else:
                mask = mask.any(dim=1)
            mask = _normalize_mask_tensor(mask)
        else:
            raise ValueError("Unsupported attention_mask dimensions: {}".format(mask.dim()))
        mask = mask.to(device=device, dtype=torch.bool)
        if mask.dim() == 2:
            mask = mask.unsqueeze(1) | mask.unsqueeze(2)
        if mask.dim() != 3:
            raise ValueError("attention_mask must broadcast to a square matrix")
        if mask.size(0) == 1 and batch_size > 1:
            mask = mask.expand(batch_size, -1, -1).clone()
        elif mask.size(0) != batch_size:
            raise ValueError("attention_mask batch dimension {} does not match inputs {}".format(mask.size(0), batch_size))
        rows = min(mask.size(1), seq_len)
        cols = min(mask.size(2), seq_len)
        if mask.size(1) != seq_len or mask.size(2) != seq_len:
            new_mask = torch.ones(batch_size, seq_len, seq_len, dtype=torch.bool, device=device)
            new_mask[:, :rows, :cols] = mask[:, :rows, :cols]
            mask = new_mask
    mask = _ensure_valid_rows(mask)
    return mask.unsqueeze(1)


class ClassifierHead(nn.Module):
    def __init__(self, config) -> None:
        super().__init__()
        self.nonlinearity: nn.Sequential = nn.Sequential(
            nn.LayerNorm(config.hidden_size, 1.0e-5, elementwise_affine=False),
            nn.Linear(config.hidden_size, config.hidden_size),
            nn.GELU(),
            nn.LayerNorm(config.hidden_size, 1.0e-5, elementwise_affine=False),
            nn.Dropout(0.1),
            nn.Linear(config.hidden_size, config.num_labels)
        )

    def forward(self, eembeddings):
        return self.nonlinearity(eembeddings)



class GPTBertForSequenceClassification(PreTrainedModel):
    def __init__(self, model_name, config):
        super().__init__(config)
        print(config)
        self.gptbert = AutoModelForMaskedLM.from_pretrained(model_name, trust_remote_code=True)

        self.classifier = ClassifierHead(config)        
        self.post_init()

    def forward(self, input_ids=None, attention_mask=None, labels=None, **kwargs):
        mask_4d = _build_babylm_attention_mask(input_ids, attention_mask)
        static_embeddings, relative_embedding = self.gptbert.model.embedding(input_ids)
        if static_embeddings.dim() == 3 and static_embeddings.shape[0] == input_ids.shape[0]:
            static_embeddings = static_embeddings.transpose(0, 1)
        outputs = self.gptbert.model.transformer(static_embeddings, mask_4d, relative_embedding)

        # pooled = outputs[0]  # [CLS] position
        sequence_lengths = attention_mask.sum(-1) - 1
        pooled = outputs[sequence_lengths, torch.arange(outputs.size(1))]

        logits = self.classifier(pooled)

        loss = None
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.config.num_labels), labels.view(-1))
        else:
            print(f"Warning, labels is None for input of shape {input_ids.shape}")

        return SequenceClassifierOutput(loss=loss, logits=logits)