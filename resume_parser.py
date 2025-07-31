# resume_parser.py

import docx2txt
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Name not found"

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else "Email not found"

def extract_phone(text):
    match = re.search(r"(\+91[\-\s]?)?[0]?[789]\d{9}", text)
    return match.group() if match else "Phone number not found"

def extract_skills(text):
    # You can add more to this set
    skill_keywords = {"python", "java", "html", "css", "javascript", "sql", "c++", "excel", "flask", "django"}
    text = text.lower()
    found_skills = set()
    for skill in skill_keywords:
        if skill in text:
            found_skills.add(skill)
    return list(found_skills)
