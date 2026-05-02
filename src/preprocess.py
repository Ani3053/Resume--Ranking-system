import pytesseract
from PIL import Image
import os
import fitz  # PyMuPDF

def extract_pdf_text(path):
    text = ""

    try:
        doc = fitz.open(path)
        for page in doc:
            text += page.get_text("text")
            
        text = text.encode("utf-8", "ignore").decode("utf-8")
        text = text.replace("\x88", " ")  # remove junk char
        text = re.sub(r'\\x[0-9a-fA-F]+', ' ', text)  # remove hex noise
        text = text.replace("\n", " ")
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
    except Exception as e:
        print(f"Error reading {path}: {e}")

    return text.lower()

def load_resumes():
    resumes = []
    folder = "data/resumes"

    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)

        if file.endswith(".txt"):
            with open(full_path, "r", encoding="utf-8") as f:
                text = f.read()

        elif file.endswith(".pdf"):
            text = extract_pdf_text(full_path)

        else:
            continue

        if text and text.strip():
            resumes.append((file, text))
        else:
            print(f"{file} is empty or unreadable")

    return resumes