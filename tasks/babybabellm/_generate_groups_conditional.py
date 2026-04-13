import os
from pathlib import Path

# Map language names to codes used in tasks
lang_code_map = {
    "Acehnese": "ace",
    "Afrikaans": "af",
    "Arabic": "ar",
    "Balinese": "ban",
    "Basque": "eu",
    "Buginese": "bug",
    "Bulgarian": "bg",
    "Cantonese": "yue",  # Using yue for Cantonese (ISO 639-3)
    "Chinese": "zh",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Hebrew": "he",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Korean": "ko",
    "Makassarese": "mak",
    "Minangkabau": "min",
    "Northern Sotho": "nso",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Southern Sotho": "st",
    "Spanish": "es",
    "Sundanese": "su",
    "Swedish": "sv",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Zulu": "zu",
}

# Map MuBench 2-letter codes to African task 3-letter codes for African languages
mubench_to_african_map = {
    "xh": "xho",  # isiXhosa
    "zu": "zul",  # isiZulu  
    "st": "sot",  # Sesotho (Southern Sotho)
}

# Map MuBench 2-letter codes to Afrobench language codes for uhura tasks
mubench_to_afrobench_map = {
    "zu": "zu",   # isiZulu
    "nso": "nso", # Sepedi (Northern Sotho) - note: this is already 3-letter in MuBench
}

# Map 2-letter codes to 3-letter ISO 639-3 codes for group names
two_to_three_letter_map = {
    "ace": "ace",  # Acehnese (already 3-letter)
    "af": "afr",   # Afrikaans
    "ar": "ara",    # Arabic
    "ban": "ban",  # Balinese (already 3-letter)
    "eu": "eus",   # Basque
    "bug": "bug",  # Buginese (already 3-letter)
    "bg": "bul",   # Bulgarian
    "yue": "yue",  # Cantonese (already 3-letter)
    "zh": "zho",   # Chinese
    "hr": "hrv",   # Croatian
    "cs": "ces",   # Czech
    "da": "dan",   # Danish
    "nl": "nld",   # Dutch
    "en": "eng",   # English
    "et": "est",   # Estonian
    "fr": "fra",   # French
    "de": "deu",   # German
    "el": "ell",   # Greek
    "he": "heb",   # Hebrew
    "hu": "hun",   # Hungarian
    "is": "isl",   # Icelandic
    "id": "ind",   # Indonesian
    "it": "ita",   # Italian
    "ja": "jpn",   # Japanese
    "jv": "jav",   # Javanese
    "ko": "kor",   # Korean
    "mak": "mak",  # Makassarese (already 3-letter)
    "min": "min",  # Minangkabau (already 3-letter)
    "nso": "nso",  # Northern Sotho (already 3-letter)
    "no": "nor",    # Norwegian
    "fa": "fas",   # Persian
    "pl": "pol",   # Polish
    "pt": "por",   # Portuguese
    "ro": "ron",   # Romanian
    "ru": "rus",   # Russian
    "sr": "srp",   # Serbian
    "st": "sot",   # Southern Sotho
    "es": "spa",   # Spanish
    "su": "sun",   # Sundanese
    "sv": "swe",   # Swedish
    "tr": "tur",   # Turkish
    "uk": "ukr",   # Ukrainian
    "cy": "cym",   # Welsh
    "xh": "xho",   # Xhosa
    "zu": "zul",   # Zulu
}

