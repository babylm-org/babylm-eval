# Hellaswag

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

* `hellaswag_mubench`

#### Tasks
* `hellaswag_af_mubench`: Afrikaans
* `hellaswag_ar_mubench`: Arabic
* `hellaswag_az_mubench`: Azerbaijani
* `hellaswag_bg_mubench`: Bulgarian
* `hellaswag_bn_mubench`: Bengali
* `hellaswag_ca_mubench`: Catalan
* `hellaswag_ceb_mubench`: Cebuano
* `hellaswag_cs_mubench`: Czech
* `hellaswag_da_mubench`: Danish
* `hellaswag_de_mubench`: German
* `hellaswag_el_mubench`: Greek
* `hellaswag_en_mubench`: English
* `hellaswag_es_mubench`: Spanish
* `hellaswag_et_mubench`: Estonian
* `hellaswag_fa_mubench`: Persian
* `hellaswag_fi_mubench`: Finnish
* `hellaswag_fr_mubench`: French
* `hellaswag_ga_mubench`: Irish
* `hellaswag_gu_mubench`: Gujarati
* `hellaswag_he_mubench`: Hebrew
* `hellaswag_hi_mubench`: Hindi
* `hellaswag_hr_mubench`: Croatian
* `hellaswag_hu_mubench`: Hungarian
* `hellaswag_id_mubench`: Indonesian
* `hellaswag_is_mubench`: Icelandic
* `hellaswag_it_mubench`: Italian
* `hellaswag_ja_mubench`: Japanese
* `hellaswag_jv_mubench`: Javanese
* `hellaswag_kk_mubench`: Kazakh
* `hellaswag_km_mubench`: Khmer
* `hellaswag_kn_mubench`: Kannada
* `hellaswag_ko_mubench`: Korean
* `hellaswag_lt_mubench`: Lithuanian
* `hellaswag_lv_mubench`: Latvian
* `hellaswag_ml_mubench`: Malayalam
* `hellaswag_mr_mubench`: Marathi
* `hellaswag_ms_mubench`: Malay
* `hellaswag_my_mubench`: Myanmar
* `hellaswag_nl_mubench`: Dutch
* `hellaswag_no_mubench`: Norwegian
* `hellaswag_pa_mubench`: Punjabi
* `hellaswag_pl_mubench`: Polish
* `hellaswag_pt_mubench`: Portuguese
* `hellaswag_ro_mubench`: Romanian
* `hellaswag_ru_mubench`: Russian
* `hellaswag_sk_mubench`: Slovak
* `hellaswag_sl_mubench`: Slovenian
* `hellaswag_sq_mubench`: Albanian
* `hellaswag_sr_mubench`: Serbian
* `hellaswag_sv_mubench`: Swedish
* `hellaswag_sw_mubench`: Swahili
* `hellaswag_ta_mubench`: Tamil
* `hellaswag_te_mubench`: Telugu
* `hellaswag_th_mubench`: Thai
* `hellaswag_tl_mubench`: Filipino
* `hellaswag_tr_mubench`: Turkish
* `hellaswag_uk_mubench`: Ukrainian
* `hellaswag_ur_mubench`: Urdu
* `hellaswag_uz_mubench`: Uzbek
* `hellaswag_vi_mubench`: Vietnamese
* `hellaswag_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
