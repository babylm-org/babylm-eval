# BabyLM Evaluation 2026
![BabyLM Challenge](strict/assets/babylm.png)

This repository contains the setup for evaluation for BabyLM 2026. We provide separate evaluation for the Strict (+Strict-Small) track, and the Multilingual track. See the two track directories for more specific information on evaluation for these two tracks.

## Installation

```bash
pip install -r requirements.txt
```

## Baselines
We train GPT-2 baseline models on the datasets. We provide monolingual models, as well as bi- and trilingual models, trained on equal language splits. The models are available on HuggingFace [here](https://huggingface.co/BabyLM-community/models).

Following [BabyBabelLM](https://arxiv.org/pdf/2510.10159), we divide evaluation for the multilingual models up in zero-shot and fine-tuning evaluation. Zero-shot evaluation is done through `lm-eval`. Fine-tuning is adapted from a script of previous BabyLM editions.

### Strict / Strict-Small
#### Zero-shot Tasks
| task | gpt2-baseline-BabyLM-2026-Strict | gpt2-baseline-BabyLM-2026-Strict-Small |
| --- | --- | --- |
| zero_shot/blimp/blimp_filtered | **74.53** | 65.08 |
| zero_shot/blimp/supplement_filtered | **65.00** | 57.25 |
| zero_shot/comps/comps | **55.85** | 51.81 |
| zero_shot/entity_tracking/entity_tracking | **23.58** | 21.07 |
| zero_shot/wug_adj/wug_adj_nominalization | **0.62** | 0.56 |
| zero_shot/wug_past/wug_past_tense | **0.19** | 0.16 |

### Multilingual Track
#### Zero-shot Tasks
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

#### Finetuning tasks
| task | gpt2-baseline-BabyLM-2026-Strict | gpt2-baseline-BabyLM-2026-Strict-Small | gpt2-baseline-babylm-nld | gpt2-baseline-babylm-zho | gpt2-baseline-en_nld_equal | gpt2-baseline-en_zho_equal | gpt2-baseline-nld_zho_equal | gpt2-baseline-en_nld_zho_equal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **en** |  |  |  |  |  |  |  |  |
| arc | 24.79 | 24.79 |  |  | 24.58 | **25.21** |  | 24.79 |
| belebele | 23.30 | 26.14 |  |  | **26.70** | 22.73 |  | 22.16 |
| bmlama | 11.26 | 10.60 |  |  | **12.83** | 9.85 |  | 9.35 |
| mnli |  | 45.89 |  |  | 46.90 | 49.66 |  | **51.63** |
| sib200 |  | 42.00 |  |  | **79.00** | 21.50 |  | 21.50 |
| truthfulqa |  | 19.64 |  |  | **22.32** | **22.32** |  | **22.32** |
| xnli |  | 43.20 |  |  | 45.25 | 44.30 |  | **46.65** |
| *avg* | 19.78 | 30.32 |  |  | **36.80** | 27.94 |  | 28.34 |
| **nl** |  |  |  |  |  |  |  |  |
| arc |  |  | **24.38** |  | 24.17 |  | **24.38** | **24.38** |
| belebele |  |  | 26.70 |  | 29.55 |  | 21.02 | **30.11** |
| bmlama |  |  | **13.25** |  | 11.42 |  | 10.18 | 10.68 |
| include |  |  | 19.64 |  | **35.71** |  | 34.82 | 19.64 |
| mnli |  |  | 49.04 |  | **51.52** |  | 45.55 | 43.92 |
| sib200 |  |  | 74.50 |  | **76.00** |  | 21.50 | 21.50 |
| truthfulqa |  |  | **23.21** |  | 17.86 |  | **23.21** | **23.21** |
| *avg* |  |  | 32.96 |  | **35.18** |  | 25.81 | 24.78 |
| **zh** |  |  |  |  |  |  |  |  |
| arc |  |  |  | 25.83 |  | 24.58 | **26.25** | 25.00 |
| belebele |  |  |  | 21.02 |  | 22.16 | **23.30** | 22.73 |
| bmlama |  |  |  | **11.67** |  | 9.85 | 9.35 | 9.35 |
| include |  |  |  | **32.14** |  | 26.79 | 19.64 | 26.79 |
| mnli |  |  |  | **48.03** |  | 46.79 | 45.16 | 45.83 |
| sib200 |  |  |  | 21.50 |  | **80.50** | 21.50 | 21.50 |
| truthfulqa |  |  |  | **27.68** |  | 23.21 | 25.00 | 23.21 |
| xnli |  |  |  | 46.05 |  | **46.25** | 43.95 | 43.45 |
| *avg* |  |  |  | 29.24 |  | **35.02** | 26.77 | 27.23 |

## Citation
```
@misc{choshen2026babylmturns4goes,
      title={BabyLM Turns 4 and Goes Multilingual: Call for Papers for the 2026 BabyLM Workshop}, 
      author={Leshem Choshen and Ryan Cotterell and Mustafa Omer Gul and Jaap Jumelet and Tal Linzen and Aaron Mueller and Suchir Salhan and Raj Sanjay Shah and Alex Warstadt and Ethan Gotlieb Wilcox},
      year={2026},
      eprint={2602.20092},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.20092}, 
}
```