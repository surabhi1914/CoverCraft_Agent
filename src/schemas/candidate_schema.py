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
from datetime import date

# ---------------------------------------------
# Pydantic Model
# ---------------------------------------------


class EducationItem(BaseModel):
    institution: str = Field(
        default= "Unknown",
        description="Name of the university"

    )
    degree: str = Field(
        default= "Unknown",
        description="Name of the degree achieved"

    )
    field_of_study: str = Field(
        default= "Computer Science", #if you are not doing computer science, you can change it. Since this is for my use, I am populating it as CS
        description="Name of the field of study"

    )
    start_date: date = Field(
        default= date(2000, 8, 1), # random start date.
        description="Start date of the program"

    )
    end_date: date = Field(
        default= date(2000, 5, 1), # random end date.
        description="End date of the program"

    )
    grade: float = Field(
        default = 4,
        description = "Grade I achieved in this program"
    )

    details: List[str] = Field(
        default= ["Unknown"],
        description="Details regarding the program like coursework etc"
    )


class ExperienceItem(BaseModel):
    role_title: str = Field(default="Unknown", description="Job title")
    organization: str = Field(default="Unknown", description="Company name")
    start_date: date = Field(default= date(2021,8,16), description = "Start date of the job")
    end_date: date = Field(default=date(2021,8,16), description="End date of the job")
    location: str = Field(default="Unknown", description="Location of the job")
    responsibilities: List[str] = Field(default_factory=list, description="responsibilities for the role")
    achievements: List[str] = Field(default_factory=list, description="achievements")
    skills_used: List[str] = Field(default_factory=list, description="skills I gained in this role")


class ProjectItem(BaseModel):
    project_name: str = Field(default="Unknown", description="Project name")
    project_summary: str = Field(default="Unknown", description="Short description")
    tools_used: List[str] = Field(default_factory=list, description="Tools used")
    method_used: List[str] = Field(default_factory=list, description="Method used for this project")
    outcomes: List[str] = Field(default_factory=list, description="Outcomes from this project")
    relevance_tags: List[str] = Field(default_factory=list, description="Keywords for this project")

class AchievementItem(BaseModel):
    title: str = Field(default="", description="Achievement title")
    category: str = Field(default="Unknown", description="Category of achievement")
    description: List[str] = Field(default_factory=list, description="Additional details")



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


