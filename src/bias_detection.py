import re

def anonymize(text):
    # Remove names (very basic pattern)
    text = re.sub(r'\b[A-Z][a-z]+\b', 'NAME', text)
    
    # Remove gendered words
    text = re.sub(r'\b(he|she|him|her)\b', '', text, flags=re.I)
    
    return text