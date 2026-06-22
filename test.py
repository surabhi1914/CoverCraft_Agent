from src.agents.jd_analyzer import analyze_job_description

sample_jd = """
We are hiring a Data Analyst to work with SQL, Python, dashboards,
stakeholders, and product teams. The role requires strong communication
and experience turning data into insights.
"""

result = analyze_job_description(sample_jd)

print(result.model_dump())