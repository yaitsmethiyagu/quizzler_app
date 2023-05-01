from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzUI:

    def __init__(self, question_bank: QuizBrain):
        self.quizz = question_bank
        self.window = Tk()
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.window.title("Quizz App")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Aral", 12, "normal"))
        self.canvas = Canvas(width=300, height=250, bg="white")

        self.canvas_label = self.canvas.create_text(150, 125, width=280, text="some text", font=("Arial", 18, "italic"),
                                                    fill=THEME_COLOR)
        self.true_button = Button(image=true_image,
                                  bd=0, highlightthickness=0, command=self.check_true, state="disabled")

        self.false_button = Button(image=false_image,
                                   bd=0, highlightthickness=0, command=self.check_false, state="disabled")

        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.false_button.grid(column=0, row=2)
        self.true_button.grid(column=1, row=2)
        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quizz.score}")
            question_text = self.quizz.next_question()
            self.canvas.itemconfig(self.canvas_label, text=question_text)
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.canvas.itemconfig(self.canvas_label, text="You reached end of quizz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.window.mainloop()

    def check_true(self):
        self.give_feedback(self.quizz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quizz.check_answer("False"))

    def give_feedback(self, answer: bool):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        if answer:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        self.window.after(1000, self.get_next_question)
