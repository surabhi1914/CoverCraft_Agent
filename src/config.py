# src/config.py

'''
**Purpose** : This file keeps the important project settings


'''
# ---------------------------------------------
# Importing libraries
# ---------------------------------------------

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------
# Configurations setup
# ---------------------------------------------

#Project root path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

#Data folder paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Output folder path
OUTPUT_DIR = DATA_DIR / "outputs"


#Prompt Folder  paths
PROMPTS_DIR = PROJECT_ROOT / "prompts"

# Default model name
DEFAULT_MODEL = "gpt-4.1-mini"
DEFAULT_TONE = "professional, warm, confident"
DEFAULT_METHOD = "storyline with STAR-style evidence"
DEFAULT_LENGTH = "medium"

#Default cover letter settings

# Supported file types
SUPPORTED_DOCUMENT_TYPES = {".md", ".txt", ".docx", ".pdf"}

# API keys from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")