#!/usr/bin/env python3
"""Print an aggregate markdown table of lm-eval results from results/."""

import json
from glob import glob
from pathlib import Path


def parse_groups(results: dict) -> dict[str, dict[str, float]]:
    """Parse results JSON into {group -> {task -> score}}.

    indent=0: language group (e.g. zeroshot_eng)
    indent=1: task rows (e.g. blimp, multiblimp_eng)
    indent=2: subtasks already aggregated into indent=1, skip
    """
    groups: dict[str, dict[str, float]] = {}
    current_group = None

    for task_name, task_data in results.items():
        alias = task_data.get("alias", task_name)
        indent = len(alias) - len(alias.lstrip())
        acc = task_data.get("acc,none")

        if indent == 0:
            current_group = task_name
            groups[current_group] = {}
        elif indent == 1 and current_group is not None and acc is not None:
            groups[current_group][task_name] = round(acc * 100, 2)

    return groups


def load_model(json_path: str) -> dict[str, dict[str, float]]:
    with open(json_path) as f:
        data = json.load(f)
    return parse_groups(data["results"])


def fmt_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def main():
    results_dir = Path(__file__).parent.parent / "results"
    json_files = sorted(glob(str(results_dir / "**/results*.json"), recursive=True))

    # model name = name of folder directly containing the results JSON
    # multiple JSON files can share the same folder (one per language run) — merge them
    all_models: dict[str, dict[str, dict[str, float]]] = {}
    for json_path in json_files:
        model_name = Path(json_path).parent.name.split("__")[-1]
        if model_name not in all_models:
            all_models[model_name] = {}
        for group, tasks in load_model(json_path).items():
            all_models[model_name][group] = tasks

    if not all_models:
        print("No results found.")
        return

    # Collect all groups and tasks, preserving first-seen order
    group_tasks: dict[str, list[str]] = {}
    for model_groups in all_models.values():
        for group, tasks in model_groups.items():
            if group not in group_tasks:
                group_tasks[group] = []
            for task in tasks:
                if task not in group_tasks[group]:
                    group_tasks[group].append(task)

    models = sorted(all_models.keys())

    # Header: task | model1 | model2 | ...
    print(fmt_row(["task"] + models))
    print(fmt_row(["---"] + ["---"] * len(models)))

    for group, tasks in group_tasks.items():
        # Language group header row
        print(fmt_row([f"**{group}**"] + [""] * len(models)))

        # One row per task
        for task in tasks:
            row = [task]
            for model in models:
                val = all_models[model].get(group, {}).get(task)
                row.append(f"{val:.2f}" if val is not None else "")
            print(fmt_row(row))

        # Average row for this language group
        avg_row = ["*avg*"]
        for model in models:
            scores = [all_models[model].get(group, {}).get(t) for t in tasks]
            valid = [s for s in scores if s is not None]
            avg = round(sum(valid) / len(valid), 2) if valid else None
            avg_row.append(f"{avg:.2f}" if avg is not None else "")
        print(fmt_row(avg_row))


if __name__ == "__main__":
    main()
