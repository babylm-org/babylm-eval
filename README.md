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

- `babybabellm` — main BabyLM task, available per language (e.g. `babybabellm_eng`)
- `multiblimp` — morphosyntactic evaluation
- `bl2mp`, `zhoblimp` — additional BLiMP-style tasks
- `hellaswag_mubench`, `xstorycloze`, `xcomps` — commonsense reasoning
- `arc_challenge_mubench`, `arc_easy_mubench` — reading comprehension
- `bmlama_mubench`, `sib200`, `multinli_mubench`, `snli_mubench`, `truthfulqa_mubench`, `winogrande_mubench`, `gpqa_mubench` — additional benchmarks

## Baselines

| task | gpt2-baseline-BabyLM-2026-Strict | gpt2-baseline-babylm-nld | gpt2-baseline-en_nld_zho_equal | gpt2-baseline-nld_zho_equal |
| --- | --- | --- | --- | --- |
| **zeroshot_eng** |  |  |  |  |
| blimp | 73.43 |  | 69.18 |  |
| hellaswag_en_mubench | 26.49 |  | 26.66 |  |
| multiblimp_eng | 88.57 |  | 87.14 |  |
| winogrande_en_mubench | 51.44 |  | 48.80 |  |
| xstorycloze_en_mubench | 49.23 |  | 49.92 |  |
| *avg* | 57.83 |  | 56.34 |  |
| **zeroshot_nld** |  |  |  |  |
| blimp_nl |  | 84.12 | 79.27 | 80.47 |
| hellaswag_nl_mubench |  | 26.79 | 26.37 | 26.71 |
| multiblimp_nld |  | 94.72 | 91.85 | 94.04 |
| winogrande_nl_mubench |  | 49.88 | 49.30 | 48.47 |
| xcomps_nl |  | 54.54 | 52.68 | 52.87 |
| xstorycloze_nl_mubench |  | 47.60 | 47.37 | 49.23 |
| *avg* |  | 59.61 | 57.81 | 58.63 |
| **zeroshot_zho** |  |  |  |  |
| hellaswag_zh_mubench |  |  | 27.05 | 27.20 |
| winogrande_zh_mubench |  |  | 49.71 | 50.37 |
| xcomps_zh |  |  | 53.90 | 53.59 |
| xstorycloze_zh_mubench |  |  | 50.62 | 50.54 |
| zhoblimp |  |  | 75.44 | 77.23 |
| *avg* |  |  | 51.34 | 51.79 |