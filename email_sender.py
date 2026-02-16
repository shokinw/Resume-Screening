import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, candidate, score):
    subject = "Congratulations! Shortlisted for Next Round"
    body = f"""
    Dear {candidate},

    Congratulations! Your resume achieved a {round(score*100,2)}% match for the job description.

    Our HR team will contact you shortly.

    Best Regards,
    Recruitment Team
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to_email, msg.as_string())
    server.quit()
