#!/bin/bash
model_name=""
langs="eng nld zho"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --model_name) model_name="$2"; shift 2 ;;
        --langs) langs="$2"; shift 2 ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

if [[ -z "$model_name" ]]; then
    echo "Error: --model_name is required"; exit 1
fi

for lang in $langs; do
    task_name="zeroshot_${lang}"
    echo "Evaluating ${lang}"
    python3 -m lm_eval \
        --model hf \
        --model_args pretrained=${model_name} \
        --tasks ${task_name} \
        --device cuda \
        --output_path ../results \
        --batch_size auto:10 \
        --num_fewshot 0 \
        --log_samples \
        --include_path ../tasks/

    echo "Completed evaluation for ${lang}"
done