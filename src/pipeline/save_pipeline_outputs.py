# src/pipeline/save_pipeline_outputs.py

'''
Purpose of this file: saves the results from your pipeline into files.

This file:
1. Accept the result dictionary from run_cover_letter_pipeline()
2. Save final letter as .md
3. Save draft as .md
4. Save structured outputs as .json
5. Save the full result dictionary as .json
6. Return the saved file paths

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------


# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from pathlib import Path
from typing import Dict, Any

from src.config import OUTPUT_DIR
from src.utils.file_utils import save_json, save_text




REQUIRED_RESULT_KEYS = [
    "candidate_profile",
    "jd_analysis",
    "evidence_map",
    "strategy",
    "draft",
    "critic_review",
    "final_letter",
]



# ---------------------------------------------
# Functions
# ---------------------------------------------

def save_pipeline_outputs(result: dict, output_dir: str | Path = OUTPUT_DIR) -> dict:
    if not result:
        raise ValueError("Pipeline result cannot be empty.")

    missing_keys = [key for key in REQUIRED_RESULT_KEYS if key not in result]

    if missing_keys:
        raise ValueError(f"Pipeline result is missing keys: {missing_keys}")


    paths = get_output_paths(output_dir)

    save_text(result.get("final_letter", ""), paths["final_letter"])
    save_text(result.get("draft", ""), paths["draft"])

    save_json(result.get("candidate_profile", {}), paths["candidate_profile"])
    save_json(result.get("jd_analysis", {}), paths["jd_analysis"])
    save_json(result.get("evidence_map", {}), paths["evidence_map"])
    save_json(result.get("strategy", {}), paths["strategy"])
    save_json(result.get("critic_review", {}), paths["critic_review"])
    save_json(result, paths["full_result"])

    return {key: str(path) for key, path in paths.items()}


def get_output_paths(output_dir: str | Path) -> dict:
    output_dir = Path(output_dir)

    return {
        "final_letter": output_dir / "final_cover_letter.md",
        "draft": output_dir / "draft_cover_letter.md",
        "candidate_profile": output_dir / "candidate_profile.json",
        "jd_analysis": output_dir / "jd_analysis.json",
        "evidence_map": output_dir / "evidence_map.json",
        "strategy": output_dir / "strategy.json",
        "critic_review": output_dir / "critic_review.json",
        "full_result": output_dir / "full_pipeline_result.json",
    }