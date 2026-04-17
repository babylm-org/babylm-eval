# Multinli

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

* `multinli_mubench`

#### Tasks
* `multinli_af_mubench`: Afrikaans
* `multinli_ar_mubench`: Arabic
* `multinli_az_mubench`: Azerbaijani
* `multinli_bg_mubench`: Bulgarian
* `multinli_bn_mubench`: Bengali
* `multinli_ca_mubench`: Catalan
* `multinli_ceb_mubench`: Cebuano
* `multinli_cs_mubench`: Czech
* `multinli_da_mubench`: Danish
* `multinli_de_mubench`: German
* `multinli_el_mubench`: Greek
* `multinli_en_mubench`: English
* `multinli_es_mubench`: Spanish
* `multinli_et_mubench`: Estonian
* `multinli_fa_mubench`: Persian
* `multinli_fi_mubench`: Finnish
* `multinli_fr_mubench`: French
* `multinli_ga_mubench`: Irish
* `multinli_gu_mubench`: Gujarati
* `multinli_he_mubench`: Hebrew
* `multinli_hi_mubench`: Hindi
* `multinli_hr_mubench`: Croatian
* `multinli_hu_mubench`: Hungarian
* `multinli_id_mubench`: Indonesian
* `multinli_is_mubench`: Icelandic
* `multinli_it_mubench`: Italian
* `multinli_ja_mubench`: Japanese
* `multinli_jv_mubench`: Javanese
* `multinli_kk_mubench`: Kazakh
* `multinli_km_mubench`: Khmer
* `multinli_kn_mubench`: Kannada
* `multinli_ko_mubench`: Korean
* `multinli_lt_mubench`: Lithuanian
* `multinli_lv_mubench`: Latvian
* `multinli_ml_mubench`: Malayalam
* `multinli_mr_mubench`: Marathi
* `multinli_ms_mubench`: Malay
* `multinli_my_mubench`: Myanmar
* `multinli_nl_mubench`: Dutch
* `multinli_no_mubench`: Norwegian
* `multinli_pa_mubench`: Punjabi
* `multinli_pl_mubench`: Polish
* `multinli_pt_mubench`: Portuguese
* `multinli_ro_mubench`: Romanian
* `multinli_ru_mubench`: Russian
* `multinli_sk_mubench`: Slovak
* `multinli_sl_mubench`: Slovenian
* `multinli_sq_mubench`: Albanian
* `multinli_sr_mubench`: Serbian
* `multinli_sv_mubench`: Swedish
* `multinli_sw_mubench`: Swahili
* `multinli_ta_mubench`: Tamil
* `multinli_te_mubench`: Telugu
* `multinli_th_mubench`: Thai
* `multinli_tl_mubench`: Filipino
* `multinli_tr_mubench`: Turkish
* `multinli_uk_mubench`: Ukrainian
* `multinli_ur_mubench`: Urdu
* `multinli_uz_mubench`: Uzbek
* `multinli_vi_mubench`: Vietnamese
* `multinli_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
