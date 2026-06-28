import pdfplumber

COMMON_SKILLS = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "machine learning",
    "tensorflow",
    "pandas",
    "numpy",
    "statistics"
]

def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:
            text += page.extract_text() or ""

    return text.lower()


def extract_skills(text):

    found_skills = []

    for skill in COMMON_SKILLS:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))