from __future__ import annotations

import json
import pathlib
import copy
from transformers.configuration_utils import PretrainedConfig


class ModelConfig(PretrainedConfig):

    def __init__(self: ModelConfig, config_file: pathlib.Path | str | None = None, **kwargs):
        """
        """
        super().__init__(**kwargs)
        if config_file is None:
            self.attention_bias = True
            self.attention_dropout_p = 0.1
            self.attention_layernorm_learned = True
            self.attention_probabilities_dropout_p = 0.1
            self.embedding_dropout_prob = 0.1
            self.embedding_layernorm_learned = True
            self.hidden_size = 384
            self.intermediate_size = 1024
            self.layernorm_eps = 1e-5
            self.lm_head_layernorm_learned = True
            self.max_sequence_length = 512
            self.mlp_bias = True
            self.mlp_layernorm_learned = True
            self.num_attention_heads = 6
            self.num_layers = 6
            self.rope_theta = 10000
            self.vocab_size = 6144
        else:
            if config_file == "str":
                config_file = pathlib.Path(config_file)

            config = json.load(config_file.open("r"))

            for key, value in config.items():
                setattr(self, key, value)

    def __repr__(self) -> str:
        return str(self.to_json_string())

    def to_dict(self) -> dict:
        """Serializes this instance to a Python dictionary."""
        output: dict

        output = copy.deepcopy(self.__dict__)
        return output

    def to_json_string(self) -> str:
        """Serializes this instance to a JSON string."""
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def to_json_file(self, json_file_path: pathlib.Path | str) -> None:
        """Save this instance to a json file."""
        if isinstance(json_file_path, str):
            json_file_path: pathlib.Path = pathlib.Path(json_file_path)
        with json_file_path.open("w", encoding='utf-8') as writer:
            writer.write(self.to_json_string())
