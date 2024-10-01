from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15), fg="white", bg=THEME_COLOR,
                                 pady=10)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.white = self.canvas.config(bg="white")
        self.text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill="black",
                                            width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        correct = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct, command=self.correct)
        self.correct_button.grid(row=2, column=1)
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, command=self.false)
        self.false_button.grid(row=2, column=0)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=text)
        else:
            self.canvas.itemconfig(self.text, text=f"You have completed the quiz.\nYour score is {self.quiz.score}/10")
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_question()

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(bg="white")
