from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)       
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        relative_images_path = "./034_quiz/quiz/images/"
        TRUE_IMAGE = relative_images_path + "true.png"
        FALSE_IMAGE = relative_images_path + "false.png"
        
        true_image = PhotoImage(file=TRUE_IMAGE)
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file=FALSE_IMAGE)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()