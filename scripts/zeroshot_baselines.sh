#!/bin/bash

declare -A model_langs=(
    ["BabyLM-community/gpt2-baseline-nld_zho_equal"]="nld zho"
    ["BabyLM-community/gpt2-baseline-en_zho_equal"]="eng zho"
    ["BabyLM-community/gpt2-baseline-en_nld_equal"]="eng nld"
    ["BabyLM-community/gpt2-baseline-en_nld_zho_equal"]="eng nld zho"
    ["BabyLM-community/gpt2-baseline-babylm-zho"]="zho"
    ["BabyLM-community/gpt2-baseline-babylm-nld"]="nld"
    ["BabyLM-community/gpt2-baseline-BabyLM-2026-Strict-Small"]="eng"
    ["BabyLM-community/gpt2-baseline-BabyLM-2026-Strict"]="eng"
)

for model_name in "${!model_langs[@]}"; do
    echo "Evaluating ${model_name}"
    bash zeroshot_model.sh --model_name ${model_name} --langs "${model_langs[$model_name]}"
done