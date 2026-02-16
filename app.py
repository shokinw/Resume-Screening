import streamlit as st
import pandas as pd
from parser import extract_text_from_pdf, extract_email
from matcher import calculate_similarity
from database import insert_candidate
from email_sender import send_email
import os

st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("AI Resume Screening + Email Automation")

job_description = st.text_area("Paste Job Description")
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)
threshold = st.slider("Shortlisting Threshold (%)", 0, 100, 60)

if st.button("Start Screening"):
    if uploaded_files and job_description:
        resume_texts, names, emails = [], [], []
        for file in uploaded_files:
            path = os.path.join("resumes", file.name)
            with open(path, "wb") as f:
                f.write(file.getbuffer())
            text = extract_text_from_pdf(path)
            resume_texts.append(text)
            names.append(file.name)
            emails.append(extract_email(text) or "hr@example.com")

        scores = calculate_similarity(job_description, resume_texts)
        df = pd.DataFrame({"Candidate": names, "Email": emails, "Score": scores}).sort_values(by="Score", ascending=False)
        st.subheader("Candidate Ranking")
        st.dataframe(df)

        shortlisted = df[df["Score"] >= threshold/100]
        if st.button("Send Emails"):
            for _, row in shortlisted.iterrows():
                insert_candidate(row["Candidate"], row["Email"], row["Score"])
                send_email(row["Email"], row["Candidate"], row["Score"])
            st.success(f"Emails sent to {len(shortlisted)} candidates!")
    else:
        st.warning("Please upload resumes and paste a job description.")
