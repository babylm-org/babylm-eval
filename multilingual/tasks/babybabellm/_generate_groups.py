"""
Prototype script to generate YAML group files
"""

import os

languages = [
    "Afrikaans",
    "Arabic",
    "Basque",
    "Bulgarian",
    "Chinese",
    "Croatian",
    "Danish",
    "Dutch",
    "Estonian",
    "French",
    "German",
    "Greek",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "isiXhosa",
    "isiZulu",
    "Italian",
    "Japanese",
    "Kannada",
    "Korean",
    "Nepali",
    "Persian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Sepedi (Northern Sotho)",
    "Serbian",
    "Sesotho (Southern Sotho)",
    "Spanish",
    "Swedish",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Welsh",
]

languages = ["Afrikaans", "Ukrainian"]


# Map language names to codes used in tasks
lang_code_map = {
    "Afrikaans": "af",
    "Arabic": "ar",
    "Basque": "eu",
    "Bulgarian": "bg",
    "Chinese": "zh",
    "Croatian": "hr",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "isiXhosa": "xh",
    "isiZulu": "zu",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Nepali": "ne",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Sepedi (Northern Sotho)": "nso",
    "Serbian": "sr",
    "Sesotho (Southern Sotho)": "st",
    "Spanish": "es",
    "Swedish": "sv",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Welsh": "cy",
}

lang_code_belebele_map = {
    v: k
    for k, v in {
        "acm_Arab": "Mesopotamian Arabic",
        "afr_Latn": "Afrikaans",
        "als_Latn": "Tosk Albanian",
        "amh_Ethi": "Amharic",
        "apc_Arab": "North Levantine Arabic",
        "arb_Arab": "Modern Standard Arabic",
        "arb_Latn": "Modern Standard Arabic (Romanized)",
        "ars_Arab": "Najdi Arabic",
        "ary_arab": "Moroccan Arabic",
        "arz_Arab": "Egyptian Arabic",
        "asm_Beng": "Assamese",
        "azj_Latn": "North Azerbaijani",
        "bam_Latn": "Bambara",
        "ben_Beng": "Bengali",
        "ben_Latn": "Bengali (Romanized)",
        "bod_Tibt": "Standard Tibetan",
        "bul_Cyrl": "Bulgarian",
        "cat_Latn": "Catalan",
        "ceb_Latn": "Cebuano",
        "ces_Latn": "Czech",
        "ckb_Arab": "Central Kurdish",
        "dan_Latn": "Danish",
        "deu_Latn": "German",
        "ell_Grek": "Greek",
        "eng_Latn": "English",
        "est_Latn": "Estonian",
        "eus_Latn": "Basque",
        "fin_Latn": "Finnish",
        "fra_Latn": "French",
        "fuv_Latn": "Nigerian Fulfulde",
        "gaz_Latn": "West Central Oromo",
        "grn_Latn": "Guarani",
        "guj_Gujr": "Gujarati",
        "hat_Latn": "Haitian Creole",
        "hau_Latn": "Hausa",
        "heb_Hebr": "Hebrew",
        "hin_Deva": "Hindi",
        "hin_Latn": "Hindi (Romanized)",
        "hrv_Latn": "Croatian",
        "hun_Latn": "Hungarian",
        "hye_Armn": "Armenian",
        "ibo_Latn": "Igbo",
        "ilo_Latn": "Ilocano",
        "ind_Latn": "Indonesian",
        "isl_Latn": "Icelandic",
        "ita_Latn": "Italian",
        "jav_Latn": "Javanese",
        "jpn_Jpan": "Japanese",
        "kac_Latn": "Jingpho",
        "kan_Knda": "Kannada",
        "kat_Geor": "Georgian",
        "kaz_Cyrl": "Kazakh",
        "kea_Latn": "Kabuverdianu",
        "khk_Cyrl": "Halh Mongolian",
        "khm_Khmr": "Khmer",
        "kin_Latn": "Kinyarwanda",
        "kir_Cyrl": "Kyrgyz",
        "kor_Hang": "Korean",
        "lao_Laoo": "Lao",
        "lin_Latn": "Lingala",
        "lit_Latn": "Lithuanian",
        "lug_Latn": "Ganda",
        "luo_Latn": "Luo",
        "lvs_Latn": "Standard Latvian",
        "mal_Mlym": "Malayalam",
        "mar_Deva": "Marathi",
        "mkd_Cyrl": "Macedonian",
        "mlt_Latn": "Maltese",
        "mri_Latn": "Maori",
        "mya_Mymr": "Burmese",
        "nld_Latn": "Dutch",
        "nob_Latn": "Norwegian Bokmål",
        "npi_Deva": "Nepali",
        "npi_Latn": "Nepali (Romanized)",
        "nso_Latn": "Northern Sotho",
        "nya_Latn": "Nyanja",
        "ory_Orya": "Odia",
        "pan_Guru": "Eastern Panjabi",
        "pbt_Arab": "Southern Pashto",
        "pes_Arab": "Western Persian",
        "plt_Latn": "Plateau Malagasy",
        "pol_Latn": "Polish",
        "por_Latn": "Portuguese",
        "ron_Latn": "Romanian",
        "rus_Cyrl": "Russian",
        "shn_Mymr": "Shan",
        "sin_Latn": "Sinhala (Romanized)",
        "sin_Sinh": "Sinhala",
        "slk_Latn": "Slovak",
        "slv_Latn": "Slovenian",
        "sna_Latn": "Shona",
        "snd_Arab": "Sindhi",
        "som_Latn": "Somali",
        "sot_Latn": "Southern Sotho",
        "spa_Latn": "Spanish",
        "srp_Cyrl": "Serbian",
        "ssw_Latn": "Swati",
        "sun_Latn": "Sundanese",
        "swe_Latn": "Swedish",
        "swh_Latn": "Swahili",
        "tam_Taml": "Tamil",
        "tel_Telu": "Telugu",
        "tgk_Cyrl": "Tajik",
        "tgl_Latn": "Tagalog",
        "tha_Thai": "Thai",
        "tir_Ethi": "Tigrinya",
        "tsn_Latn": "Tswana",
        "tso_Latn": "Tsonga",
        "tur_Latn": "Turkish",
        "ukr_Cyrl": "Ukrainian",
        "urd_Arab": "Urdu",
        "urd_Latn": "Urdu (Romanized)",
        "uzn_Latn": "Northern Uzbek",
        "vie_Latn": "Vietnamese",
        "war_Latn": "Waray",
        "wol_Latn": "Wolof",
        "xho_Latn": "Xhosa",
        "yor_Latn": "Yoruba",
        "zho_Hans": "Chinese (Simplified)",
        "zho_Hant": "Chinese (Traditional)",
        "zsm_Latn": "Standard Malay",
        "zul_Latn": "Zulu",
    }.items()
}

