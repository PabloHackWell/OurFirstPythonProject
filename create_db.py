import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")

# Insert sample data
cursor.execute("""
INSERT INTO questions 
(question, option1, option2, option3, option4, answer)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Which language is used for web?",
    "Python", "C++", "JavaScript", "Java",
    "JavaScript"
))

conn.commit()
conn.close()

print("Database Created Successfully")