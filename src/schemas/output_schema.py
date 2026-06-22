# src/schemas/output_schema.py

'''
Purpose of this file: defines the final output structure of your cover letter agent.

This file:
1. Created 5 pydantic model
    a) CoverLetterOutput
    b) KeywordCoverageItem
        keyword
        included
        supporting_evidence
        notes
    c) EvidenceUsedITem
    d) ReviewNote
    e) UnsupportedClaimItem

'''


# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from typing import List, Literal
from pydantic import BaseModel, Field


# ---------------------------------------------
# Pydantic Models
# ---------------------------------------------
class KeywordCoverageItem(BaseModel):
    keyword: str = Field(default = "Unknown", description="Keyword for the evidence")
    included: bool = Field(default=False, description="Included in the cover letter or not?")
    supporting_evidence: str = Field(default = "Unknown", description="Supporting evidence to this keyword")
    notes:str = Field(default = "Unknown", description="Details regarding the addition in the cover letter")

class EvidenceUsedItem(BaseModel):
    evidence:str = Field(default = "Unknown", description="Evidence included in the cover letter") 
    source:str = Field(default = "Unknown", description="Source material from where the material was taken from")
    where_used:str = Field(default = "Unknown", description="Gives the section where the evidence was mentioned")

class UnsupportedClaimItem(BaseModel):
    claim: str = Field(default = "Unknown", description ="claims that were reomved or avoided")
    reason_removed: str = Field(default = "Unknown", description ="reaosn why this was reomved?")
    safer_alternative: str = Field(default = "Unknown", description ="How was this replaced?")

class ReviewNote(BaseModel):
    category:str=Field(default="Unknown", description="Review category such as tone, specificity, evidence, structure, or keyword coverage.")
    note:str=Field(default="Unknown", description="Specific review note.")
    severity: Literal["low","medium","high"] = Field(default="medium", description="Severity of the issue: low, medium, or high.")

class CoverLetterOutput(BaseModel):
    cover_letter: str = Field(default="", description="Final generated cover letter.")
    role_title: str = Field(default="Unknown", description="Job role title.")
    company_name: str = Field(default="Unknown", description="Company name.")
    tone: str = Field(default="professional, warm, confident", description="Tone used in the final cover letter.")
    method_used: str = Field(default="storyline with STAR-style evidence", description="Writing method or strategy used.")
    keywords_covered: List[KeywordCoverageItem] = Field(default_factory=list, description="Keyword coverage report.")
    evidence_used: List[EvidenceUsedItem] = Field(default_factory=list, description="Candidate evidence used in the final cover letter.")
    unsupported_claims_removed: List[UnsupportedClaimItem] = Field(default_factory=list, description="Claims avoided or removed because they were not supported.")
    review_notes: List[ReviewNote] = Field(default_factory=list, description="Review notes from the critic or revision step.")
    suggestions: List[str] = Field(default_factory=list, description="Suggestions for improving the cover letter or application.")
    final_quality_score: float = Field(default=0.0, description="Optional quality score from 0 to 10.")