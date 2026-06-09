# CoverCraft Agent

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-In%26Progress-lightgrey)](#development-roadmap)

An AI-powered cover letter generation agent designed to create personalized, evidence-backed cover letters through a multi-agent pipeline.

## Problem Statement

Writing a strong cover letter is time-consuming because each role requires a different emphasis. Candidates often need to interpret job descriptions, connect requirements to resume evidence, include the right keywords, and choose a writing strategy that sounds authentic rather than generic.

## Proposed Solution

CoverCraft Agent will help turn job descriptions, resumes or CVs, additional user notes, writing strategies, keywords, and supporting documents into tailored cover letters. The project is planned as a multi-agent pipeline where each agent handles a focused step: analyzing the job description, extracting candidate evidence, planning a strategy, drafting, critiquing, and rewriting the final letter.

## Tech Stack

- Python
- OpenAI API
- Pydantic
- Streamlit
- pypdf
- python-docx
- python-dotenv
- pytest
- Ruff

## Key Features Planned

- Parse resumes, CVs, job descriptions, and supporting documents.
- Extract role requirements, responsibilities, keywords, and hiring signals.
- Match candidate experience to job requirements using evidence-based reasoning.
- Support writing strategies such as the STAR method, storytelling, and achievement-first framing.
- Generate personalized cover letter drafts.
- Critique drafts for relevance, tone, clarity, and evidence strength.
- Rewrite final outputs into polished, ready-to-edit cover letters.
- Provide a future Streamlit interface for uploading documents and configuring preferences.

## Expected Outcome

The finished project should produce cover letters that are specific to the target role, grounded in candidate evidence, aligned with the job description, and written in a clear professional voice.

## Project Structure

```text
CoverCraft_Agent/
  requirements.txt
  .env.example
  README.md
  .gitignore
  LICENSE

  src/
    config.py

    utils/
      text_cleaning.py
      file_utils.py
      llm_client.py

    parsers/
      document_parser.py
      resume_parser.py
      jd_parser.py

    schemas/
      candidate_schema.py
      jd_schema.py
      evidence_schema.py
      output_schema.py

    agents/
      jd_analyzer.py
      evidence_matcher.py
      strategy_planner.py
      draft_generator.py
      critic.py
      final_rewriter.py

    pipeline/
      run_cover_letter_pipeline.py

  app/
    streamlit_app.py
```

## Set Up Locally

Clone or download the project, then move into the project folder:

```bash
cd CoverCraft_Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Copy the example environment file:

```bash
cp .env.example .env
```

Then update `.env` with your local API keys and model settings.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Future Streamlit App

The Streamlit app file is intentionally empty in this initial skeleton. When the app is implemented, run it with:

```bash
streamlit run app/streamlit_app.py
```

## Development Roadmap

1. Define Pydantic schemas for candidate profiles, job descriptions, evidence, and cover letter outputs.
2. Build document parsing utilities for PDF, DOCX, and plain text inputs.
3. Implement job description analysis and keyword extraction.
4. Add resume and evidence matching logic.
5. Create strategy planning support for STAR, storytelling, and keyword-focused drafts.
6. Implement draft generation, critique, and final rewriting agents.
7. Connect the full cover letter pipeline.
8. Build the Streamlit user interface.
9. Add tests, linting, and example workflows.

## Contributing

Contributions are welcome once the core implementation begins. Please keep changes focused, document important decisions, and add tests for behavior that affects parsing, schema validation, agent outputs, or pipeline orchestration.

Recommended local checks:

```bash
ruff check .
pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Created By

Created by Surabhi Nair
