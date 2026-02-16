import sqlite3

conn = sqlite3.connect("candidates.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
    name TEXT,
    email TEXT,
    score REAL
)
""")

def insert_candidate(name, email, score):
    cursor.execute("INSERT INTO candidates VALUES (?, ?, ?)", (name, email, score))
    conn.commit()

def get_all_candidates():
    cursor.execute("SELECT * FROM candidates ORDER BY score DESC")
    return cursor.fetchall()
