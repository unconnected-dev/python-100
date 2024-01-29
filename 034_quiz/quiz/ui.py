from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)       
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        relative_images_path = "./034_quiz/quiz/images/"
        TRUE_IMAGE = relative_images_path + "true.png"
        FALSE_IMAGE = relative_images_path + "false.png"
        
        true_image = PhotoImage(file=TRUE_IMAGE)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=FALSE_IMAGE)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz...")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_correct = self.quiz_brain.check_answer("True")
        self.check_answer(is_correct)

    def false_pressed(self):
        is_correct = self.quiz_brain.check_answer("False")
        self.check_answer(is_correct)

    def check_answer(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)