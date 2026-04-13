#!/bin/bash

MODEL_NAME=""
langs="eng nld zho"
LR=5e-5
PATIENCE=3
BSZ=64
MAX_EPOCHS=10
SEED=12

while [[ $# -gt 0 ]]; do
    case "$1" in
        --model_name)  MODEL_NAME="$2";  shift 2 ;;
        --langs)       langs="$2";       shift 2 ;;
        --lr)          LR="$2";          shift 2 ;;
        --patience)    PATIENCE="$2";    shift 2 ;;
        --bsz)         BSZ="$2";         shift 2 ;;
        --max_epochs)  MAX_EPOCHS="$2";  shift 2 ;;
        --seed)        SEED="$2";        shift 2 ;;
        *) echo "Unknown argument: $1"; exit 1 ;;
    esac
done

if [[ -z "$MODEL_NAME" ]]; then
    echo "Error: --model_name is required"; exit 1
fi


# NOTE: if you've already run finetuning and just want to generate predictions,
# you can set `--model_name_or_path "results/finetune/$model_basename/$TRAIN_NAME/"`
# and remove the `--do_train` and `--do_eval` arguments.

model_basename=$(basename $MODEL_NAME)
for LANGUAGE in $langs; do
    for task in arc belebele bmlama include mnli sib200 truthfulqa xnli; do
        TRAIN_NAME=$task
        VALID_NAME=$task
        DO_TRAIN=True
        MODEL_NAME_FULL=$MODEL_NAME

        mkdir -p finetune/results/finetune/$model_basename/$task/

        python3 finetune/finetune_classification.py \
              --model_name_or_path "$MODEL_NAME" \
              --language "$LANGUAGE" \
              --output_dir "finetuning_babybabel_lm/results/finetune/${model_basename}/${task}" \
              --train_file "finetuning_babybabel_lm/finetuning_data/${task}/${LANGUAGE}/${task}_${LANGUAGE}.train.jsonl" \
              --validation_file "finetuning_babybabel_lm/finetuning_data/${task}/${LANGUAGE}/${task}_${LANGUAGE}.valid.jsonl" \
              --do_train $DO_TRAIN \
              --do_eval \
              --do_predict \
              --max_seq_length 128 \
              --per_device_train_batch_size "$BSZ" \
              --learning_rate "$LR" \
              --num_train_epochs "$MAX_EPOCHS" \
              --patience "$PATIENCE" \
              --eval_strategy epoch \
              --save_strategy epoch \
              --overwrite_output_dir \
              --seed "$SEED"
    done
done

# Add `--trust_remote_code` if you need to load custom config/model files.
# If you run into memory issues, try reducing $BSZ or reducing `--max_seq_length` first.