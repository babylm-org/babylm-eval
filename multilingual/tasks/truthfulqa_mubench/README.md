# Truthfulqa

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

* `truthfulqa_mubench`

#### Tasks
* `truthfulqa_af_mubench`: Afrikaans
* `truthfulqa_ar_mubench`: Arabic
* `truthfulqa_az_mubench`: Azerbaijani
* `truthfulqa_bg_mubench`: Bulgarian
* `truthfulqa_bn_mubench`: Bengali
* `truthfulqa_ca_mubench`: Catalan
* `truthfulqa_ceb_mubench`: Cebuano
* `truthfulqa_cs_mubench`: Czech
* `truthfulqa_da_mubench`: Danish
* `truthfulqa_de_mubench`: German
* `truthfulqa_el_mubench`: Greek
* `truthfulqa_en_mubench`: English
* `truthfulqa_es_mubench`: Spanish
* `truthfulqa_et_mubench`: Estonian
* `truthfulqa_fa_mubench`: Persian
* `truthfulqa_fi_mubench`: Finnish
* `truthfulqa_fr_mubench`: French
* `truthfulqa_ga_mubench`: Irish
* `truthfulqa_gu_mubench`: Gujarati
* `truthfulqa_he_mubench`: Hebrew
* `truthfulqa_hi_mubench`: Hindi
* `truthfulqa_hr_mubench`: Croatian
* `truthfulqa_hu_mubench`: Hungarian
* `truthfulqa_id_mubench`: Indonesian
* `truthfulqa_is_mubench`: Icelandic
* `truthfulqa_it_mubench`: Italian
* `truthfulqa_ja_mubench`: Japanese
* `truthfulqa_jv_mubench`: Javanese
* `truthfulqa_kk_mubench`: Kazakh
* `truthfulqa_km_mubench`: Khmer
* `truthfulqa_kn_mubench`: Kannada
* `truthfulqa_ko_mubench`: Korean
* `truthfulqa_lt_mubench`: Lithuanian
* `truthfulqa_lv_mubench`: Latvian
* `truthfulqa_ml_mubench`: Malayalam
* `truthfulqa_mr_mubench`: Marathi
* `truthfulqa_ms_mubench`: Malay
* `truthfulqa_my_mubench`: Myanmar
* `truthfulqa_nl_mubench`: Dutch
* `truthfulqa_no_mubench`: Norwegian
* `truthfulqa_pa_mubench`: Punjabi
* `truthfulqa_pl_mubench`: Polish
* `truthfulqa_pt_mubench`: Portuguese
* `truthfulqa_ro_mubench`: Romanian
* `truthfulqa_ru_mubench`: Russian
* `truthfulqa_sk_mubench`: Slovak
* `truthfulqa_sl_mubench`: Slovenian
* `truthfulqa_sq_mubench`: Albanian
* `truthfulqa_sr_mubench`: Serbian
* `truthfulqa_sv_mubench`: Swedish
* `truthfulqa_sw_mubench`: Swahili
* `truthfulqa_ta_mubench`: Tamil
* `truthfulqa_te_mubench`: Telugu
* `truthfulqa_th_mubench`: Thai
* `truthfulqa_tl_mubench`: Filipino
* `truthfulqa_tr_mubench`: Turkish
* `truthfulqa_uk_mubench`: Ukrainian
* `truthfulqa_ur_mubench`: Urdu
* `truthfulqa_uz_mubench`: Uzbek
* `truthfulqa_vi_mubench`: Vietnamese
* `truthfulqa_zh_mubench`: Chinese



### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
