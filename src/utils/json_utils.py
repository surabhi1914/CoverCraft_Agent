# src/utils/json.py

'''
Purpose of this file:handles JSON extraction from LLM responses.

This file:
1. Accept the draft cover letter
2. Accept JD analysis
3. Accept candidate profile
4. Accept evidence map
5. Accept strategy
6. Build a review prompt
7. Ask the LLM to return structured JSON feedback
8. Parse JSON response
9. Return a dictionary

'''




# ---------------------------------------------
# Importing Libraries
# ---------------------------------------------
import json


# ---------------------------------------------
# Functions
# ---------------------------------------------

def extract_json_from_response(response_text: str) -> dict:
    if not response_text or not response_text.strip():
        raise ValueError("LLM response is empty.")

    cleaned = strip_json_code_fence(response_text)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")

        if start == -1 or end == -1 or end <= start:
            raise ValueError("No valid JSON object found in LLM response.")

        json_text = cleaned[start:end + 1]

        try:
            return json.loads(json_text)
        except json.JSONDecodeError as e:
            print("---- CLEANED RESPONSE START ----")
            print(cleaned)
            print("---- CLEANED RESPONSE END ----")
            raise ValueError(f"Failed to parse JSON from LLM response: {e}")


def strip_json_code_fence(response_text: str) -> str:
    if not response_text:
        return ""

    cleaned = response_text.strip()
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")

    return cleaned.strip()