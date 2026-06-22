from src.schemas.output_schema import (
    CoverLetterOutput,
    KeywordCoverageItem,
    EvidenceUsedItem,
)

keyword = KeywordCoverageItem(
    keyword="machine learning",
    included=True,
    supporting_evidence="BioVerify used LLaMA 3, GroundingDINO, and BioCLIP2.",
    notes="Included in the technical evidence paragraph."
)

evidence = EvidenceUsedItem(
    evidence="Improved species-level accuracy from 54.98% to 71.93%.",
    source="BioVerify project",
    where_used="Second paragraph"
)

output = CoverLetterOutput(
    cover_letter="Dear Hiring Manager...",
    role_title="Machine Learning Engineer",
    company_name="Example Company",
    keywords_covered=[keyword],
    evidence_used=[evidence],
    final_quality_score=8.5
)

print(output.model_dump())