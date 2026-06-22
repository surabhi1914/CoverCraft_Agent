# src/agents/strategy_planner.py

'''
Purpose of this file: decides how the cover letter should be structured before we generate the actual draft.

This file:
1. Accept JD analysis, candidate profile, evidence map
2. Accept method preference
3. Accept user instructions
4. Build a planning prompt
5. Ask the LLM for a structured strategy
6. Parse JSON response
7. Return a dictionary for now

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------

# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import json
from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.candidate_schema import CandidateProfile
from src.schemas.evidence_schema import EvidenceMap
from src.utils.llm_client import generate_text
from src.utils.json_utils import extract_json_from_response
from src.config import DEFAULT_METHOD, DEFAULT_LENGTH, DEFAULT_TONE

# ---------------------------------------------
# Functions
# ---------------------------------------------

def build_strategy_prompt(
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile,
    evidence_map: EvidenceMap,
    method: str = DEFAULT_METHOD,
    user_instructions: str = "",
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH
) -> str:
    jd_data = jd_analysis.model_dump()
    candidate_data = candidate_profile.model_dump()
    evidence_data = evidence_map.model_dump()

    return f"""
    You are an expert cover letter strategist.

    Your task is to create a clear writing strategy for a personalized cover letter.

    Rules:
    - Return only valid JSON.
    - Do not include markdown.
    - Do not write the full cover letter yet.
    - Use only the provided candidate profile and evidence map.
    - Do not invent achievements, metrics, tools, or experience.
    - Prioritize strong evidence over weak evidence.
    - Avoid unsupported requirements.
    - Make the strategy specific to the role and company.
    - Follow the requested method as closely as possible.

    Requested method:
    {method}

    Requested tone:
    {tone}

    Requested length:
    {length}

    User instructions:
    {user_instructions}

    Return JSON with exactly this structure:
    {{
    "method_used": "",
    "overall_strategy": "",
    "opening_strategy": "",
    "body_paragraphs": [
        {{
        "paragraph_goal": "",
        "evidence_to_use": [],
        "keywords_to_include": [],
        "tone_guidance": ""
        }}
    ],
    "closing_strategy": "",
    "must_include": [],
    "avoid": [],
    "suggested_length": "",
    "tone_notes": ""
    }}

    JOB DESCRIPTION ANALYSIS:
    {jd_data}

    CANDIDATE PROFILE:
    {candidate_data}

    EVIDENCE MAP:
    {evidence_data}
    """

    

def plan_cover_letter_strategy(
    jd_analysis:JobDescriptionAnalysis,
    candidate_profile:CandidateProfile,
    evidence_map:EvidenceMap,
    method:str = DEFAULT_METHOD,
    user_instructions:str ="",
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
) -> dict:
    
    prompt = build_strategy_prompt(
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        method=method,
        user_instructions=user_instructions,
        tone=tone,
        length=length,
    )

    response_text = generate_text(
        prompt = prompt,
        temperature = 0.3, # 0.3 because strategy planning needs a tiny bit more flexibility than pure extraction, but still should stay controlled.
        max_output_tokens=1800
    )

    parsed_json = extract_json_from_response(response_text)

    return parsed_json

