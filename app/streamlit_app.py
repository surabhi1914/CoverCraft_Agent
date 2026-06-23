# app/streamlit.py

'''
Purpose of this file: gives your project a simple UI so you can actually use the cover letter agent without running Python scripts manually.

This file:
1. Creates a simple UI
2. Upload or paste a job description
3. Choose method, tone, and length
4. Add custom instructions
5. Generate the cover letter
6. View final letter, draft, evidence map, and critic review
7. Download/save outputs

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------


# ---------------------------------------------
# Importing Libraries 
# ---------------------------------------------

from pathlib import Path
import sys

import streamlit as st


# Make src imports work when running Streamlit from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


from src.config import RAW_DATA_DIR, SUPPORTED_DOCUMENT_TYPES
from src.pipeline.run_from_files_and_save import run_from_files_and_save
from src.pipeline.run_from_files import get_candidate_files_from_raw


# ---------------------------------------------
# UI design
# ---------------------------------------------

st.set_page_config(
    page_title="CoverCraft Agent",
    page_icon="✍️",
    layout="wide",
)

st.title("✍️ CoverCraft Agent")

st.write(
    "Paste a job description, choose your writing preferences, and generate a source-grounded cover letter."
)

with st.sidebar:
    st.header("Candidate Source Files")

    st.caption("The app automatically reads supported files from `data/raw/`.")

    try:
        candidate_files = get_candidate_files_from_raw(RAW_DATA_DIR)

        st.success(f"Found {len(candidate_files)} source file(s).")

        for file_path in candidate_files:
            st.write(f"• {file_path.name}")

    except Exception as e:
        st.error(str(e))

    st.divider()

    st.caption("Do not place job descriptions inside `data/raw/`.")

    st.subheader("Pipeline Options")
    use_candidate_cache = st.checkbox(
        "Use candidate profile cache",
        value=True,
        help="Uses saved candidate profile if data/raw files have not changed.",
    )


st.subheader("Job Description")
job_description_text = st.text_area(
    label="Paste the job description here",
    height=300,
    placeholder="Paste the full job description...",
)


st.subheader("Writing Preferences")

col1, col2, col3 = st.columns(3)

with col1:
    method = st.selectbox(
        "Writing method",
        options=[
            "storyline with STAR-style evidence",
            "direct professional cover letter",
            "achievement-focused cover letter",
            "mission-alignment cover letter",
            "career-transition explanation",
        ],
        index=0,
    )

with col2:
    tone = st.selectbox(
        "Tone",
        options=[
            "professional, warm, confident",
            "concise and direct",
            "enthusiastic but not exaggerated",
            "polished and formal",
            "human, natural, and sincere",
        ],
        index=0,
    )

with col3:
    length = st.selectbox(
        "Length",
        options=[
            "short",
            "medium",
            "detailed",
        ],
        index=1,
    )


user_instructions = st.text_area(
    label="Custom instructions",
    height=120,
    placeholder="Example: Make it warm, specific, not too formal, and highlight my ML projects.",
)


generate_button = st.button("Generate Cover Letter", type="primary")


if generate_button:
    if not job_description_text.strip():
        st.error("Please paste a job description first.")

    else:
        try:
            with st.spinner("Generating cover letter..."):
                output = run_from_files_and_save(
                    job_description_text=job_description_text,
                    method=method,
                    tone=tone,
                    length=length,
                    user_instructions=user_instructions,
                    use_candidate_cache=use_candidate_cache,
                )
                

            result = output["result"]
            metadata = result.get("metadata", {})

            st.info(
                f"Candidate cache used: {metadata.get('used_candidate_cache')} | "
            )
            saved_paths = output["saved_paths"]

            st.success("Cover letter generated successfully.")

            st.subheader("Final Cover Letter")

            final_letter = result.get("final_letter", "")

            st.text_area(
                label="Generated cover letter",
                value=final_letter,
                height=500,
            )

            st.download_button(
                label="Download Final Cover Letter",
                data=final_letter,
                file_name="final_cover_letter.md",
                mime="text/markdown",
            )

            with st.expander("View Draft"):
                st.write(result.get("draft", ""))

            with st.expander("View JD Analysis"):
                st.json(result.get("jd_analysis", {}))

            with st.expander("View Evidence Map"):
                st.json(result.get("evidence_map", {}))

            with st.expander("View Critic Review"):
                st.json(result.get("critic_review", {}))

            with st.expander("Saved Output Paths"):
                st.json(saved_paths)

        except Exception as e:
            st.error("Something went wrong while generating the cover letter.")
            st.exception(e)

