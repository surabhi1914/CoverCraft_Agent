# src/utils/file_utls.py

'''
**Purpose** : This file handles basic file handling and loading

This file: 

1. load json
2. save json
3. save text
4. load text
5. create folders
6. check file existance

'''

# ---------------------------------------------
# Importing Libraries and Configuration setup
# ---------------------------------------------
from pathlib import Path
import json

# REQUIRED_FILES = ["RESUME", "additional", "profile", "sample_job_descriptions", "motivation"]

# ---------------------------------------------
# Helper Functions
# ---------------------------------------------

def ensure_directory_exists(path) -> None:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    # print(f"Directory: {path} |  directory exists: {path.exists()}")

def file_exists(path) -> bool:
    path =  Path(path)
    # print(f"File: {path} |  File exists: {path.exists()}")
    return path.exists()

# Loading the files

def load_json(path) -> dict:
    if file_exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        raise FileNotFoundError(f"{path} doesn't exist.")
    return data

def load_text(path) -> str:
    if file_exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
    else:
        raise FileNotFoundError(f"{path} doesn't exist.")
    return data

# Saving the files

def save_json(text, path):
    path =  Path(path)
    ensure_directory_exists(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(text,f, indent=2, ensure_ascii=False)
    


def save_text(text: str, path):
    path =  Path(path)
    ensure_directory_exists(path.parent)
    with open(path, "w", encoding="utf-8") as f:
            f.write(text)

