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