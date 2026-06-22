# src/schemas/candidate_schema.py

'''
Purpose of this file: Tells the project what a "candidate profile" should look like after we analyze source documents

This file:
1. Created pydantic model:
    a) Candidate Profile
    b) Experience Item
    c)Education item
    d) Achievements
    e)Project Item 

'''


# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
from typing import List
from pydantic import BaseModel, Field

# ---------------------------------------------
# Pydantic Model
# ---------------------------------------------


class EducationItem(BaseModel):
    institution: str = Field(default="", description="Name of the school, university, or institution.")
    degree: str = Field(default="", description="Degree or credential earned.")
    field_of_study: str = Field(default="", description="Major, concentration, or area of study.")
    start_date: str = Field(default="", description="Start date if available.")
    end_date: str = Field(default="", description="End date or expected graduation date if available.")
    grade: str = Field(default="", description="Grade or GPA if available.")
    details: List[str] = Field(default_factory=list, description="Relevant coursework, honors, or education details.")

class ExperienceItem(BaseModel):
    role_title: str = Field(default="", description="Job title.")
    organization: str = Field(default="", description="Company, lab, nonprofit, or organization name.")
    start_date: str = Field(default="", description="Start date if available.")
    end_date: str = Field(default="", description="End date if available.")
    location: str = Field(default="", description="Location of the role if available.")
    responsibilities: List[str] = Field(default_factory=list, description="Responsibilities for the role.")
    achievements: List[str] = Field(default_factory=list, description="Achievements from this role.")
    skills_used: List[str] = Field(default_factory=list, description="Skills used in this role.")


class ProjectItem(BaseModel):
    project_name: str = Field(default="", description="Project name.")
    project_summary: str = Field(default="", description="Short project description.")
    tools_used: List[str] = Field(default_factory=list, description="Tools used.")
    methods_used: List[str] = Field(default_factory=list, description="Methods used for this project.")
    outcomes: List[str] = Field(default_factory=list, description="Outcomes from this project.")
    relevance_tags: List[str] = Field(default_factory=list, description="Keywords for this project.")

class AchievementItem(BaseModel):
    title: str = Field(default="", description="Achievement title.")
    category: str = Field(default="", description="Category of achievement.")
    description: str = Field(default="", description="Additional details.")



class CandidateProfile(BaseModel):
    name: str = Field(
        default="",
        description="Candidate's full name."
    )

    headline: str = Field(
        default="",
        description="Short professional headline."
    )

    target_roles: List[str] = Field(
        default_factory=list,
        description="Roles the candidate is targeting."
    )

    education: List[EducationItem] = Field(
        default_factory=list,
        description="Education history."
    )

    experience: List[ExperienceItem] = Field(
        default_factory=list,
        description="Professional, research, internship, or volunteer experience."
    )
    projects: List[ProjectItem] = Field(
        default_factory=list,
        description="Technical, academic, research, or portfolio projects."
    )

    technical_skills: List[str] = Field(
        default_factory=list,
        description="Technical skills, tools, programming languages, and platforms."
    )

    soft_skills: List[str] = Field(
        default_factory=list,
        description="Communication, collaboration, leadership, and other soft skills."
    )

    certifications: List[str] = Field(
        default_factory=list,
        description="Certifications or training programs."
    )

    publications: List[str] = Field(
        default_factory=list,
        description="Publications, papers, submissions, or research outputs."
    )

    achievements: List[AchievementItem] = Field(
        default_factory=list,
        description="Awards, recognitions, metrics, or notable accomplishments."
    )
    work_authorization: str = Field(
        default="",
        description="Work authorization information if the candidate wants to include it."
    )

    location_preferences: str = Field(
        default="",
        description="Location, remote, relocation, or work arrangement preferences."
    )

    career_summary: str = Field(
        default="",
        description="Brief summary of the candidate's background and career direction."
    )


