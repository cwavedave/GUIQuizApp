from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain :QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzter")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.window.minsize(width=350, height=800)
        self.window.maxsize(width=350, height=800)


        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.quiz_bg = Canvas(width=300,height=250, bg="white")
        self.question_text = self.quiz_bg.create_text(150,125,
                                                      text="Question Text",
                                                      w = 270,
                                                      fill ="black",
                                                      font=("Arial", 20, "italic"))
        self.quiz_bg.grid(column=0,row=1, columnspan=2, pady=50)

        incorrect = PhotoImage(file="./images/false.png")
        self.left_button = Button(image=incorrect, highlightthickness=0, command= self.check_false)
        self.left_button.grid(column=0,row=2)

        correct = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=correct, highlightthickness=0, command=self.check_true)
        self.right_button.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.quiz_bg.itemconfig(self.question_text, text=q_text)

    def check_true(self):
        self.quiz.check_answer("True")

    def check_false(self):
        self.quiz.check_answer("False")

    # def false(self):