# src/pipeline/run_from_files.py

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
# Importing libraries
# ---------------------------------------------
from pathlib import Path
from typing import List

from src.parsers.document_parser import parse_document
from src.pipeline.run_cover_letter_pipeline import run_cover_letter_pipeline
from src.config import RAW_DATA_DIR, SUPPORTED_DOCUMENT_TYPES,DEFAULT_METHOD, DEFAULT_TONE, DEFAULT_LENGTH


# ---------------------------------------------
# Functions
# ---------------------------------------------
def get_candidate_files_from_raw(
    raw_data_dir: str | Path = RAW_DATA_DIR,
) -> List[Path]:
    """
    Find all supported candidate source files inside data/raw.
    """
    raw_data_dir = Path(raw_data_dir)

    if not raw_data_dir.exists():
        raise FileNotFoundError(f"Raw data directory does not exist: {raw_data_dir}")

    candidate_files = []

    for file_path in raw_data_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_DOCUMENT_TYPES:
            candidate_files.append(file_path)

    if not candidate_files:
        raise ValueError(
            f"No supported candidate files found in {raw_data_dir}. "
            f"Supported types: {SUPPORTED_DOCUMENT_TYPES}"
        )

    return sorted(candidate_files)


def combine_raw_candidate_documents(
    raw_data_dir: str | Path = RAW_DATA_DIR,
) -> str:
    """
    Parse and combine all candidate source documents from data/raw.
    """
    candidate_files = get_candidate_files_from_raw(raw_data_dir)

    combined_sections = []

    for file_path in candidate_files:
        parsed_doc = parse_document(file_path)

        section = f"""
SOURCE FILE: {parsed_doc["file_name"]}

{parsed_doc["text"]}
"""
        combined_sections.append(section.strip())

    return "\n\n---\n\n".join(combined_sections)


def run_cover_letter_pipeline_from_files(
    job_description_text: str,
    method: str = DEFAULT_METHOD,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = "",
    raw_data_dir: str | Path = RAW_DATA_DIR,
    use_candidate_cache: bool = True,
    
) -> dict:
    """
    Run the cover letter pipeline using candidate files from data/raw
    and a job description provided directly as text.
    """
    if not job_description_text or not job_description_text.strip():
        raise ValueError("Job description text cannot be empty.")

    candidate_source_text = combine_raw_candidate_documents(raw_data_dir)

    result = run_cover_letter_pipeline(
        candidate_source_text=candidate_source_text,
        job_description_text=job_description_text,
        method=method,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
        use_candidate_cache=use_candidate_cache,
    )

    return result