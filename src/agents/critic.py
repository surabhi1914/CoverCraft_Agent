# src/agents/critic.py

'''
Purpose of this file:reviews the first draft and gives structured feedback.

This file:
1. Accept the draft cover letter
2. Accept JD analysis
3. Accept candidate profile
4. Accept evidence map
5. Accept strategy
6. Build a review prompt
7. Ask the LLM to return structured JSON feedback
8. Parse JSON response
9. Return a dictionary

'''




# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import json

from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.candidate_schema import CandidateProfile
from src.schemas.evidence_schema import EvidenceMap
from src.utils.llm_client import generate_text
from src.utils.json_utils import extract_json_from_response
from src.config import DEFAULT_TONE, DEFAULT_LENGTH



# ---------------------------------------------
# Functions
# ---------------------------------------------


def build_critic_prompt(
    draft: str,
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile,
    evidence_map: EvidenceMap,
    strategy:dict,
    tone:str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = ""
) -> str:
    
    jd_data = jd_analysis.model_dump()
    candidate_data = candidate_profile.model_dump()
    evidence_data = evidence_map.model_dump()


    return f"""
    You are an expert cover letter critic and truthfulness reviewer.

    Review the cover letter draft using the job analysis, candidate profile,
    evidence map, and writing strategy.

    Your job is to identify what should be improved before the final rewrite.

    Rules:
    - Return only valid JSON.
    - Do not include markdown.
    - Do not rewrite the full cover letter.
    - Do not invent candidate experience.
    - Check whether every claim is supported by the candidate profile or evidence map.
    - Flag unsupported or risky claims.
    - Identify generic or AI-sounding phrases.
    - Identify missing supported keywords.
    - Identify stronger evidence that should be added.
    - Check whether the draft follows the requested tone, length, and strategy.
    - Be specific and practical.

    Requested tone:
    {tone}
    Requested length:
    {length}

    User instructions:
    {user_instructions}

    Return JSON with exactly this structure:
    {{
    "overall_score": 0,
    "summary": "",
    "strengths": [],
    "issues": [
        {{
        "category": "",
        "problem": "",
        "severity": "",
        "suggested_fix": ""
        }}
    ],
    "missing_keywords": [],
    "unsupported_or_risky_claims": [],
    "generic_phrases": [],
    "evidence_to_add": [],
    "tone_feedback": "",
    "structure_feedback": "",
    "revision_instructions": []
    }}
    COVER LETTER DRAFT:
    \"\"\"
    {draft}
    \"\"\"

    JOB DESCRIPTION ANALYSIS:
    {jd_data}

    CANDIDATE PROFILE:
    {candidate_data}

    EVIDENCE MAP:
    {evidence_data}

    WRITING STRATEGY:
    {strategy}
    """
    

def review_cover_letter_draft(
    draft: str,
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile,
    evidence_map: EvidenceMap,
    strategy:dict,
    tone:str =DEFAULT_TONE,
    length:str=DEFAULT_LENGTH,
    user_instructions=""
) -> dict:
    
    if not draft or not draft.strip():
        raise ValueError("Draft cannot be empty")
    
    prompt = build_critic_prompt(
        draft= draft,
        jd_analysis = jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone=tone,
        length=length,
        user_instructions=user_instructions
    )

    response_text = generate_text(
        prompt = prompt,
        temperature=0.2,
        max_output_tokens=1800
    )

    parsed_json = extract_json_from_response(response_text)

    return parsed_json

