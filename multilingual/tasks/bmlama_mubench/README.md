# Bmlama

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

* `bmlama_mubench`

#### Tasks
* `bmlama_af_mubench`: Afrikaans
* `bmlama_ar_mubench`: Arabic
* `bmlama_az_mubench`: Azerbaijani
* `bmlama_bg_mubench`: Bulgarian
* `bmlama_bn_mubench`: Bengali
* `bmlama_ca_mubench`: Catalan
* `bmlama_ceb_mubench`: Cebuano
* `bmlama_cs_mubench`: Czech
* `bmlama_da_mubench`: Danish
* `bmlama_de_mubench`: German
* `bmlama_el_mubench`: Greek
* `bmlama_en_mubench`: English
* `bmlama_es_mubench`: Spanish
* `bmlama_et_mubench`: Estonian
* `bmlama_fa_mubench`: Persian
* `bmlama_fi_mubench`: Finnish
* `bmlama_fr_mubench`: French
* `bmlama_ga_mubench`: Irish
* `bmlama_gu_mubench`: Gujarati
* `bmlama_he_mubench`: Hebrew
* `bmlama_hi_mubench`: Hindi
* `bmlama_hr_mubench`: Croatian
* `bmlama_hu_mubench`: Hungarian
* `bmlama_id_mubench`: Indonesian
* `bmlama_is_mubench`: Icelandic
* `bmlama_it_mubench`: Italian
* `bmlama_ja_mubench`: Japanese
* `bmlama_jv_mubench`: Javanese
* `bmlama_kk_mubench`: Kazakh
* `bmlama_km_mubench`: Khmer
* `bmlama_kn_mubench`: Kannada
* `bmlama_ko_mubench`: Korean
* `bmlama_lt_mubench`: Lithuanian
* `bmlama_lv_mubench`: Latvian
* `bmlama_ml_mubench`: Malayalam
* `bmlama_mr_mubench`: Marathi
* `bmlama_ms_mubench`: Malay
* `bmlama_my_mubench`: Myanmar
* `bmlama_nl_mubench`: Dutch
* `bmlama_no_mubench`: Norwegian
* `bmlama_pa_mubench`: Punjabi
* `bmlama_pl_mubench`: Polish
* `bmlama_pt_mubench`: Portuguese
* `bmlama_ro_mubench`: Romanian
* `bmlama_ru_mubench`: Russian
* `bmlama_sk_mubench`: Slovak
* `bmlama_sl_mubench`: Slovenian
* `bmlama_sq_mubench`: Albanian
* `bmlama_sr_mubench`: Serbian
* `bmlama_sv_mubench`: Swedish
* `bmlama_sw_mubench`: Swahili
* `bmlama_ta_mubench`: Tamil
* `bmlama_te_mubench`: Telugu
* `bmlama_th_mubench`: Thai
* `bmlama_tl_mubench`: Filipino
* `bmlama_tr_mubench`: Turkish
* `bmlama_uk_mubench`: Ukrainian
* `bmlama_ur_mubench`: Urdu
* `bmlama_uz_mubench`: Uzbek
* `bmlama_vi_mubench`: Vietnamese
* `bmlama_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
