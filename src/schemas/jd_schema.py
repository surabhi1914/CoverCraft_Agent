# src/schemas/jd_schema.py

'''
Purpose of this file: defines the structure for a parsed job description.

This file:

1. Validate data models
Pydantic model - A class that ensures incoming data matches the expected types and structure.
2. Expected output format:
{
    "company_name": "Google",
    "role_title": "Data Scientist Intern",
    "core_responsibilities": [...],
    "required_skills": [...],
    "preferred_skills": [...],
    "keywords": [...],
    "soft_skills": [...],
    "role_summary": "...",
    "candidate_focus_areas": [...]
}
'''



# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from pydantic import BaseModel, Field
from typing import List

# ---------------------------------------------
#  Defining the pydantic model
# ---------------------------------------------

class JobDescriptionAnalysis(BaseModel):
    
    company_name: str = Field(
        default = "Unknown",
        description = "Name of the company hiring for the role"
    )
    role_title: str = Field(
        default = "Unknown",
        description = "Title of the job role"
    )
    core_responsibilities: str = Field(
        default = "Unknown",
        description = "Main responsibilities of the job role"
    )
    employment_type: str = Field(
        default="Unknown",
        description="Employment type such as internship, full-time, part-time, contract, or unknown."
    )
    location: str = Field(
        default="Unknown",
        description="Location of the role, remote status, or Unknown."
    )

    role_summary: str = Field(
        default="",
        description="Brief summary of the role in 1-2 sentences."
    )
    required_skills: List[str] = Field(
        default_factory=list,
        description="Skills or qualifications that appear required."
    )

    preferred_skills: List[str] = Field(
        default_factory=list,
        description="Nice-to-have or preferred skills."
    )

    technical_keywords: List[str] = Field(
        default_factory=list,
        description="Technical keywords useful for ATS and cover letter alignment."
    )

    soft_skills: List[str] = Field(
        default_factory=list,
        description="Soft skills or behavioral qualities requested in the job description."
    )

    company_values: List[str] = Field(
        default_factory=list,
        description="Company values, mission phrases, or cultural signals from the job description."
    )

    candidate_focus_areas: List[str] = Field(
        default_factory=list,
        description="Areas of the candidate profile that should be emphasized in the cover letter."
    )
    red_flags_or_gaps: List[str] = Field(
        default_factory=list,
        description="Potential concerns, missing requirements, or areas needing careful handling."
    )