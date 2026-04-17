# Arc Challenge

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

* `arc_challenge_mubench`

#### Tasks
* `arc_challenge_af_mubench`: Afrikaans
* `arc_challenge_ar_mubench`: Arabic
* `arc_challenge_az_mubench`: Azerbaijani
* `arc_challenge_bg_mubench`: Bulgarian
* `arc_challenge_bn_mubench`: Bengali
* `arc_challenge_ca_mubench`: Catalan
* `arc_challenge_ceb_mubench`: Cebuano
* `arc_challenge_cs_mubench`: Czech
* `arc_challenge_da_mubench`: Danish
* `arc_challenge_de_mubench`: German
* `arc_challenge_el_mubench`: Greek
* `arc_challenge_en_mubench`: English
* `arc_challenge_es_mubench`: Spanish
* `arc_challenge_et_mubench`: Estonian
* `arc_challenge_fa_mubench`: Persian
* `arc_challenge_fi_mubench`: Finnish
* `arc_challenge_fr_mubench`: French
* `arc_challenge_ga_mubench`: Irish
* `arc_challenge_gu_mubench`: Gujarati
* `arc_challenge_he_mubench`: Hebrew
* `arc_challenge_hi_mubench`: Hindi
* `arc_challenge_hr_mubench`: Croatian
* `arc_challenge_hu_mubench`: Hungarian
* `arc_challenge_id_mubench`: Indonesian
* `arc_challenge_is_mubench`: Icelandic
* `arc_challenge_it_mubench`: Italian
* `arc_challenge_ja_mubench`: Japanese
* `arc_challenge_jv_mubench`: Javanese
* `arc_challenge_kk_mubench`: Kazakh
* `arc_challenge_km_mubench`: Khmer
* `arc_challenge_kn_mubench`: Kannada
* `arc_challenge_ko_mubench`: Korean
* `arc_challenge_lt_mubench`: Lithuanian
* `arc_challenge_lv_mubench`: Latvian
* `arc_challenge_ml_mubench`: Malayalam
* `arc_challenge_mr_mubench`: Marathi
* `arc_challenge_ms_mubench`: Malay
* `arc_challenge_my_mubench`: Myanmar
* `arc_challenge_nl_mubench`: Dutch
* `arc_challenge_no_mubench`: Norwegian
* `arc_challenge_pa_mubench`: Punjabi
* `arc_challenge_pl_mubench`: Polish
* `arc_challenge_pt_mubench`: Portuguese
* `arc_challenge_ro_mubench`: Romanian
* `arc_challenge_ru_mubench`: Russian
* `arc_challenge_sk_mubench`: Slovak
* `arc_challenge_sl_mubench`: Slovenian
* `arc_challenge_sq_mubench`: Albanian
* `arc_challenge_sr_mubench`: Serbian
* `arc_challenge_sv_mubench`: Swedish
* `arc_challenge_sw_mubench`: Swahili
* `arc_challenge_ta_mubench`: Tamil
* `arc_challenge_te_mubench`: Telugu
* `arc_challenge_th_mubench`: Thai
* `arc_challenge_tl_mubench`: Filipino
* `arc_challenge_tr_mubench`: Turkish
* `arc_challenge_uk_mubench`: Ukrainian
* `arc_challenge_ur_mubench`: Urdu
* `arc_challenge_uz_mubench`: Uzbek
* `arc_challenge_vi_mubench`: Vietnamese
* `arc_challenge_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