# Direct map from 2-letter codes to Belebele/SIB-200 language_Script codes
two_letter_to_belebele_map = {
    "ace": "ace_Latn",    # Acehnese
    "af": "afr_Latn",     # Afrikaans
    "ar": "arb_Arab",     # Arabic -> Modern Standard Arabic
    "ban": "ban_Latn",    # Balinese
    "eu": "eus_Latn",     # Basque
    "bug": "bug_Latn",    # Buginese
    "bg": "bul_Cyrl",     # Bulgarian
    "yue": "yue_Hant",    # Cantonese -> Traditional Chinese script
    "zh": "zho_Hans",     # Chinese -> Simplified Chinese
    "hr": "hrv_Latn",     # Croatian
    "cs": "ces_Latn",     # Czech
    "da": "dan_Latn",     # Danish
    "nl": "nld_Latn",     # Dutch
    "en": "eng_Latn",     # English
    "et": "est_Latn",     # Estonian
    "fr": "fra_Latn",     # French
    "de": "deu_Latn",     # German
    "el": "ell_Grek",     # Greek
    "he": "heb_Hebr",     # Hebrew
    "hu": "hun_Latn",     # Hungarian
    "is": "isl_Latn",     # Icelandic
    "id": "ind_Latn",     # Indonesian
    "it": "ita_Latn",     # Italian
    "ja": "jpn_Jpan",     # Japanese
    "jv": "jav_Latn",     # Javanese
    "ko": "kor_Hang",     # Korean
    "mak": "mak_Latn",    # Makassarese
    "min": "min_Latn",    # Minangkabau
    "nso": "nso_Latn",    # Northern Sotho
    "no": "nob_Latn",     # Norwegian Bokmål
    "fa": "pes_Arab",     # Persian -> Western Persian
    "pl": "pol_Latn",     # Polish
    "pt": "por_Latn",     # Portuguese
    "ro": "ron_Latn",     # Romanian
    "ru": "rus_Cyrl",     # Russian
    "sr": "srp_Cyrl",     # Serbian
    "st": "sot_Latn",     # Southern Sotho
    "es": "spa_Latn",     # Spanish
    "su": "sun_Latn",     # Sundanese
    "sv": "swe_Latn",     # Swedish
    "tr": "tur_Latn",     # Turkish
    "uk": "ukr_Cyrl",     # Ukrainian
    "xh": "xho_Latn",     # Xhosa
    "zu": "zul_Latn",     # Zulu
    # Note: cy (Welsh) may not have Belebele/SIB-200 equivalents
}

