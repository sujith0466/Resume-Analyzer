import docx2txt
from pdfminer.high_level import extract_text
import json
import re

# Load target keywords
with open("target_keywords.json") as f:
    target_keywords = json.load(f)

def extract_text_from_file(path):
    if path.endswith(".pdf"):
        return extract_text(path)
    elif path.endswith(".docx"):
        return docx2txt.process(path)
    else:
        return ""

def analyze_resume(file_path):
    text = extract_text_from_file(file_path).lower()

    # Simple keyword matching
    found = []
    missing = []
    for keyword in target_keywords["keywords"]:
        if keyword.lower() in text:
            found.append(keyword)
        else:
            missing.append(keyword)

    score = round((len(found) / len(target_keywords["keywords"])) * 100)

    suggestions = []
    if score < 70:
        suggestions.append("Consider adding more job-specific keywords.")
    if "experience" not in text:
        suggestions.append("Mention your experience section clearly.")
    if len(text.split()) < 150:
        suggestions.append("Try to elaborate more on your skills and projects.")

    return {
        "score": score,
        "found": found,
        "missing": missing,
        "suggestions": suggestions
    }
