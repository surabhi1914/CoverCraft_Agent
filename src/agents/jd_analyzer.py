# src/agents/jd_analyzer.py

'''
Purpose of this file: takes a raw job description and converts it into structured job analysis.

This file:
1. Accept raw job description text
2. Clean the JD text
3. Build a clear prompt for the LLM
4. Ask the LLM to return JSON
5. Parse the JSON response
6. Validate it using JobDescriptionAnalysis
7. Return a clean structured object

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import json

from src.utils.text_cleaning import prepare_text_for_llm
from src.utils.llm_client import generate_text
from src.schemas.jd_schema import JobDescriptionAnalysis



# ---------------------------------------------
# Functions
# ---------------------------------------------

def build_jd_analysis_prompt(job_description: str) -> str:
    '''
    A prompt that asks the LLM to analyze a job description 
    and return the structured JSON

    '''
    return f""""
        You are an expert job description analyst.

        Analyze the job description below and extract structured information for a personalized cover letter system.

        Rules:
        - Return only valid JSON.
        - Do not include markdown.
        - Do not include explanations.
        - Do not invent missing information.
        - If company, title, location, or employment type are missing, use "Unknown".
        - Keep lists concise but complete.
        - Focus on what a candidate should emphasize in a cover letter.

        Return JSON with exactly these fields:
        {{
        "company_name": "",
        "role_title": "",
        "employment_type": "",
        "location": "",
        "role_summary": "",
        "core_responsibilities": [],
        "required_skills": [],
        "preferred_skills": [],
        "technical_keywords": [],
        "soft_skills": [],
        "company_values": [],
        "candidate_focus_areas": [],
        "red_flags_or_gaps": []
        }}

        Job description:
        \"\"\"
        {job_description}
        \"\"\"
        """

def extract_json_from_response(response_text: str) -> dict:
    '''
    Extract and parse JSON from the LLM response
    '''
    cleaned = response_text.strip()
    if not cleaned:
        raise ValueError("LLM response is empty")
    
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json. JSONDecodeError as e:
        raise ValueError(f" Failed to parse JSON from LLM response: {e}")
    

def analyze_job_description(job_description: str) -> JobDescriptionAnalysis:
    '''
    Analyze a raw job description and return a validated JobDescriptionAnalysis object
    '''

    if not job_description or  not job_description.strip():
        raise ValueError("Job description is Empty")
    
    cleaned_jd = prepare_text_for_llm(job_description)
    prompt = build_jd_analysis_prompt(cleaned_jd)

    response_text = generate_text(
        prompt=prompt,
        temperature=0.2, # since we want extraction rather than creativity here
        max_output_tokens=1500

    )
    
    parsed_json = extract_json_from_response(response_text)

    return JobDescriptionAnalysis(**parsed_json) #validating with pydantic because it turn raw model json into a structured object

# analyze_job_description_from_file(file_path: str)