def check_task_exists(task_name, base_path="../", lang_name=None):
    """
    Check if a task configuration file exists.
    This function looks for YAML files in the task directories with flexible matching.
    """
    # Check both local tasks directory and lm_eval package tasks
    task_paths = [
        Path(base_path),
        Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks")
    ]
    
    for task_path in task_paths:
        if not task_path.exists():
            continue
        
        # Hellaswag special case - check only in base path, not lm_eval
        if task_name.endswith("_mubench") and task_name.startswith("hellaswag_"):
            if task_path == Path(base_path):
                # Extract language code from task name (e.g., hellaswag_tr_mubench -> tr)
                lang_code = task_name.split('_')[1]
                # Check for language-specific hellaswag file
                hellaswag_file = task_path / "hellaswag_mubench" / f"default_{lang_code}.yaml"
                if hellaswag_file.exists():
                    return True
            continue  # Don't check lm_eval for hellaswag
        
        # African tasks special case - check only in lm_eval, not base path
        if task_name.startswith("afrixnli_") or task_name.startswith("afrimmlu_"):
            if task_path != Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks"):
                continue  # Only check lm_eval for African tasks
            
            # African tasks - specific patterns for lm_eval only
            possible_paths = []
            
            if task_name.startswith("afrixnli_"):
                # Extract the MuBench language code and convert to African task code
                african_lang_code = task_name.split('_')[1]
                
                if african_lang_code:
                    # Use the 3-letter African code for the actual file
                    african_task_name = f"afrixnli_{african_lang_code}"
                    afrixnli_paths = [
                        task_path / "afrixnli" / "direct" / "prompt_1" / f"{african_task_name}.yaml",
                    ]
                    possible_paths.extend(afrixnli_paths)
                
            if task_name.startswith("afrimmlu_direct_"):
                # Extract the MuBench language code and convert to African task code  
                african_lang_code = task_name.split('_')[2]
                
                if african_lang_code:
                    # Use the 3-letter African code for the actual file
                    african_task_name = f"afrimmlu_direct_{african_lang_code}"
                    afrimmlu_paths = [
                        task_path / "afrimmlu" / "direct" / "prompt_1" / f"{african_task_name}.yaml",
                    ]
                    possible_paths.extend(afrimmlu_paths)
            
            # Check African task paths
            for path in possible_paths:
                if path.exists():
                    return True
            continue  # Don't use general patterns for African tasks

        # Afrobench tasks special case - check only in lm_eval, not base path
        if task_name.startswith("uhura-arc-easy_") or task_name.startswith("sib_"):
            if task_path != Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks"):
                continue  # Only check lm_eval for afrobench tasks
            
            if task_name.startswith("uhura-arc-easy_"):
                # Extract the MuBench language code and convert to afrobench code
                afrobench_lang_code = task_name.split('_')[1]
                
                if afrobench_lang_code:
                    # Use prompt_1 for uhura arc easy
                    uhura_task_name = f"uhura-arc-easy_{afrobench_lang_code}"
                    uhura_path = task_path / "afrobench" / "uhura-arc-easy" / "prompt_1" / f"{uhura_task_name}.yaml"
                    if uhura_path.exists():
                        return True
            
            if task_name.startswith("sib_") and task_name.endswith("_prompt_1"):
                # Extract the language code (e.g., sib_nso_prompt_1 -> nso, sib_sot_prompt_1 -> sot)
                sib_lang_code = task_name.split('_')[1]
                
                if sib_lang_code:
                    # Check for SIB tasks in afrobench directory
                    sib_path = task_path / "afrobench" / "sib" / "prompt_1" / f"sib_{sib_lang_code}.yaml"
                    if sib_path.exists():
                        return True
            
            continue  # Don't use general patterns for afrobench tasks
        
        # Try multiple possible file patterns and locations
        possible_paths = []
        
        # Extract base task name and language code
        if "_" in task_name:
            task_parts = task_name.split("_")
            base_task = task_parts[0]
            lang_code = "_".join(task_parts[1:])  # Handle multi-part language codes
        else:
            base_task = task_name
            lang_code = ""
        
        # For MuBench tasks, check if the task directory and default language files exist
        if "_mubench" in task_name:
            # Handle multi-word task names like arc_easy, truthfulqa, etc.
            if task_name.endswith("_mubench"):
                # Extract the language code (second to last part)
                mubench_lang_code = task_parts[-2]
                # Base task is everything except language and _mubench
                mubench_base_task = "_".join(task_parts[:-2])
                task_dir = task_path / f"{mubench_base_task}_mubench"
                config_file = task_dir / f"default_{mubench_lang_code}.yaml"
                possible_paths.append(config_file)
        
        # Standard patterns - try various combinations
        possible_paths.extend([
            # Direct task file
            task_path / f"{task_name}.yaml",
            
            # Task in its own directory
            task_path / task_name / f"{task_name}.yaml",
            task_path / task_name / "default.yaml",
            task_path / task_name / f"default_{lang_code}.yaml",
            
            # Task in base task directory
            task_path / base_task / f"{task_name}.yaml",
            task_path / base_task / f"default_{lang_code}.yaml",
            task_path / base_task / f"{lang_code}.yaml",
            
            # Special directory mappings
            task_path / "xcomps" / f"{task_name}.yaml",  # xcomps tasks
            task_path / "belebele" / f"{task_name}.yaml",
            task_path / "global_mmlu" / f"{task_name}.yaml",
            task_path / "multiblimp" / f"{task_name}.yaml",
            task_path / "sib200" / f"{task_name}.yaml",  # sib200 tasks
            task_path / "nusaparagraph_topic" / f"{task_name}.yaml",  # nusaparagraph tasks
            task_path / "zhoblimp" / f"_{task_name}.yaml",  # zhoblimp group task
            task_path / "jblimp" / f"{task_name}.yaml",  # jblimp task
            task_path / "lindsea_blimp" / f"_{task_name}.yaml",  # lindsea blimp group task
            task_path / "clams" / f"{task_name}.yaml",  # clams tasks
            task_path / "xnli" / f"{task_name}.yaml",
            task_path / "xcopa" / f"{task_name}.yaml",
            task_path / "bl2mp" / f"{task_name}.yaml",  # bl2mp tasks
            task_path / "copa" / f"{task_name}.yaml",  # copa tasks
            task_path / "blimp" / f"_{task_name}.yaml",  # blimp tasks
            
            # Global MMLU specific patterns with underscores
            task_path / "global_mmlu" / "full" / lang_code / f"_{task_name}.yaml",
            task_path / "global_mmlu" / "default" / lang_code / f"_{task_name}.yaml",
            
            # Include base 44 specific patterns
            task_path / "include" / "default" / (lang_name.title() if lang_name else "") / f"_{task_name}.yaml",
            task_path / "include" / "default" / (lang_name.lower() if lang_name else "") / f"_{task_name}.yaml",
            
            # Alternative naming patterns
            task_path / base_task / f"{base_task}_{lang_code}.yaml",
            task_path / base_task / f"{base_task}.yaml",
        ])
        
        # Global MMLU is a special case - check if language directory exists first
        if task_name.startswith("global_mmlu_full_"):
            lang_code = task_name.split('_')[-1]
            # Only check lm_eval path for global_mmlu
            if task_path == Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks"):
                # Check if the language directory exists in global_mmlu
                lang_dir = task_path / "global_mmlu" / "full" / lang_code
                if lang_dir.exists():
                    # Look for any global_mmlu file for this language (since they have multiple subjects)
                    global_mmlu_files = list(lang_dir.glob(f"global_mmlu_full_{lang_code}_*.yaml"))
                    if global_mmlu_files:
                        # If we find any global_mmlu files for this language, consider the task available
                        return True
            continue  # Don't check base path for global_mmlu, only lm_eval
        
        # Basque-specific tasks - check basque_bench and truthfulqa-multi directories in lm_eval
        if task_name in ["xcopa_eu", "xstorycloze_eu", "truthfulqa-multi_mc1_eu"] and task_path == Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks"):
            # Check basque_bench directory
            basque_bench_path = task_path / "basque_bench" / f"{task_name}.yaml"
            if basque_bench_path.exists():
                return True
            # Check truthfulqa-multi directory
            truthfulqa_multi_path = task_path / "truthfulqa-multi" / f"{task_name}.yaml"
            if truthfulqa_multi_path.exists():
                return True
        
        # COPA task special cases - check specific directories in lm_eval
        if task_name in ["copa", "copa_es", "copa_ar"] and task_path == Path("/ikerlariak/jetxaniz007/lm-evaluation-harness/lm_eval/tasks"):
            if task_name == "copa":
                copa_path = task_path / "super_glue" / "copa" / "default.yaml"
                if copa_path.exists():
                    return True
            elif task_name == "copa_es":
                copa_es_path = task_path / "spanish_bench" / "copa_es.yaml"
                if copa_es_path.exists():
                    return True
            elif task_name == "copa_ar":
                copa_ar_path = task_path / "alghafa" / "copa_ar" / "copa_ar.yaml"
                if copa_ar_path.exists():
                    return True
            continue  # Don't use general patterns for copa tasks
        
        # Include base 44 is a special case - check for proper directory structure
        if task_name.startswith("include_base_44_") and lang_name:
            include_paths = [
                task_path / "include" / "default" / lang_name.title() / f"_{task_name}.yaml",
                task_path / "include" / "default" / lang_name.lower() / f"_{task_name}.yaml",
                task_path / "include" / "default" / lang_name / f"_{task_name}.yaml",
            ]
            possible_paths.extend(include_paths)
        
        # Also try recursive search in common task directories (excluding African task dirs)
        common_dirs = ["xcomps", "belebele", "global_mmlu", "multiblimp", "sib200", "nusaparagraph_topic", "zhoblimp", "jblimp", "lindsea_blimp", "clams", "xnli", "xcopa", "bl2mp", "copa", "blimp"]
        for dir_name in common_dirs:
            dir_path = task_path / dir_name
            if dir_path.exists():
                # Look for any YAML file that might match our task
                possible_paths.extend([
                    dir_path / f"{task_name}.yaml",
                    dir_path / f"default_{lang_code}.yaml",
                    dir_path / base_task / f"{task_name}.yaml",
                    dir_path / base_task / f"default_{lang_code}.yaml",
                ])
        
        # Check if any of the possible paths exist
        for path in possible_paths:
            if path.exists():
                return True
    
    return False

