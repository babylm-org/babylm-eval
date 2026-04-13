# MultiBLIMP

### Paper

Title: `MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguistic Minimal Pairs`

Abstract: https://arxiv.org/abs/2504.02768

MultiBLiMP is a massively multilingual benchmark of linguistic minimal pairs, covering 101 languages, 6 linguistic phenomena and containing more than 125,000 minimal pairs. This repository contains the code for creating the corpus and the scripts for LLM evaluation.

Homepage: https://github.com/jumelet/multiblimp

### Citation

```
@article{jumelet2025multiblimp,
  title={MultiBLiMP 1.0: A massively multilingual benchmark of linguistic minimal pairs},
  author={Jumelet, Jaap and Weissweiler, Leonie and Bisazza, Arianna},
  journal={arXiv preprint arXiv:2504.02768},
  year={2025}
}
```

### Groups and Tasks

#### Groups

* `multiblimp`

#### Tasks
* `multiblimp_abk`: ABK
* `multiblimp_aln`: ALN
* `multiblimp_amh`: AMH
* `multiblimp_apu`: APU
* `multiblimp_aqz`: AQZ
* `multiblimp_arb`: ARB
* `multiblimp_azz`: AZZ
* `multiblimp_bel`: BEL
* `multiblimp_ben`: BEN
* `multiblimp_bho`: BHO
* `multiblimp_bor`: BOR
* `multiblimp_bre`: BRE
* `multiblimp_bua`: BUA
* `multiblimp_bul`: BUL
* `multiblimp_cat`: CAT
* `multiblimp_ces`: CES
* `multiblimp_chu`: CHU
* `multiblimp_cym`: CYM
* `multiblimp_dan`: DAN
* `multiblimp_deu`: DEU
* `multiblimp_egy`: EGY
* `multiblimp_ell`: ELL
* `multiblimp_eng`: ENG
* `multiblimp_est`: EST
* `multiblimp_eus`: EUS
* `multiblimp_fao`: FAO
* `multiblimp_fas`: FAS
* `multiblimp_fin`: FIN
* `multiblimp_fra`: FRA
* `multiblimp_frm`: FRM
* `multiblimp_fro`: FRO
* `multiblimp_gla`: GLA
* `multiblimp_gle`: GLE
* `multiblimp_glg`: GLG
* `multiblimp_got`: GOT
* `multiblimp_grc`: GRC
* `multiblimp_guj`: GUJ
* `multiblimp_hbo`: HBO
* `multiblimp_hbs`: HBS
* `multiblimp_heb`: HEB
* `multiblimp_hin`: HIN
* `multiblimp_hit`: HIT
* `multiblimp_hsb`: HSB
* `multiblimp_hun`: HUN
* `multiblimp_hye`: HYE
* `multiblimp_hyw`: HYW
* `multiblimp_isl`: ISL
* `multiblimp_ita`: ITA
* `multiblimp_kat`: KAT
* `multiblimp_kaz`: KAZ
* `multiblimp_kir`: KIR
* `multiblimp_kmr`: KMR
* `multiblimp_koi`: KOI
* `multiblimp_kpv`: KPV
* `multiblimp_krl`: KRL
* `multiblimp_kxh`: KXH
* `multiblimp_lat`: LAT
* `multiblimp_lav`: LAV
* `multiblimp_lij`: LIJ
* `multiblimp_lit`: LIT
* `multiblimp_mar`: MAR
* `multiblimp_mdf`: MDF
* `multiblimp_mkd`: MKD
* `multiblimp_myv`: MYV
* `multiblimp_nds`: NDS
* `multiblimp_nhi`: NHI
* `multiblimp_nld`: NLD
* `multiblimp_olo`: OLO
* `multiblimp_orv`: ORV
* `multiblimp_ota`: OTA
* `multiblimp_pcm`: PCM
* `multiblimp_pol`: POL
* `multiblimp_por`: POR
* `multiblimp_quc`: QUC
* `multiblimp_ron`: RON
* `multiblimp_rus`: RUS
* `multiblimp_sah`: SAH
* `multiblimp_san`: SAN
* `multiblimp_slk`: SLK
* `multiblimp_slv`: SLV
* `multiblimp_sme`: SME
* `multiblimp_sms`: SMS
* `multiblimp_spa`: SPA
* `multiblimp_sqi`: SQI
* `multiblimp_swe`: SWE
* `multiblimp_tam`: TAM
* `multiblimp_tpn`: TPN
* `multiblimp_ttc`: TTC
* `multiblimp_tur`: TUR
* `multiblimp_uig`: UIG
* `multiblimp_ukr`: UKR
* `multiblimp_urb`: URB
* `multiblimp_urd`: URD
* `multiblimp_uzb`: UZB
* `multiblimp_vep`: VEP
* `multiblimp_wbp`: WBP
* `multiblimp_wol`: WOL
* `multiblimp_xcl`: XCL
* `multiblimp_xnr`: XNR
* `multiblimp_xpg`: XPG
* `multiblimp_yrl`: YRL


### Checklist

For adding novel benchmarks/datasets to the library:
* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:
* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
