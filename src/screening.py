from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resumes, job_desc):
    texts = [job_desc] + [r[1] for r in resumes]

    texts=[t.strip() for t in texts if t and t.strip()!=""]

    print("Texts being used:",texts)

    if len(texts)<2:
        print("Error: Not enough valid texts(job description or resumes missing)")
        return[]
        
    vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,2),max_features=5000)
    vectors = vectorizer.fit_transform(texts)
    
    similarity = cosine_similarity(vectors[0:1], vectors[1:])
    
    scores = list(zip([r[0] for r in resumes], similarity[0]))
    return sorted(scores, key=lambda x: x[1], reverse=True)