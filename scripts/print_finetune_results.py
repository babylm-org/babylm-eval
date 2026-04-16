#!/usr/bin/env python3
"""Print an aggregate markdown table of finetuning results from finetune/results/."""

import json
from pathlib import Path


_LANG_COMBO_ORDER = [
    frozenset({"eng"}),
    frozenset({"nld"}),
    frozenset({"zho"}),
    frozenset({"eng", "nld"}),
    frozenset({"eng", "zho"}),
    frozenset({"nld", "zho"}),
    frozenset({"eng", "nld", "zho"}),
]

# Map directory language codes to the canonical 3-letter codes used for ordering
_DIR_LANG_TO_CANONICAL = {"en": "eng", "nl": "nld", "zh": "zho"}


def training_languages(model_name: str) -> frozenset[str]:
    """Infer the training language(s) from a model name."""
    name = model_name.lower()

    if "strict" in name:
        return frozenset({"eng"})

    for lang in ("nld", "zho"):
        if f"babylm-{lang}" in name:
            return frozenset({lang})

    langs: set[str] = set()
    if "en_" in name or "_en_" in name or name.startswith("en"):
        langs.add("eng")
    if "nld" in name:
        langs.add("nld")
    if "zho" in name:
        langs.add("zho")
    if langs:
        return frozenset(langs)

    return frozenset()


def model_sort_key(model_name: str) -> tuple[int, str]:
    langs = training_languages(model_name)
    try:
        order = _LANG_COMBO_ORDER.index(langs)
    except ValueError:
        order = len(_LANG_COMBO_ORDER)
    return (order, model_name)


def fmt_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def load_results(finetune_dir: Path) -> dict[str, dict[str, dict[str, float]]]:
    """Return {model -> {lang -> {task -> eval_accuracy (as %)}}}."""
    all_models: dict[str, dict[str, dict[str, float]]] = {}

    for result_file in sorted(finetune_dir.glob("*/*/*/all_results.json")):
        model, lang, task = result_file.parts[-4], result_file.parts[-3], result_file.parts[-2]
        with open(result_file) as f:
            data = json.load(f)
        acc = data.get("eval_accuracy")
        if acc is None:
            continue
        all_models.setdefault(model, {}).setdefault(lang, {})[task] = round(acc * 100, 2)

    return all_models


def main():
    finetune_dir = Path(__file__).parent.parent / "finetune" / "results"
    all_models = load_results(finetune_dir)

    if not all_models:
        print("No results found.")
        return

    # Collect all langs and tasks in first-seen order
    lang_tasks: dict[str, list[str]] = {}
    for model_langs in all_models.values():
        for lang, tasks in model_langs.items():
            if lang not in lang_tasks:
                lang_tasks[lang] = []
            for task in tasks:
                if task not in lang_tasks[lang]:
                    lang_tasks[lang].append(task)

    # Sort tasks within each language alphabetically for consistency
    for lang in lang_tasks:
        lang_tasks[lang].sort()

    # Sort languages: canonical order where possible, else alphabetical
    def lang_sort_key(lang: str) -> tuple[int, str]:
        canonical = _DIR_LANG_TO_CANONICAL.get(lang, lang)
        for i, combo in enumerate(_LANG_COMBO_ORDER):
            if combo == frozenset({canonical}):
                return (i, lang)
        return (len(_LANG_COMBO_ORDER), lang)

    sorted_langs = sorted(lang_tasks.keys(), key=lang_sort_key)
    models = sorted(all_models.keys(), key=model_sort_key)

    # Header
    print(fmt_row(["task"] + models))
    print(fmt_row(["---"] + ["---"] * len(models)))

    for lang in sorted_langs:
        tasks = lang_tasks[lang]
        print(fmt_row([f"**{lang}**"] + [""] * len(models)))

        for task in tasks:
            vals = [all_models[model].get(lang, {}).get(task) for model in models]
            best = max((v for v in vals if v is not None), default=None)
            row = [task]
            for val in vals:
                if val is None:
                    row.append("")
                elif val == best:
                    row.append(f"**{val:.2f}**")
                else:
                    row.append(f"{val:.2f}")
            print(fmt_row(row))

        # Average row for this language
        avgs = []
        for model in models:
            scores = [all_models[model].get(lang, {}).get(t) for t in tasks]
            valid = [s for s in scores if s is not None]
            avgs.append(round(sum(valid) / len(valid), 2) if valid else None)
        best_avg = max((a for a in avgs if a is not None), default=None)
        avg_row = ["*avg*"]
        for avg in avgs:
            if avg is None:
                avg_row.append("")
            elif avg == best_avg:
                avg_row.append(f"**{avg:.2f}**")
            else:
                avg_row.append(f"{avg:.2f}")
        print(fmt_row(avg_row))


if __name__ == "__main__":
    main()