for lang in languages:
    code = lang_code_map[lang]
    group_name = f"babybabellm_{code}"
    categories = {
        "multiblimp": {
            "default": f"multiblimp_{code}",
            "Afrikaans": False,
            "Chinese": False,  # TODO: add custom
            "Indonesian": False,  # TODO: add custom
            "isiXhosa": False,
            "isiZulu": False,
            "Japanese": False,  # TODO: add custom
            "Kannada": False,
            "Korean": False,
            "Sepedi (Northern Sotho)": False,
            "Sesotho (Southern Sotho)": False,
        },
        "ner": {
            # "default": "# - TODO: ner",
        },
        "pos": {
            #  "default": "# - TODO: pos",
        },
        "xnli": {},
        "winogrande": {
            "default": f"winogrande_{code}_mubench",
        },
        "xstorycloze": {
            "default": f"xstorycloze_{code}_mubench",
        },
        "comps": {
            "default": f"comps_{code}",
            "Afrikaans": False,
        },
        "belebele": {
            "default": f"belebele_{lang_code_belebele_map[lang]}",
        },
        "global_mmlu_full": {
            "default": f"global_mmlu_full_{code}",
            "Afrikaans": False,
        },
        "include_base_44": {
            "default": f"include_base_44_{lang.lower().replace(' ', '').replace('(', '').replace(')', '')}",
            "Afrikaans": False,
        },
        "lang_specific": {},
    }
    tasks = []
    for category in categories:
        contains_category_lang = categories[category].get(lang, None)
        if contains_category_lang is not None:
            if contains_category_lang is False:
                continue
            else:
                tasks.append(contains_category_lang)
        elif (
            categories[category].get("default", False) is not False
        ):  # If the default task exists
            tasks.append(categories[category]["default"])
        else:
            pass
    yaml_content = f"""group: {group_name}
task:
  - {"\n  - ".join(tasks)}
metadata:
  version: 1.0
"""
    filename = f"{group_name}.yaml"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(yaml_content)
