from tkinter import *
from quiz_brain import QuizBrain

FONT_NAME = "Courier"
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.q_text = []
        self.window = Tk()
        self.window.title("QuizLab")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg="red")
        self.score_label.grid(column = 0, row = 0)
        self.canvas = Canvas(self.window, width=300, height=250, highlightthickness=0, bg= "white")
        self.question_text= self.canvas.create_text(150, 125, width=290,
                                                   text="Question Text",
                                                   fill="blue",
                                                   font=("Arial", 20, "italic"))  # Using defined font

        self.canvas.grid(column=0, row=1, columnspan = 3,pady=50)
        self.score_label.grid(row=0, column=2)
        true_image = PhotoImage("/home/bode/Documents/python_langage/day_34/quizzlab/true.png")
        self.true_button = Button(text="True",command = self.true_pressed)
        self.true_button.grid(column=1, row=2)
        false_image = "/home/bode/Documents/python_langage/day_34/quizzlab/false.png"
        self.false_button = Button(text="False",command=self.false_pressed)
        self.false_button.grid(column=2, row=2)


        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            global q_text
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(text= "You've reached the end of the quiz. See you!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_riight = self.quiz.check_answer("False")
        self.give_feedback(is_riight)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
            self.window.after(1000, self.get_next_question)
        if not is_right:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)


