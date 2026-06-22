# src/pipeline/run_cover_letter_pipeline.py

'''
Purpose of this file: Main orchestrator

This file:
1. Validate user inputs
2. Build candidate profile
3. Analyze job description
4. Match evidence
5. Plan strategy
6. Generate first draft
7. Review draft
8. Rewrite final letter
9. Return all results

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------



# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from src.agents.candidate_builder import build_candidate_profile
from src.agents.jd_analyzer import analyze_job_description
from src.agents.evidence_matcher import match_evidence
from src.agents.strategy_planner import plan_cover_letter_strategy
from src.agents.draft_generator import generate_cover_letter_draft
from src.agents.critic import review_cover_letter_draft
from src.agents.final_rewriter import rewrite_final_cover_letter
from src.config import DEFAULT_METHOD, DEFAULT_TONE, DEFAULT_LENGTH



# ---------------------------------------------
# Functions
# ---------------------------------------------

def validate_pipeline_inputs(
    candidate_source_text: str,
    job_description_text: str,
) -> None:
    if not candidate_source_text or not candidate_source_text.strip():
        raise ValueError("Candidate source text cannot be empty.")

    if not job_description_text or not job_description_text.strip():
        raise ValueError("Job description text cannot be empty.")


def run_cover_letter_pipeline(
    candidate_source_text: str,
    job_description_text: str,
    method: str = DEFAULT_METHOD,
    tone: str = DEFAULT_TONE,
    length: str = DEFAULT_LENGTH,
    user_instructions: str = "",
) -> dict:
    validate_pipeline_inputs(
        candidate_source_text=candidate_source_text,
        job_description_text=job_description_text
    )

    candidate_profile = build_candidate_profile(candidate_source_text)

    jd_analysis = analyze_job_description(job_description_text)

    evidence_map = match_evidence(jd_analysis=jd_analysis, candidate_profile=candidate_profile)

    strategy = plan_cover_letter_strategy(
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        method=method,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
    )

    draft = generate_cover_letter_draft(
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
    )

    critic_review = review_cover_letter_draft(
        draft=draft,
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
    )

    final_letter = rewrite_final_cover_letter(
        draft=draft,
        critic_review=critic_review,
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile,
        evidence_map=evidence_map,
        strategy=strategy,
        tone=tone,
        length=length,
        user_instructions=user_instructions,
    )

    return {
        "candidate_profile": candidate_profile.model_dump(),
        "jd_analysis": jd_analysis.model_dump(),
        "evidence_map": evidence_map.model_dump(),
        "strategy": strategy,
        "draft": draft,
        "critic_review": critic_review,
        "final_letter": final_letter,
    }
