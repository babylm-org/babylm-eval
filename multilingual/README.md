# Multilingual Track Evaluation

This repository contains the evaluation pipeline for the **multilingual track** of the 2026 BabyLM Challenge. It uses [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) with custom tasks defined in `tasks/`.

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
