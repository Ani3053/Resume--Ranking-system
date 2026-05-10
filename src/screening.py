from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(resumes, job_desc):

    resume_names = list(resumes.keys())
    resume_texts = list(resumes.values())

    documents = [job_desc] + resume_texts

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    results = list(zip(resume_names, similarity))

    return results