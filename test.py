from src.schemas.evidence_schema import EvidenceMap, EvidenceMatch, UnsupportedRequirement

match = EvidenceMatch(
    job_requirement="Experience with machine learning pipelines",
    candidate_evidence="Built BioVerify using LLaMA 3, GroundingDINO, and BioCLIP2.",
    evidence_source="BioVerify project",
    match_strength="strong",
    skills_connected=["Python", "machine learning", "computer vision"],
    keywords_covered=["machine learning", "pipeline"],
    suggested_angle="Use BioVerify as the strongest technical example."
)

gap = UnsupportedRequirement(
    job_requirement="5+ years of production ML experience",
    reason="Candidate source material does not clearly show 5+ years of production ML experience.",
    recommendation="Do not claim 5+ years. Emphasize graduate research and applied ML projects instead."
)

evidence_map = EvidenceMap(
    role_title="Machine Learning Engineer",
    company_name="Example Company",
    overall_match_summary="Strong fit for applied ML and research-oriented pipeline work.",
    strong_matches=[match],
    unsupported_requirements=[gap],
    recommended_cover_letter_focus=[
        "Applied machine learning projects",
        "Research experience",
        "Python-based pipeline development"
    ],
    keywords_to_include=["Python", "machine learning", "pipeline"],
    keywords_to_avoid_or_handle_carefully=["5+ years"]
)

print(evidence_map.model_dump())