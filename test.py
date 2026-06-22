from src.schemas.jd_schema import JobDescriptionAnalysis
from src.schemas.candidate_schema import CandidateProfile, ProjectItem
from src.schemas.evidence_schema import EvidenceMap, EvidenceMatch, UnsupportedRequirement
from src.agents.strategy_planner import build_strategy_prompt
from src.agents.draft_generator import generate_cover_letter_draft


# 1. Create fake JD analysis
jd = JobDescriptionAnalysis(
    company_name="Example Company",
    role_title="Machine Learning Engineer",
    core_responsibilities=[
        "Build machine learning pipelines",
        "Collaborate with product and engineering teams"
    ],
    required_skills=["Python", "machine learning", "model evaluation"],
    technical_keywords=["Python", "machine learning", "pipeline", "model evaluation"],
    candidate_focus_areas=[
        "machine learning projects",
        "pipeline development",
        "technical communication"
    ]
)


# 2. Create fake candidate profile
bioverify = ProjectItem(
    project_name="BioVerify",
    project_summary="Built a species verification pipeline for iNaturalist predator-prey images.",
    tools_used=["Python", "LLaMA 3", "GroundingDINO", "BioCLIP2"],
    methods_used=["LLM prompting", "object detection", "image classification"],
    outcomes=["Improved species-level accuracy from 54.98% to 71.93%"],
    relevance_tags=["machine learning", "computer vision", "AI pipeline"]
)

candidate = CandidateProfile(
    name="Surabhi Nair",
    headline="Machine learning and data science graduate",
    target_roles=["Applied AI Engineer", "Machine Learning Engineer"],
    projects=[bioverify],
    technical_skills=["Python", "SQL", "Neo4j", "PyTorch"],
    soft_skills=["communication", "collaboration"]
)


# 3. Create fake evidence map
strong_match = EvidenceMatch(
    job_requirement="Build machine learning pipelines",
    candidate_evidence="Built BioVerify, a species verification pipeline using LLaMA 3, GroundingDINO, and BioCLIP2.",
    evidence_source="BioVerify project",
    match_strength="strong",
    skills_connected=["Python", "machine learning", "computer vision"],
    keywords_covered=["Python", "machine learning", "pipeline"],
    suggested_angle="Use BioVerify as the strongest technical example.",
    use_in_cover_letter=True
)

gap = UnsupportedRequirement(
    job_requirement="Production deployment experience",
    reason="Candidate profile does not clearly show production deployment experience.",
    recommendation="Do not claim production deployment. Emphasize applied project pipeline experience instead."
)

evidence_map = EvidenceMap(
    role_title="Machine Learning Engineer",
    company_name="Example Company",
    overall_match_summary="The candidate has strong evidence for applied machine learning and pipeline-oriented project work.",
    strong_matches=[strong_match],
    medium_matches=[],
    weak_matches=[],
    unsupported_requirements=[gap],
    recommended_cover_letter_focus=[
        "Applied machine learning",
        "AI pipeline development",
        "Research-based problem solving"
    ],
    keywords_to_include=["Python", "machine learning", "pipeline"],
    keywords_to_avoid_or_handle_carefully=["production deployment"]
)


# 4. strategy
strategy = {
    "method_used": "storyline with STAR-style evidence",
    "overall_strategy": "Position the candidate as an applied AI and data professional with strong ML pipeline evidence.",
    "opening_strategy": "Connect the candidate's applied AI interests to the role.",
    "body_paragraphs": [
        {
            "paragraph_goal": "Show technical fit",
            "evidence_to_use": ["BioVerify project", "Python", "GroundingDINO", "BioCLIP2"],
            "keywords_to_include": ["machine learning", "pipeline", "Python"],
            "tone_guidance": "Specific and confident"
        },
        {
            "paragraph_goal": "Show collaboration and communication",
            "evidence_to_use": ["Deloitte experience", "research collaboration"],
            "keywords_to_include": ["stakeholder communication", "collaboration"],
            "tone_guidance": "Warm and grounded"
        }
    ],
    "closing_strategy": "End with concise enthusiasm and readiness to contribute.",
    "must_include": ["BioVerify", "Python"],
    "avoid": ["Do not claim unsupported production deployment experience."],
    "suggested_length": "medium",
    "tone_notes": "Professional, warm, and confident."
}


draft = generate_cover_letter_draft(
    jd_analysis=jd,
    candidate_profile=candidate,
    evidence_map=evidence_map,
    strategy=strategy,
    user_instructions="Make it warm but not too long."
)

print(draft[:1500])