def generate_group_for_language(lang, code, base_path="../"):
    """Generate a group YAML for a specific language, only including available tasks."""
    
    # Get the proper language codes using direct mappings
    belebele_code = two_letter_to_belebele_map.get(code)
    african_code = mubench_to_african_map.get(code, code)
    afrobench_code = mubench_to_afrobench_map.get(code, code)
    three_letter_code = two_to_three_letter_map.get(code, code)
    
    # Define potential tasks for this language
    potential_tasks = [
        f"multiblimp_{three_letter_code}",  # Updated to use 3-letter codes
        f"winogrande_{code}_mubench",
        f"xstorycloze_{code}_mubench", 
        f"bmlama_{code}_mubench",
        f"hellaswag_{code}_mubench",
        # f"snli_{code}_mubench",
        f"multinli_{code}_mubench",
        f"arc_easy_{code}_mubench",
        f"truthfulqa_{code}_mubench",
        f"xnli_{code}",
        f"xcopa_{code}",
        f"xcomps_{code}",  # Updated from comps_ to xcomps_
        f"global_mmlu_full_{code}",
        f"afrixnli_{african_code}_prompt_1",
        f"afrimmlu_direct_{african_code}_prompt_1",
        f"uhura-arc-easy_{afrobench_code}_prompt_1",
        f"include_base_44_{lang.lower().replace(' ', '').replace('(', '').replace(')', '')}",
    ]
    
    # Special case for Basque - add additional tasks
    if code == "eu":
        potential_tasks.extend([
            "xstorycloze_eu",  # Add non-mubench xstorycloze for Basque
            "truthfulqa-multi_mc1_eu",  # Add truthfulqa-multi for Basque
            "bl2mp",  # Add BL2MP for Basque
        ])
    
    # Special case for English - add additional tasks
    if code == "en":
        potential_tasks.extend([
            "copa",  # Add COPA for English
            "blimp",  # Add BLIMP for English
        ])
    
    # Special case for Spanish - add COPA
    if code == "es":
        potential_tasks.extend([
            "copa_es",  # Add Spanish COPA
        ])
    
    # Special case for Arabic - add COPA
    if code == "ar":
        potential_tasks.extend([
            "copa_ar",  # Add Arabic COPA
        ])

    # Special case for Italian and Estonian (remove xnli and xcomps)
    if code in ["it", "et", "id"]:
        potential_tasks = [task for task in potential_tasks if task not in [f"xnli_{code}", f"xcomps_{code}"]]

    # Add Belebele task if available for this language
    if belebele_code:
        potential_tasks.append(f"belebele_{belebele_code}")
    
    # Add SIB-200 task if available for this language  
    # SIB-200 uses the same language_Script format as Belebele, except for some African languages
    if belebele_code:
        # Special cases for African languages that use different SIB naming
        if code == "nso":  # Northern Sotho
            potential_tasks.append("sib_nso_prompt_1")
        elif code == "st":  # Southern Sotho  
            potential_tasks.append("sib_sot_prompt_1")
        else:
            # Standard SIB-200 naming
            potential_tasks.append(f"sib200_{belebele_code}")
    
    # Add NusaParagraph topic task if available for Indonesian languages
    nusaparagraph_langs = {
        "jv": "jav",    # Javanese -> jav
        "su": "sun",    # Sundanese -> sun  
        "mak": "mak",   # Makassarese -> mak
        "min": "min"    # Minangkabau -> min
    }
    if code in nusaparagraph_langs:
        nusa_code = nusaparagraph_langs[code]
        potential_tasks.append(f"nusaparagraph_topic_{nusa_code}")
    
    # Add ZhoBLIMP group task for Chinese
    if code == "zh":
        potential_tasks.append("zhoblimp")
    
    # Add JBLiMP task for Japanese
    if code == "ja":
        potential_tasks.append("jblimp")
    
    # Add Indonesian BLIMP tasks for Indonesian
    if code == "id":
        potential_tasks.extend([
            "lindsea_blimp",
        ])
    
    # Add CLAMS tasks for supported languages
    clams_languages = ["en", "fr", "de", "he", "ru"]
    if code in clams_languages:
        potential_tasks.append(f"clams_{code}")

    # Check which tasks actually exist
    available_tasks = []
    for task in potential_tasks:
        if check_task_exists(task, base_path, lang):
            available_tasks.append(f"  - {task}")
            print(f"✓ Found: {task}")
        else:
            print(f"✗ Missing: {task}")
    
    # Only create group if we have at least one available task
    if available_tasks:
        group_name = f"babybabellm_{three_letter_code}"
        
        yaml_content = f"""group: {group_name}
task:
{chr(10).join(available_tasks)}
aggregate_metric_list:
  - metric: acc
    aggregation: mean
    weight_by_size: true
metadata:
  version: 1.0
"""
        
        return group_name, yaml_content
    else:
        print(f"⚠️  No tasks found for {lang} ({code}), skipping group creation")
        return None, None

