# src/utils/text_cleaning.py

'''
Purpose of this file: General text cleaning and normalization for resume text, job description and user instructions

In this project, many inputs will be messy:
- Resume text copied from PDF
- Job description pasted from website
- Extra notes written by user
- Keyword lists
- Cover letter drafts


This file provides functions  for:
1. Normalizing whitespace
2. Remove excessive blank lines
3. Clean bullet characters gently
4. Convert keyword strings into clean lists
5. remove very pobvious noise
6. Prepare text for llm input

'''


# Template
# ---------------------------------------------
# 
# ---------------------------------------------

# ---------------------------------------------
# Importing libraries and setup configuration
# ---------------------------------------------
import re

# ---------------------------------------------
# Helper Functions
# ---------------------------------------------

# normalize the whitespace
def normalize_whitespace(text) -> str:
    if not text:
        return ""
    text = re.sub(r"[ \t]+", " ", text)
    return text


# Remove any excessive new lines with no text
def remove_excess_blank_lines(text) ->str:
    if not text:
        return ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

# normalize different types of bullets into -
def clean_bullets(text) ->str:
    text = re.sub(r'^\s*([^\w\s]+|\d+[\.\)]|[a-zA-Z][\.\)])\s+', '-', text, flags=re.MULTILINE)
    return text

# Split the keywords and remove repetative keywords in the list
def split_keywords(keywords) -> list[str]:
    if not keywords:
        return []
    
    keywords = keywords.replace("\n", ",")
    keywords_list = keywords.split(",")

    cleaned_keywords = []
    seen = set()

    for word in keywords_list:
        word = word.strip()
        if word and word.lower() not in seen:
            cleaned_keywords.append(word)
            seen.add(word.lower())

    return cleaned_keywords


# 
def prepare_text_for_llm(text) ->str:
    
    text = clean_bullets(text)
    text = normalize_whitespace(text)
    text = remove_excess_blank_lines(text)
    
    
    return text.strip()