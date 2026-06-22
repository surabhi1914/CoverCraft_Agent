# src/schemas/evidence_schema.py

'''
Purpose of this file: This file basically would help in linking the job requriements to the candidate and help analyze what is the candidate lacking and what is the strong match

This file:
1. Created 2 pydantic model - 
    a)EvidenceMatch -
        job_requirement
        candidate_evidence
        evidence_source
        match_strength - ["strong","medium", "weak", "none"]
        skills_connected
        keywords_covered
        suggested_angle
        use_in_cover_letter
    b)EvidenceMap
        role_title
        company_name
        overall_match_summary
        strong_matches
        medium_matches
        weak_matches
        unsupported_requirements
        recommended_cover_letter_focus
        keywords_to_include
        keywords_to_avoid_or_handle_carefully
    c) UnsupportedRequirement
        job_requirement
        reason
        recommendation

'''




# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from typing import List, Literal
from pydantic import BaseModel, Field




# ---------------------------------------------
#  Pydantic models
# ---------------------------------------------

class EvidenceMatch(BaseModel):
    job_requirement: str = Field(default = "Unknown", description="Job requirements mentioned in the Job description")
    candidate_evidence: str = Field(default = "Unknown", description="candidate evidence from the source")
    skills_connected: List[str] = Field(default_factory=list, description="skills present in source that are required as per the JD")
    keywords_covered: List[str] = Field(default_factory=list, description="keywords present in the source that are required as per the JD")
    skills_connected: List[str] = Field(default_factory=list, description="skills that are required as per the JD")    
    match_strength: Literal["strong", "medium", "weak", "none"] = Field(default="none", description="Strength of the match")
    evidence_source: str = Field(default = "Unknown", description="Evidence source")
    suggested_angle: str = Field(default = "Unknown", description="Suggested angle based on the role")
    use_in_cover_letter: bool = Field(default = True, description="Whether this evidence should be used in the final cover letter.")


class UnsupportedRequirement(BaseModel):
    job_requirement: str = Field(default="Unknown", description="Job requirements mentioned in the Job description that the candidate cannot satisfy based on the source material")
    reason: str = Field(default="Unknown", description="Answer to \"Why cant the candidate satisfy? \" ")
    recommendation: str = Field(default = "Unknown", description="Answer to \" How to reduce the negative impact because of this requirement")      

class EvidenceMap(BaseModel):
    role_title: str = Field(default="Unknown",description="Job role title.")
    company_name: str = Field(default="Unknown",description="Company name.")
    overall_match_summary: str = Field(default="",description="Brief summary of how well the candidate matches the role.")
    strong_matches: List[EvidenceMatch] = Field(default_factory=list, description="Requirements strongly supported by candidate evidence.")
    medium_matches: List[EvidenceMatch] = Field(default_factory=list,description="Requirements partially or reasonably supported by candidate evidence.")
    weak_matches: List[EvidenceMatch] = Field(default_factory=list, description="Requirements weakly supported by candidate evidence.")
    unsupported_requirements: List[UnsupportedRequirement] = Field(default_factory=list, description="Requirements that the candidate cannot satisfy as per the source material")
    recommended_cover_letter_focus: List[str] = Field(default_factory=list, description="Main themes the cover letter should emphasize.")
    keywords_to_include: List[str] = Field(default_factory=list, description="Keywords that are supported and should be included naturally.")
    keywords_to_avoid_or_handle_carefully: List[str] = Field(default_factory=list, description="Keywords that should not be forced because support is weak or missing.")


