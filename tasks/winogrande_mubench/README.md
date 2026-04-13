# Winogrande

### Paper

Title: `MuBench: Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages`

Abstract: Multilingual large language models (LLMs) are advancing rapidly, with new models frequently claiming support for an increasing number of languages. However, existing evaluation datasets are limited and lack cross-lingual alignment, leaving assessments of multilingual capabilities fragmented in both language and skill coverage. To address this, we introduce MuBench, a benchmark covering 61 languages and evaluating a broad range of capabilities. We evaluate several state-of-the-art multilingual LLMs and find notable gaps between claimed and actual language coverage, particularly a persistent performance disparity between English and low-resource languages. Leveraging MuBench's alignment, we propose Multilingual Consistency (MLC) as a complementary metric to accuracy for analyzing performance bottlenecks and guiding model improvement. Finally, we pretrain a suite of 1.2B-parameter models on English and Chinese with 500B tokens, varying language ratios and parallel data proportions to investigate cross-lingual transfer dynamics.

Homepage: https://huggingface.co/datasets/aialt/MuBench


### Citation

```
@misc{han2025mubench,
      title={MuBench: Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages}, 
      author={Wenhan Han and Yifan Zhang and Zhixun Chen and Binbin Liu and Haobin Lin and Bingni Zhang and Taifeng Wang and Mykola Pechenizkiy and Meng Fang and Yin Zheng},
      year={2025},
      eprint={2506.19468},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.19468}, 
}
```

### Groups and Tasks

#### Groups

* `winogrande_mubench`

#### Tasks
* `winogrande_af_mubench`: Afrikaans
* `winogrande_ar_mubench`: Arabic
* `winogrande_az_mubench`: Azerbaijani
* `winogrande_bg_mubench`: Bulgarian
* `winogrande_bn_mubench`: Bengali
* `winogrande_ca_mubench`: Catalan
* `winogrande_ceb_mubench`: Cebuano
* `winogrande_cs_mubench`: Czech
* `winogrande_da_mubench`: Danish
* `winogrande_de_mubench`: German
* `winogrande_el_mubench`: Greek
* `winogrande_en_mubench`: English
* `winogrande_es_mubench`: Spanish
* `winogrande_et_mubench`: Estonian
* `winogrande_fa_mubench`: Persian
* `winogrande_fi_mubench`: Finnish
* `winogrande_fr_mubench`: French
* `winogrande_ga_mubench`: Irish
* `winogrande_gu_mubench`: Gujarati
* `winogrande_he_mubench`: Hebrew
* `winogrande_hi_mubench`: Hindi
* `winogrande_hr_mubench`: Croatian
* `winogrande_hu_mubench`: Hungarian
* `winogrande_id_mubench`: Indonesian
* `winogrande_is_mubench`: Icelandic
* `winogrande_it_mubench`: Italian
* `winogrande_ja_mubench`: Japanese
* `winogrande_jv_mubench`: Javanese
* `winogrande_kk_mubench`: Kazakh
* `winogrande_km_mubench`: Khmer
* `winogrande_kn_mubench`: Kannada
* `winogrande_ko_mubench`: Korean
* `winogrande_lt_mubench`: Lithuanian
* `winogrande_lv_mubench`: Latvian
* `winogrande_ml_mubench`: Malayalam
* `winogrande_mr_mubench`: Marathi
* `winogrande_ms_mubench`: Malay
* `winogrande_my_mubench`: Myanmar
* `winogrande_nl_mubench`: Dutch
* `winogrande_no_mubench`: Norwegian
* `winogrande_pa_mubench`: Punjabi
* `winogrande_pl_mubench`: Polish
* `winogrande_pt_mubench`: Portuguese
* `winogrande_ro_mubench`: Romanian
* `winogrande_ru_mubench`: Russian
* `winogrande_sk_mubench`: Slovak
* `winogrande_sl_mubench`: Slovenian
* `winogrande_sq_mubench`: Albanian
* `winogrande_sr_mubench`: Serbian
* `winogrande_sv_mubench`: Swedish
* `winogrande_sw_mubench`: Swahili
* `winogrande_ta_mubench`: Tamil
* `winogrande_te_mubench`: Telugu
* `winogrande_th_mubench`: Thai
* `winogrande_tl_mubench`: Filipino
* `winogrande_tr_mubench`: Turkish
* `winogrande_uk_mubench`: Ukrainian
* `winogrande_ur_mubench`: Urdu
* `winogrande_uz_mubench`: Uzbek
* `winogrande_vi_mubench`: Vietnamese
* `winogrande_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
