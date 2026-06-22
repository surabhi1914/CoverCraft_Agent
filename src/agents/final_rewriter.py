# src/agents/final_rewriter.py

'''
Purpose of this file: 
takes first draft + critic feedback and produces the polished final cover letter

This file:
1. Accept the original draft
2. Accept critic feedback
3. Accept JD analysis, candidate profile, evidence map, and strategy
4. Build a rewrite prompt
5. Ask the LLM to revise the draft
6. Return only the final cover letter text

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------


# ---------------------------------------------
# Importing libraries
# ---------------------------------------------

from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.candidate_schema import CandidateProfile
from src.schemas.evidence_schema import EvidenceMap
from src.utils.llm_client import generate_text
from src.config import DEFAULT_TONE, DEFAULT_LENGTH


# ---------------------------------------------
# Functions
# ---------------------------------------------


def build_final_rewrite_prompt(
    draft:str,
    critic_review:dict,
    jd_analysis:JobDescriptionAnalysis,
    candidate_profile:CandidateProfile,
    evidence_map:EvidenceMap,
    strategy:dict,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = ""
) -> str:
    jd_data = jd_analysis.model_dump()
    candidate_data = candidate_profile.model_dump()
    evidence_data = evidence_map.model_dump()

    return f"""
    You are an expert cover letter editor.

    Rewrite the draft cover letter into a polished final version using the critic feedback.

    Rules:
    - Return only the final cover letter text.
    - Do not include markdown headings.
    - Do not include explanations.
    - Do not mention the critic review, evidence map, or strategy.
    - Use only the provided candidate profile and evidence map.
    - Do not invent experience, metrics, tools, companies, degrees, publications, or achievements.
    - Remove or soften unsupported claims.
    - Add stronger supported evidence when useful.
    - Remove generic or AI-sounding phrases.
    - Keep the tone natural, professional, warm, and confident.
    - Keep the length aligned with the requested length.
    - Do not turn the letter into a resume summary.
    - Do not use bullet points unless the user requested them.

    Requested tone:
    {tone}
    Requested length:
    {length}

    User instructions:
    {user_instructions}

    ORIGINAL DRAFT:
    \"\"\"
    {draft}
    \"\"\"

    CRITIC REVIEW:
    {critic_review}

    WRITING STRATEGY:
    {strategy}

    JOB DESCRIPTION ANALYSIS:
    {jd_data}

    CANDIDATE PROFILE:
    {candidate_data}

    EVIDENCE MAP:
    {evidence_data}
    """
    

def rewrite_final_cover_letter(
    draft: str,
    critic_review: dict,
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile:CandidateProfile,
    evidence_map:EvidenceMap,
    strategy:dict,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str =""
) -> str:
    
    if not draft or not draft.strip():
        raise ValueError("Draft cannot be empty")
    
    if not critic_review:
        raise ValueError("Critic review cannot be empty")
    
    prompt = build_final_rewrite_prompt(        
        draft = draft,
        critic_review=critic_review,
        jd_analysis = jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone=tone,
        length=length,
        user_instructions=user_instructions
    )


    final_letter = generate_text(
        prompt = prompt,
        temperature=0.4,
        max_output_tokens=1600
    )

    return final_letter.strip()

