import os
from parser import extract_text_from_pdf, extract_email
from matcher import calculate_similarity
from database import insert_candidate
from email_sender import send_email

resumes_folder = "resumes/"
job_description = open("job_description.txt").read()

resume_texts, names, emails = [], [], []

for file in os.listdir(resumes_folder):
    if file.endswith(".pdf"):
        path = os.path.join(resumes_folder, file)
        text = extract_text_from_pdf(path)
        resume_texts.append(text)
        names.append(file)
        emails.append(extract_email(text) or "hr@example.com")

scores = calculate_similarity(job_description, resume_texts)

for name, email, score in zip(names, emails, scores):
    if score >= 0.6:
        insert_candidate(name, email, score)
        send_email(email, name, score)
