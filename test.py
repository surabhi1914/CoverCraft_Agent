from src.utils.text_cleaning import prepare_text_for_llm, split_keywords

messy_text = """
• Built BioVerify      using Python



● Improved accuracy from 54.98% to 71.93%
"""

cleaned = prepare_text_for_llm(messy_text)
print(cleaned)

keywords = split_keywords("Python, SQL\nNeo4j, Power BI, Python")
print(keywords)