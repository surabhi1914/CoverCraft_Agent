# src/utils/llm_client.py

'''
Purpose of this file: Contains resuable functions or classes for calling an LLM

This file:
1. Load the API key from config
2. Create the LLM client
3. Send a prompt to the model
4. Return clean text output
5. Raise clear errors if the API key is missing
6. Keep model settings in one place

'''



# ---------------------------------------------
# Importing libraries
# ---------------------------------------------

from src.config import OPENAI_API_KEY, DEFAULT_MODEL
from openai import OpenAI


# ---------------------------------------------
# Helper Functions
# ---------------------------------------------

def validate_api_key(api_key):
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing.")
    
    
def get_openai_client():
    validate_api_key(OPENAI_API_KEY)
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client

def generate_text(prompt, model=DEFAULT_MODEL, temperature:float=0.3, max_output_tokens = 1200):
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    client = get_openai_client()
    response = client.responses.create(
        model = model,
        input = prompt,
        temperature = temperature,
        max_output_tokens=max_output_tokens
    )
    return response.output_text.strip()


