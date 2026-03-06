import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# 1. Connect to your specific database
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect securely
db_connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
cursor = db_connection.cursor()

# 2. The 10 AI and ML Questions 
ai_ml_questions = [
    (
        "What does 'AI' stand for?", 
        "A. Automated Intelligence", "B. Artificial Intelligence", "C. Applied Intelligence", "D. Algorithmic Integration", 
        "B"
    ),
    (
        "Which of the following is considered a subset of Machine Learning?", 
        "A. Deep Learning", "B. Cloud Computing", "C. Internet of Things", "D. Cybersecurity", 
        "A"
    ),
    (
        "In Machine Learning, what defines 'Supervised Learning'?", 
        "A. Learning without human intervention", "B. Learning from unclassified data", "C. Learning with labeled training data", "D. Learning through trial and error", 
        "C"
    ),
    (
        "What does 'NLP' stand for in the context of Artificial Intelligence?", 
        "A. Natural Language Processing", "B. Network Logic Protocol", "C. Neural Learning Process", "D. Node Location Parameter", 
        "A"
    ),
    (
        "What is the term for when a machine learning model learns the training data too well, including its noise, making it perform poorly on new data?", 
        "A. Underfitting", "B. Overfitting", "C. Hyper-tuning", "D. Data saturation", 
        "B"
    ),
    (
        "Which of these tasks is a classic example of Unsupervised Learning?", 
        "A. Predicting house prices", "B. Spam detection in emails", "C. Grouping customers based on purchasing behavior (Clustering)", "D. Recognizing handwritten digits", 
        "C"
    ),
    (
        "What is the primary purpose of an 'activation function' in an artificial neural network?", 
        "A. To store data", "B. To introduce non-linearity into the output", "C. To connect to the database", "D. To compress the model size", 
        "B"
    ),
    (
        "Reinforcement learning is primarily based on which of the following concepts?", 
        "A. Labeled datasets", "B. Rewards and punishments", "C. Decision trees", "D. Static rulesets", 
        "B"
    ),
    (
        "Which algorithm is commonly used for basic classification tasks like determining if a tumor is benign or malignant?", 
        "A. K-Means Clustering", "B. Linear Regression", "C. Logistic Regression", "D. Principal Component Analysis", 
        "C"
    ),
    (
        "What is a 'Turing Test' designed to determine?", 
        "A. The processing speed of a computer", "B. If a machine can exhibit intelligent behavior indistinguishable from a human", "C. The accuracy of a neural network", "D. How much memory an AI requires", 
        "B"
    )
]

# 3. The SQL Command to insert the data
sql = '''
    INSERT INTO questions (question_text, choice_a, choice_b, choice_c, choice_d, correct_answer)
    VALUES (%s, %s, %s, %s, %s, %s)
'''

# 4. Execute and Save
cursor.executemany(sql, ai_ml_questions)
db_connection.commit() # This line actually saves the data to the server

print(f"Success! {cursor.rowcount} AI/ML questions were inserted into your database.")

# Close the connection when done
cursor.close()
db_connection.close()