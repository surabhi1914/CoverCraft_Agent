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
from src.config import DEFAULT_METHOD, DEFAULT_TONE, DEFAULT_LENGTH


# ---------------------------------------------
# Functions
# ---------------------------------------------
def combine_candidate_documents(candidate_file_paths: List[str]) -> str:
    if not candidate_file_paths:
        raise ValueError("At least one candidate source file is required.")

    combined_sections = []

    for file_path in candidate_file_paths:
        parsed_doc = parse_document(file_path)

        section = f"""
        SOURCE FILE: {parsed_doc["file_name"]}

        {parsed_doc["text"]}
        """
        combined_sections.append(section.strip())

    return "\n\n---\n\n".join(combined_sections)

def run_cover_letter_pipeline_from_files(
    candidate_file_paths: List[str],
    job_description_file_path: str,
    method: str = DEFAULT_METHOD,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = "",
) -> dict:
    if not job_description_file_path:
        raise ValueError("Job description file path is required.")

    candidate_source_text = combine_candidate_documents(candidate_file_paths)

    parsed_jd = parse_document(job_description_file_path)
    job_description_text = parsed_jd["text"]

    result = run_cover_letter_pipeline(
        candidate_source_text=candidate_source_text,
        job_description_text=job_description_text,
        method=method,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
    )

    return result