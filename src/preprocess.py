import pdfplumber
import os

def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + ""

    return text

def load_resumes(folder_path="data/resumes"):
    resumes = {}

    for file in os.listdir(folder_path):

        path = os.path.join(folder_path, file)

        # TXT FILES
        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                resumes[file] = f.read()

        # PDF FILES
        elif file.endswith(".pdf"):
            resumes[file] = read_pdf(path)

    return resumes