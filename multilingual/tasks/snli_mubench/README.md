# Snli

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

* `snli_mubench`

#### Tasks
* `snli_af_mubench`: Afrikaans
* `snli_ar_mubench`: Arabic
* `snli_az_mubench`: Azerbaijani
* `snli_bg_mubench`: Bulgarian
* `snli_bn_mubench`: Bengali
* `snli_ca_mubench`: Catalan
* `snli_ceb_mubench`: Cebuano
* `snli_cs_mubench`: Czech
* `snli_da_mubench`: Danish
* `snli_de_mubench`: German
* `snli_el_mubench`: Greek
* `snli_en_mubench`: English
* `snli_es_mubench`: Spanish
* `snli_et_mubench`: Estonian
* `snli_fa_mubench`: Persian
* `snli_fi_mubench`: Finnish
* `snli_fr_mubench`: French
* `snli_ga_mubench`: Irish
* `snli_gu_mubench`: Gujarati
* `snli_he_mubench`: Hebrew
* `snli_hi_mubench`: Hindi
* `snli_hr_mubench`: Croatian
* `snli_hu_mubench`: Hungarian
* `snli_id_mubench`: Indonesian
* `snli_is_mubench`: Icelandic
* `snli_it_mubench`: Italian
* `snli_ja_mubench`: Japanese
* `snli_jv_mubench`: Javanese
* `snli_kk_mubench`: Kazakh
* `snli_km_mubench`: Khmer
* `snli_kn_mubench`: Kannada
* `snli_ko_mubench`: Korean
* `snli_lt_mubench`: Lithuanian
* `snli_lv_mubench`: Latvian
* `snli_ml_mubench`: Malayalam
* `snli_mr_mubench`: Marathi
* `snli_ms_mubench`: Malay
* `snli_my_mubench`: Myanmar
* `snli_nl_mubench`: Dutch
* `snli_no_mubench`: Norwegian
* `snli_pa_mubench`: Punjabi
* `snli_pl_mubench`: Polish
* `snli_pt_mubench`: Portuguese
* `snli_ro_mubench`: Romanian
* `snli_ru_mubench`: Russian
* `snli_sk_mubench`: Slovak
* `snli_sl_mubench`: Slovenian
* `snli_sq_mubench`: Albanian
* `snli_sr_mubench`: Serbian
* `snli_sv_mubench`: Swedish
* `snli_sw_mubench`: Swahili
* `snli_ta_mubench`: Tamil
* `snli_te_mubench`: Telugu
* `snli_th_mubench`: Thai
* `snli_tl_mubench`: Filipino
* `snli_tr_mubench`: Turkish
* `snli_uk_mubench`: Ukrainian
* `snli_ur_mubench`: Urdu
* `snli_uz_mubench`: Uzbek
* `snli_vi_mubench`: Vietnamese
* `snli_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
