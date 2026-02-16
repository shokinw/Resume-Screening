Recruiters often spend hours manually reviewing resumes to find suitable candidates. This project solves that problem by introducing an AI-based screening system that evaluates resumes based on skill relevance and job requirements.

The system extracts information from resumes, compares it with the job description using NLP techniques, calculates a matching score, and automatically shortlists candidates. Shortlisted applicants can then receive automated emails without manual intervention.

The project also includes a Streamlit dashboard that allows HR teams to visualize candidate rankings and manage the screening process easily.


The main goals of this project are:
Automate resume screening and candidate shortlisting
Reduce manual HR effort using AI-based matching
Improve hiring efficiency and consistency
Demonstrate real-world AI + Automation integration
Build an industry-level project suitable for placements


The workflow of the system is as follows:
HR uploads resumes or resumes are received automatically.
The system extracts text from PDF resumes.
Resume content is compared with the job description.
A similarity score is calculated using NLP techniques.
Candidates are ranked based on their scores.
Candidates above a defined threshold are shortlisted.
Automated emails are sent to shortlisted candidates.
Results are stored in the database and displayed in the dashboard.

Tech Stack
Python
Natural Language Processing (NLP)
TF-IDF & Sentence Transformers
Scikit-learn
Pandas
Streamlit
SMTP (Email Automation)
SQLite Database
n8n / Automation Anywhere (Workflow Automation)