def main():
    """Main function to generate conditional group files."""
    print("Generating conditional BabyBabelLM group files...")
    print("Checking task availability before including in groups...\n")
    
    # Get the base path for task directories
    script_dir = Path(__file__).parent
    base_path = script_dir.parent  # Go up one level to tasks directory
    
    created_groups = []
    skipped_groups = []

    for lang, code in lang_code_map.items():
        print(f"\n=== Processing {lang} ({code}) ===")
        
        group_name, yaml_content = generate_group_for_language(lang, code, base_path)
        
        if yaml_content:
            filename = f"{group_name}.yaml"
            filepath = script_dir / filename
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(yaml_content)
            
            created_groups.append(group_name)
            print(f"✅ Created: {filename}")
        else:
            skipped_groups.append(f"{lang} ({code})")
    
    # Summary
    print("\n=== Summary ===")
    print(f"Created {len(created_groups)} group files:")
    for group in created_groups:
        print(f"  - {group}.yaml")
    
    if skipped_groups:
        print(f"\nSkipped {len(skipped_groups)} languages (no available tasks):")
        for lang in skipped_groups:
            print(f"  - {lang}")
    
    print(f"\nTotal: {len(created_groups)} created, {len(skipped_groups)} skipped")

if __name__ == "__main__":
    main()
