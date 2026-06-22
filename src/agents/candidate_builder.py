# src/agents/candidate_builder.py

'''
Purpose of this file: converts your raw resume/CV/project/profile text into a structured CandidateProfile

This file:
1. Accept candidate source text
2. Clean the text
3. Build a prompt for the LLM
4. Ask the model to extract structured candidate information
5. Parse the JSON response
6. Validate it using CandidateProfile
7. Return a CandidateProfile object

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import json
from src.utils.llm_client import generate_text
from src.utils.text_cleaning import prepare_text_for_llm
from src.schemas.candidate_schema import CandidateProfile

# ---------------------------------------------
# Functions
# ---------------------------------------------

def build_candidate_profile_prompt(candidate_source_text: str) -> str:
    return f"""
    You are an expert resume and candidate profile analyst.

    Analyze the candidate source material below and extract structured candidate information for a personalized cover letter system.

    Rules:
    - Return only valid JSON.
    - Do not include markdown.
    - Do not include explanations.
    - Do not invent experience, metrics, skills, tools, education, publications, or achievements.
    - Use only the provided candidate source material.
    - If a field is missing, use an empty string or empty list.
    - Keep descriptions concise but specific.
    - Preserve important tool names, metrics, project names, and organizations exactly when possible.

    Return JSON with exactly this structure:
    {{
    "name": "",
    "headline": "",
    "target_roles": [],
    "education": [
        {{
        "institution": "",
        "degree": "",
        "field_of_study": "",
        "start_date": "",
        "end_date": "",
        "details": []
        }}
    ],
    "experience": [
        {{
        "organization": "",
        "role_title": "",
        "start_date": "",
        "end_date": "",
        "location": "",
        "responsibilities": [],
        "achievements": [],
        "skills_used": []
        }}
    ],
    "projects": [
        {{
        "project_name": "",
        "project_summary": "",
        "tools_used": [],
        "methods_used": [],
        "outcomes": [],
        "relevance_tags": []
        }}
    ],
    "technical_skills": [],
    "soft_skills": [],
    "certifications": [],
    "publications": [],
    "achievements": [
        {{
        "title": "",
        "description": "",
        "category": ""
        }}
    ],
    "work_authorization": "",
    "location_preferences": "",
    "career_summary": ""
    }}

    Candidate source material:
    \"\"\"
    {candidate_source_text}
    \"\"\"
    """

def extract_json_from_response(response_text: str) -> dict:
    cleaned = response_text.strip()

    if not cleaned:
        raise ValueError("LLM response is empty")
    
    cleaned = cleaned.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except json. JSONDecodeError as e:
        raise ValueError(f" Failed to parse JSON from LLM response: {e}")
    



def build_candidate_profile(candidate_source_text: str) -> CandidateProfile:

    candidate_text = candidate_source_text.strip()

    if not candidate_text:
        raise ValueError("")


    cleaned_text = prepare_text_for_llm(candidate_source_text)
    prompt = build_candidate_profile_prompt(cleaned_text)
    
    response_text = generate_text(
        prompt = prompt,
        temperature=0.2,
        max_output_tokens=2500 # 2500 because Candidate profiles are longer than JD analysis because they may include education, experience, projects, skills, and achievements
    )

    parsed_json = extract_json_from_response(response_text)

    return CandidateProfile(**parsed_json) #validating with pydantic because it turn raw model json into a structured object
