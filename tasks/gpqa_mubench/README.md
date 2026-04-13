# Gpqa

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

* `gpqa_mubench`

#### Tasks
* `gpqa_af_mubench`: Afrikaans
* `gpqa_ar_mubench`: Arabic
* `gpqa_az_mubench`: Azerbaijani
* `gpqa_bg_mubench`: Bulgarian
* `gpqa_bn_mubench`: Bengali
* `gpqa_ca_mubench`: Catalan
* `gpqa_ceb_mubench`: Cebuano
* `gpqa_cs_mubench`: Czech
* `gpqa_da_mubench`: Danish
* `gpqa_de_mubench`: German
* `gpqa_el_mubench`: Greek
* `gpqa_en_mubench`: English
* `gpqa_es_mubench`: Spanish
* `gpqa_et_mubench`: Estonian
* `gpqa_fa_mubench`: Persian
* `gpqa_fi_mubench`: Finnish
* `gpqa_fr_mubench`: French
* `gpqa_ga_mubench`: Irish
* `gpqa_gu_mubench`: Gujarati
* `gpqa_he_mubench`: Hebrew
* `gpqa_hi_mubench`: Hindi
* `gpqa_hr_mubench`: Croatian
* `gpqa_hu_mubench`: Hungarian
* `gpqa_id_mubench`: Indonesian
* `gpqa_is_mubench`: Icelandic
* `gpqa_it_mubench`: Italian
* `gpqa_ja_mubench`: Japanese
* `gpqa_jv_mubench`: Javanese
* `gpqa_kk_mubench`: Kazakh
* `gpqa_km_mubench`: Khmer
* `gpqa_kn_mubench`: Kannada
* `gpqa_ko_mubench`: Korean
* `gpqa_lt_mubench`: Lithuanian
* `gpqa_lv_mubench`: Latvian
* `gpqa_ml_mubench`: Malayalam
* `gpqa_mr_mubench`: Marathi
* `gpqa_ms_mubench`: Malay
* `gpqa_my_mubench`: Myanmar
* `gpqa_nl_mubench`: Dutch
* `gpqa_no_mubench`: Norwegian
* `gpqa_pa_mubench`: Punjabi
* `gpqa_pl_mubench`: Polish
* `gpqa_pt_mubench`: Portuguese
* `gpqa_ro_mubench`: Romanian
* `gpqa_ru_mubench`: Russian
* `gpqa_sk_mubench`: Slovak
* `gpqa_sl_mubench`: Slovenian
* `gpqa_sq_mubench`: Albanian
* `gpqa_sr_mubench`: Serbian
* `gpqa_sv_mubench`: Swedish
* `gpqa_sw_mubench`: Swahili
* `gpqa_ta_mubench`: Tamil
* `gpqa_te_mubench`: Telugu
* `gpqa_th_mubench`: Thai
* `gpqa_tl_mubench`: Filipino
* `gpqa_tr_mubench`: Turkish
* `gpqa_uk_mubench`: Ukrainian
* `gpqa_ur_mubench`: Urdu
* `gpqa_uz_mubench`: Uzbek
* `gpqa_vi_mubench`: Vietnamese
* `gpqa_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
