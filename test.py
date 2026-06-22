from src.agents.candidate_builder import build_candidate_profile

candidate_text = """
Surabhi Nair is a Master of Computer Science graduate from North Carolina State University.
She worked on BioVerify, a species verification pipeline using LLaMA 3, GroundingDINO, and BioCLIP2.
The project improved species-level accuracy from 54.98% to 71.93%.
Skills include Python, SQL, Neo4j, PyTorch, TensorFlow, and data analytics.
"""

profile = build_candidate_profile(candidate_text)

print(profile.model_dump())