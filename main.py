from src.preprocess import load_resumes
from src.screening import rank_resumes

# Load job description
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_desc = f.read()

# Load resumes
resumes = load_resumes()

# Rank resumes
ranked = rank_resumes(resumes, job_desc)

print("\n--- Resume Rankings ---")
for name, score in ranked:
    print(f"{name}: {score:.4f}")