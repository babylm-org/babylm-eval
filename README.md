# BabyLM Evaluation 2026

This repository contains the evaluation pipeline for the 2026 BabyLM Challenge. It uses [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) with custom tasks defined in `tasks/`.

## Installation

```bash
pip install -r requirements.txt
```

## Running evaluation

Use `scripts/eval_model.sh` to evaluate a model across languages:

```bash
bash scripts/zeroshot_model.sh --model_name <path_or_hf_name>
```

By default, evaluation runs for `eng`, `nld`, and `zho`. Use `--langs` to override:

```bash
bash scripts/zeroshot_model.sh --model_name <path_or_hf_name> --langs "eng zho"
```

Results are written to `results/<model_name>/`.

## Tasks

Custom tasks are located in `tasks/`. Notable ones:

- `zeroshot_babybabellm` — main BabyLM task, available per language (e.g. `zeroshot_eng`)
- `multiblimp` — Multilingual subject-verb agreement evaluation.
- `blimp`, `blimp_nl`, `zhoblimp` — additional language-specific linguistic evaluation for English, Dutch and Chinese.
- `hellaswag_mubench`, `xstorycloze`, `xcomps` — Commonsense reasoning
- `arc_challenge_mubench`, `arc_easy_mubench` — Reading comprehension (evaluated through finetuning)
- `bmlama_mubench`, `sib200`, `multinli_mubench`, `snli_mubench`, `truthfulqa_mubench`, `winogrande_mubench`, `gpqa_mubench` — additional benchmarks (evaluated through finetuning)

## Baselines
We train GPT-2 baseline models on the datasets. We provide monolingual models, as well as bi- and trilingual models, trained on equal language splits. The models are available on HuggingFace [here](https://huggingface.co/BabyLM-community/models).

Following [BabyBabelLM](https://arxiv.org/pdf/2510.10159), we divide evaluation for the multilingual models up in zero-shot and fine-tuning evaluation. Zero-shot evaluation is done through `lm-eval`. Fine-tuning is adapted from a script of previous BabyLM editions.

| task | gpt2-baseline-BabyLM-2026-Strict | gpt2-baseline-BabyLM-2026-Strict-Small | gpt2-baseline-babylm-nld | gpt2-baseline-babylm-zho | gpt2-baseline-en_nld_equal | gpt2-baseline-en_zho_equal | gpt2-baseline-nld_zho_equal | gpt2-baseline-en_nld_zho_equal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **zeroshot_eng** |  |  |  |  |  |  |  |  |
| blimp | **73.43** | 64.39 |  |  | 71.77 | 71.01 |  | 69.18 |
| hellaswag_en_mubench | 26.49 | 25.70 |  |  | 26.43 | 26.30 |  | **26.66** |
| multiblimp_eng | **88.57** | 80.39 |  |  | 87.92 | 86.49 |  | 87.14 |
| winogrande_en_mubench | 51.44 | 51.03 |  |  | 50.54 | **52.84** |  | 48.80 |
| xstorycloze_en_mubench | 49.23 | 48.37 |  |  | 47.37 | **49.92** |  | **49.92** |
| *avg* | **57.83** | 53.98 |  |  | 56.81 | 57.31 |  | 56.34 |
| **zeroshot_nld** |  |  |  |  |  |  |  |  |
| blimp_nl |  |  | **84.12** |  | 81.70 |  | 80.47 | 79.27 |
| hellaswag_nl_mubench |  |  | **26.79** |  | 26.38 |  | 26.71 | 26.37 |
| multiblimp_nld |  |  | **94.72** |  | 92.62 |  | 94.04 | 91.85 |
| winogrande_nl_mubench |  |  | **49.88** |  | 48.80 |  | 48.47 | 49.30 |
| xcomps_nl |  |  | **54.54** |  | 53.87 |  | 52.87 | 52.68 |
| xstorycloze_nl_mubench |  |  | 47.60 |  | 47.99 |  | **49.23** | 47.37 |
| *avg* |  |  | **59.61** |  | 58.56 |  | 58.63 | 57.81 |
| **zeroshot_zho** |  |  |  |  |  |  |  |  |
| hellaswag_zh_mubench |  |  |  | **27.78** |  | 26.72 | 27.20 | 27.05 |
| winogrande_zh_mubench |  |  |  | **51.85** |  | 50.62 | 50.37 | 49.71 |
| xcomps_zh |  |  |  | **55.70** |  | 53.74 | 53.59 | 53.90 |
| xstorycloze_zh_mubench |  |  |  | 50.23 |  | **51.55** | 50.54 | 50.62 |
| zhoblimp |  |  |  | **78.79** |  | 78.60 | 77.23 | 75.44 |
| *avg* |  |  |  | **52.87** |  | 52.25 | 51.79 | 51.34 |