# Arc Easy

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

* `arc_easy_mubench`

#### Tasks
* `arc_easy_af_mubench`: Afrikaans
* `arc_easy_ar_mubench`: Arabic
* `arc_easy_az_mubench`: Azerbaijani
* `arc_easy_bg_mubench`: Bulgarian
* `arc_easy_bn_mubench`: Bengali
* `arc_easy_ca_mubench`: Catalan
* `arc_easy_ceb_mubench`: Cebuano
* `arc_easy_cs_mubench`: Czech
* `arc_easy_da_mubench`: Danish
* `arc_easy_de_mubench`: German
* `arc_easy_el_mubench`: Greek
* `arc_easy_en_mubench`: English
* `arc_easy_es_mubench`: Spanish
* `arc_easy_et_mubench`: Estonian
* `arc_easy_fa_mubench`: Persian
* `arc_easy_fi_mubench`: Finnish
* `arc_easy_fr_mubench`: French
* `arc_easy_ga_mubench`: Irish
* `arc_easy_gu_mubench`: Gujarati
* `arc_easy_he_mubench`: Hebrew
* `arc_easy_hi_mubench`: Hindi
* `arc_easy_hr_mubench`: Croatian
* `arc_easy_hu_mubench`: Hungarian
* `arc_easy_id_mubench`: Indonesian
* `arc_easy_is_mubench`: Icelandic
* `arc_easy_it_mubench`: Italian
* `arc_easy_ja_mubench`: Japanese
* `arc_easy_jv_mubench`: Javanese
* `arc_easy_kk_mubench`: Kazakh
* `arc_easy_km_mubench`: Khmer
* `arc_easy_kn_mubench`: Kannada
* `arc_easy_ko_mubench`: Korean
* `arc_easy_lt_mubench`: Lithuanian
* `arc_easy_lv_mubench`: Latvian
* `arc_easy_ml_mubench`: Malayalam
* `arc_easy_mr_mubench`: Marathi
* `arc_easy_ms_mubench`: Malay
* `arc_easy_my_mubench`: Myanmar
* `arc_easy_nl_mubench`: Dutch
* `arc_easy_no_mubench`: Norwegian
* `arc_easy_pa_mubench`: Punjabi
* `arc_easy_pl_mubench`: Polish
* `arc_easy_pt_mubench`: Portuguese
* `arc_easy_ro_mubench`: Romanian
* `arc_easy_ru_mubench`: Russian
* `arc_easy_sk_mubench`: Slovak
* `arc_easy_sl_mubench`: Slovenian
* `arc_easy_sq_mubench`: Albanian
* `arc_easy_sr_mubench`: Serbian
* `arc_easy_sv_mubench`: Swedish
* `arc_easy_sw_mubench`: Swahili
* `arc_easy_ta_mubench`: Tamil
* `arc_easy_te_mubench`: Telugu
* `arc_easy_th_mubench`: Thai
* `arc_easy_tl_mubench`: Filipino
* `arc_easy_tr_mubench`: Turkish
* `arc_easy_uk_mubench`: Ukrainian
* `arc_easy_ur_mubench`: Urdu
* `arc_easy_uz_mubench`: Uzbek
* `arc_easy_vi_mubench`: Vietnamese
* `arc_easy_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
