from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Use TF-IDF for lightweight, Sentence-BERT for semantic matching
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(job_description, resume_texts):
    # Sentence-BERT embeddings
    job_embedding = model.encode(job_description)
    resume_embeddings = model.encode(resume_texts)
    scores = cosine_similarity([job_embedding], resume_embeddings)[0]
    return scores
