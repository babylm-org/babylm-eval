# Xstorycloze

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

* `xstorycloze_mubench`

#### Tasks
* `xstorycloze_af_mubench`: Afrikaans
* `xstorycloze_ar_mubench`: Arabic
* `xstorycloze_az_mubench`: Azerbaijani
* `xstorycloze_bg_mubench`: Bulgarian
* `xstorycloze_bn_mubench`: Bengali
* `xstorycloze_ca_mubench`: Catalan
* `xstorycloze_ceb_mubench`: Cebuano
* `xstorycloze_cs_mubench`: Czech
* `xstorycloze_da_mubench`: Danish
* `xstorycloze_de_mubench`: German
* `xstorycloze_el_mubench`: Greek
* `xstorycloze_en_mubench`: English
* `xstorycloze_es_mubench`: Spanish
* `xstorycloze_et_mubench`: Estonian
* `xstorycloze_fa_mubench`: Persian
* `xstorycloze_fi_mubench`: Finnish
* `xstorycloze_fr_mubench`: French
* `xstorycloze_ga_mubench`: Irish
* `xstorycloze_gu_mubench`: Gujarati
* `xstorycloze_he_mubench`: Hebrew
* `xstorycloze_hi_mubench`: Hindi
* `xstorycloze_hr_mubench`: Croatian
* `xstorycloze_hu_mubench`: Hungarian
* `xstorycloze_id_mubench`: Indonesian
* `xstorycloze_is_mubench`: Icelandic
* `xstorycloze_it_mubench`: Italian
* `xstorycloze_ja_mubench`: Japanese
* `xstorycloze_jv_mubench`: Javanese
* `xstorycloze_kk_mubench`: Kazakh
* `xstorycloze_km_mubench`: Khmer
* `xstorycloze_kn_mubench`: Kannada
* `xstorycloze_ko_mubench`: Korean
* `xstorycloze_lt_mubench`: Lithuanian
* `xstorycloze_lv_mubench`: Latvian
* `xstorycloze_ml_mubench`: Malayalam
* `xstorycloze_mr_mubench`: Marathi
* `xstorycloze_ms_mubench`: Malay
* `xstorycloze_my_mubench`: Myanmar
* `xstorycloze_nl_mubench`: Dutch
* `xstorycloze_no_mubench`: Norwegian
* `xstorycloze_pa_mubench`: Punjabi
* `xstorycloze_pl_mubench`: Polish
* `xstorycloze_pt_mubench`: Portuguese
* `xstorycloze_ro_mubench`: Romanian
* `xstorycloze_ru_mubench`: Russian
* `xstorycloze_sk_mubench`: Slovak
* `xstorycloze_sl_mubench`: Slovenian
* `xstorycloze_sq_mubench`: Albanian
* `xstorycloze_sr_mubench`: Serbian
* `xstorycloze_sv_mubench`: Swedish
* `xstorycloze_sw_mubench`: Swahili
* `xstorycloze_ta_mubench`: Tamil
* `xstorycloze_te_mubench`: Telugu
* `xstorycloze_th_mubench`: Thai
* `xstorycloze_tl_mubench`: Filipino
* `xstorycloze_tr_mubench`: Turkish
* `xstorycloze_uk_mubench`: Ukrainian
* `xstorycloze_ur_mubench`: Urdu
* `xstorycloze_uz_mubench`: Uzbek
* `xstorycloze_vi_mubench`: Vietnamese
* `xstorycloze_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
