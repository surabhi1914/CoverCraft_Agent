from src.schemas.candidate_schema import CandidateProfile, ProjectItem

bioverify = ProjectItem(
    project_name="BioVerify",
    project_summary="Built a species verification pipeline for iNaturalist predator-prey images.",
    tools_used=["Python", "LLaMA 3", "GroundingDINO", "BioCLIP2"],
    outcomes=["Improved species-level accuracy from 54.98% to 71.93%"],
    relevance_tags=["machine learning", "computer vision", "AI pipeline"]
)

profile = CandidateProfile(
    name="Surabhi Nair",
    headline="Machine learning and data science graduate",
    target_roles=["Applied AI Engineer", "Data Scientist", "ML Engineer"],
    projects=[bioverify],
    technical_skills=["Python", "SQL", "Neo4j", "PyTorch"]
)

print(profile)
print(profile.model_dump())