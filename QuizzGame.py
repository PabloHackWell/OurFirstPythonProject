import mysql.connector

# --- 1. The Question Blueprint ---
class Question:
    def __init__(self, text, choices, correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

# --- 2. The QuizBrain Blueprint ---
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = None
    

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_question

    def check_answer(self, user_guess):
        correct_answer = self.current_question.correct_answer
        if user_guess.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

# --- 3. The Database Loader ---
def load_questions_from_mysql(chosen_difficulty):
    db_connection = mysql.connector.connect(
      host="localhost", user="root", password="yourpasswd", database="quiz_game"
    )
    cursor = db_connection.cursor()
    
    query = "SELECT * FROM questions WHERE difficulty = %s ORDER BY RAND() LIMIT 10"
    cursor.execute(query, (chosen_difficulty,))
    rows = cursor.fetchall()
    
    question_bank = []
    for row in rows:
        text, choices, answer = row[1], [row[2], row[3], row[4], row[5]], row[6]
        question_bank.append(Question(text, choices, answer))
        
    return question_bank
        
import tkinter as tk
from tkinter import messagebox

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        
        self.window = tk.Tk()
        self.window.title("Advanced AI/ML Quiz")
        self.window.geometry("500x650") 
        self.window.config(padx=20, pady=20, bg="#2b2b2b") 
        
        self.score_label = tk.Label(text="Score: 0", fg="white", bg="#2b2b2b", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)
        
       
        self.timer_label = tk.Label(text="Time Left: 15", fg="#FFEB3B", bg="#2b2b2b", font=("Arial", 14, "bold"))
        self.timer_label.pack()
        
        self.time_left = 15
        self.timer_id = None 
        
        self.canvas = tk.Canvas(width=400, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200, 125, width=380, text="Question goes here", 
            fill="#2b2b2b", font=("Arial", 16, "italic")
        )
        self.canvas.pack(pady=20)
        
        self.buttons = []
        for i in range(4):
            btn = tk.Button(text="", font=("Arial", 12), width=35, height=2, 
                            command=lambda idx=i: self.button_clicked(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)
            
        self.get_next_question()
        self.window.mainloop()

    # --- TIMER LOGIC ---
    def start_timer(self):
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left}")
            self.time_left -= 1
            self.timer_id = self.window.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's Up!")
            self.mark_wrong_and_continue()

    def mark_wrong_and_continue(self):
        for btn in self.buttons:
            btn.config(state="disabled")
        self.window.after(1000, self.get_next_question)

    # --- GAME FLOW LOGIC ---
    def get_next_question(self):
        for btn in self.buttons:
            btn.config(bg="SystemButtonFace", fg="black", state="normal")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number}")
            
            q_data = self.quiz.get_next_question()
            self.canvas.itemconfig(self.question_text, text=q_data.text)
            
            for i in range(4):
                self.buttons[i].config(text=q_data.choices[i])
                
            if self.timer_id:
                self.window.after_cancel(self.timer_id) 
            self.start_timer()
            
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over! You've completed the quiz.")
            for btn in self.buttons:
                btn.config(state="disabled")
            if self.timer_id:
                self.window.after_cancel(self.timer_id)
            messagebox.showinfo("Finished", f"Your final score is {self.quiz.score}/{self.quiz.question_number}")

    def button_clicked(self, button_index):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)

        letters = ["A", "B", "C", "D"]
        user_guess = letters[button_index]
        is_right = self.quiz.check_answer(user_guess)
        
        if is_right:
            self.buttons[button_index].config(bg="#4CAF50", fg="white")
        else:
            self.buttons[button_index].config(bg="#F44336", fg="white")
            
        for btn in self.buttons:
            btn.config(state="disabled")
            
        self.window.after(1000, self.get_next_question)


# ==========================================
# --- 4. RUNNING THE ACTUAL GAME ---
# ==========================================

print("Loading questions from database...")

my_questions = load_questions_from_mysql("Medium")
quiz = QuizBrain(my_questions)
quiz_ui = QuizInterface(quiz)
print("--- GAME OVER ---")
print(f"Your final score is: {quiz.score} out of {quiz.question_number}")
