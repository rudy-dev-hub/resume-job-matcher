import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

# Optional: common skills to match against
COMMON_SKILLS = [
    "python", "sql", "docker", "tensorflow", "scikit-learn",
    "pytorch", "java", "c++", "ros", "linux", "git", "react",
    "node.js", "pandas", "numpy", "langchain", "llamaindex"
]

def parse_resume(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "".join([page.extract_text() or "" for page in pdf.pages])

    doc = nlp(text.lower())

    # Token-based match with common skill list
    found_skills = set()
    for token in doc:
        if token.text in COMMON_SKILLS:
            found_skills.add(token.text)

    return {
        "raw": text,
        "skills": sorted(list(found_skills))
    }
