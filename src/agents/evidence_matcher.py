# src/agents/evidence_matcher.py

'''
Purpose of this file: brain file of the project.matches job requirements to candidate evidence.
takes JobDescriptionAnalysis + CandidateProfile and creates evidencemap. 
It basically figuresout what does the job want and how can the candidate show proof for it.

This file:
1. Accept a JobDescriptionAnalysis object
2. Accept a CandidateProfile object
3. Convert both into clean dictionaries/text for the LLM
4. Build an evidence matching prompt
5. Ask the LLM to return structured JSON
6. Parse the JSON response
7. Validate it using EvidenceMap
8. Return an EvidenceMap object
'''


# ---------------------------------------------
# Importing libraries
# ---------------------------------------------
import json
from src.utils.llm_client import generate_text
from src.utils.json_utils import extract_json_from_response
from src.utils.text_cleaning import prepare_text_for_llm
from src.schemas.candidate_schema import CandidateProfile
from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.evidence_schema import EvidenceMap



# ---------------------------------------------
# Functions
# ---------------------------------------------




def build_evidence_matching_prompt(
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile
) -> str:
    jd_data = jd_analysis.model_dump()
    candidate_data = candidate_profile.model_dump()
    return f"""

    You are an expert career evidence matcher.

    `    Your task is to compare a structured job description analysis with a structured candidate profile.

        The goal is to identify which candidate experiences, projects, skills, education, and achievements best support the job requirements.

        Rules:
        - Return only valid JSON.
        - Do not include markdown.
        - Do not include explanations outside the JSON.
        - Use only the candidate profile as evidence.
        - Do not invent experience, metrics, skills, tools, companies, publications, or achievements.
        - Do not exaggerate weak evidence.
        - If a job requirement is not clearly supported, place it in unsupported_requirements.
        - Prefer specific evidence from projects, experience, education, or achievements.
        - Do not write the cover letter.
        - Keep evidence concise but specific.

        Match strength guide:
        - strong: directly supported by specific candidate evidence
        - medium: reasonably related but not exact
        - weak: lightly related or indirect
        - none: not supported by candidate evidence

        Return JSON with exactly this structure:
        {{
        "role_title": "",
        "company_name": "",
        "overall_match_summary": "",
        "strong_matches": [
            {{
            "job_requirement": "",
            "candidate_evidence": "",
            "evidence_source": "",
            "match_strength": "strong",
            "skills_connected": [],
            "keywords_covered": [],
            "suggested_angle": "",
            "use_in_cover_letter": true
            }}
        ],
        "medium_matches": [
            {{
            "job_requirement": "",
            "candidate_evidence": "",
            "evidence_source": "",
            "match_strength": "medium",
            "skills_connected": [],
            "keywords_covered": [],
            "suggested_angle": "",
            "use_in_cover_letter": true
            }}
        ],
        "weak_matches": [
            {{
            "job_requirement": "",
            "candidate_evidence": "",
            "evidence_source": "",
            "match_strength": "weak",
            "skills_connected": [],
            "keywords_covered": [],
            "suggested_angle": "",
            "use_in_cover_letter": false
            }}
        ],
        "unsupported_requirements": [
            {{
            "job_requirement": "",
            "reason": "",
            "recommendation": ""
            }}
        ],
        "recommended_cover_letter_focus": [],
        "keywords_to_include": [],
        "keywords_to_avoid_or_handle_carefully": []
        }}

        JOB DESCRIPTION ANALYSIS:
        {jd_data}

        CANDIDATE PROFILE:
        {candidate_data}`

    """
    

def match_evidence(
    jd_analysis: JobDescriptionAnalysis,
    candidate_profile: CandidateProfile
) -> EvidenceMap:
    prompt = build_evidence_matching_prompt(
        jd_analysis=jd_analysis,
        candidate_profile=candidate_profile
    )

    response_text = generate_text(
        prompt=prompt,
        temperature=0.2,
        max_output_tokens=2500,
    )


    parsed_json = extract_json_from_response(response_text)

    return EvidenceMap(**parsed_json)
    


# def summarize_candidate_for_matching(candidate_profile: CandidateProfile) -> str: