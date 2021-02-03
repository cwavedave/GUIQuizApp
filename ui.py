from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzter")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.window.minsize(width=350, height=800)
        self.window.maxsize(width=350, height=800)


        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.quiz_bg = Canvas(width=300,height=250, bg="white")
        self.question_text = self.quiz_bg.create_text(150,125,
                                                      text="Question Text",
                                                      fill ="black",
                                                      font=("Arial", 20, "italic"))
        self.quiz_bg.grid(column=0,row=1, columnspan=2, pady=50)

        incorrect = PhotoImage(file="./images/false.png")
        self.left_button = Button(image=incorrect, highlightthickness=0)
        self.left_button.grid(column=0,row=2)

        correct = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=correct, highlightthickness=0)
        self.right_button.grid(column=1,row=2)

        self.window.mainloop()
