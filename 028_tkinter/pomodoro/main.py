from tkinter import *
from PIL import ImageTk, Image
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
relative_image_path = "./028_tkinter/pomodoro/tomato.png"
img = ImageTk.PhotoImage(Image.open(relative_image_path))

canvas.create_image(100,112,image=img)
canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))

canvas.pack()



window.mainloop()