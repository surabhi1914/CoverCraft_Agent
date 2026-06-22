# src/agents/draft_generator.py

'''
Purpose of this file: file that finally writes the first cover letter draft.

This file:
1. Accept structured JD analysis
2. Accept structured candidate profile
3. Accept evidence map
4. Accept cover letter strategy
5. Build a strong drafting prompt
6. Call the LLM
7. Return the draft text

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------



# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.candidate_schema import CandidateProfile
from src.schemas.evidence_schema import EvidenceMap
from src.utils.llm_client import generate_text
from src.config import DEFAULT_TONE, DEFAULT_LENGTH


# ---------------------------------------------
# Functions
# ---------------------------------------------

def build_draft_prompt(
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile,
    evidence_map: EvidenceMap,
    strategy: dict,
    tone: str = DEFAULT_TONE,
    length:str = DEFAULT_LENGTH,
    user_instructions:str = ""
) -> str:
    jd_data = jd_analysis.model_dump()
    candidate_data = candidate_profile.model_dump()
    evidence_data = evidence_map.model_dump()
    return f"""
    You are an expert cover letter writer.

    Write a personalized first-draft cover letter using the provided job analysis,
    candidate profile, evidence map, and writing strategy.

    Rules:
    - Use only the provided candidate profile and evidence map.
    - Do not invent experience, metrics, tools, companies, degrees, publications, or achievements.
    - Do not claim unsupported requirements.
    - Follow the provided cover letter strategy.
    - Include supported keywords naturally.
    - Do not force keywords if they are unsupported.
    - Do not repeat the resume as a list.
    - Make the writing specific, human, and professional.
    - Avoid generic openings like "I am writing to express my interest" unless it truly fits.
    - Do not mention that you are using an evidence map or strategy.
    - Do not include bullet points unless the user specifically asks.
    - Return only the cover letter text.

    Tone:
    {tone}

    Length:
    {length}

    User instructions:
    {user_instructions}

    COVER LETTER STRATEGY:
    {strategy}

    JOB DESCRIPTION ANALYSIS:
    {jd_data}

    CANDIDATE PROFILE:
    {candidate_data}

    EVIDENCE MAP:
    {evidence_data}

    """

def generate_cover_letter_draft(
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile,
    evidence_map: EvidenceMap,
    strategy: dict,
    tone:str= DEFAULT_TONE,
    length: str =DEFAULT_LENGTH,
    user_instructions : str =""
) -> str:
    prompt = build_draft_prompt(
        jd_analysis= jd_analysis,
        candidate_profile= candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone= tone,
        length= length,
        user_instructions=user_instructions
    )


    draft = generate_text(
        prompt=prompt,
        temperature=0.5,
        max_output_tokens=1600, # 1600 because drafting needs more natural writing than extraction. But we still don’t want wild creativity.
    )
    
    return draft.strip()