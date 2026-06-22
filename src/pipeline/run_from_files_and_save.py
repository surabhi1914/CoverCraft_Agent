# src/pipeline/run_from_files_and_save.py

'''
Purpose of this file: lets you run the full cover letter pipeline using actual files instead of pasted strings.

This file:
1. Accept candidate file paths
2. Accept job description file path
3. Parse candidate documents
4. Load or parse the JD
5. Combine candidate source text
6. Run the full pipeline
7. Return the result dictionary

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------

from pathlib import Path
from typing import Any, Dict, List

from src.pipeline.run_from_files import run_cover_letter_pipeline_from_files
from src.pipeline.save_pipeline_outputs import save_pipeline_outputs
from src.config import DEFAULT_METHOD, DEFAULT_TONE, DEFAULT_LENGTH, OUTPUT_DIR


# ---------------------------------------------
# Functions
# ---------------------------------------------
def run_from_files_and_save(
    candidate_file_paths: List[str],
    job_description_file_path: str,
    method: str = DEFAULT_METHOD,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = "",
    output_dir: str | Path = OUTPUT_DIR,
) -> Dict[str, Any]:
    
    result = run_cover_letter_pipeline_from_files(
    candidate_file_paths=candidate_file_paths,
    job_description_file_path=job_description_file_path,
    method=method,
    tone=tone,
    length=length,
    user_instructions=user_instructions,
    )


    saved_paths = save_pipeline_outputs(
    result=result,
    output_dir=output_dir,
    )

    return {
    "result": result,
    "saved_paths": saved_paths,
}

