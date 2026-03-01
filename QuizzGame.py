from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty, NumericProperty
import random
from kivy.lang import Builder

# Questions
questions = [
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": "JavaScript"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def"
    },
    {
        "question": "Which language is mainly used for iOS app development?",
        "options": ["Swift", "Kotlin", "PHP", "Go"],
        "answer": "Swift"
    }
]


class WelcomeScreen(Screen):
    pass


class QuizScreen(Screen):
    question_text = StringProperty("")
    options = ListProperty([])
    score = NumericProperty(0)
    current_question = 0

    def start_quiz(self):
        random.shuffle(questions)
        self.score = 0
        self.current_question = 0
        self.load_question()

    def load_question(self):
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_text = q["question"]
            self.options = q["options"]
        else:
            self.manager.get_screen("result").final_score = self.score
            self.manager.current = "result"

    def check_answer(self, selected):
        if selected == questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.load_question()


class ResultScreen(Screen):
    final_score = NumericProperty(0)


class QuizApp(App):
    def build(self):
        return Builder.load_file("quizzgame.kv")


if __name__ == "__main__":
    QuizApp().run()