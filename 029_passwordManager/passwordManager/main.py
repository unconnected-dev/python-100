import math
from tkinter import *
from PIL import ImageTk, Image

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)

relative_image_path = "./029_passwordManager/passwordManager/logo.png"
img = ImageTk.PhotoImage(Image.open(relative_image_path))
canvas.create_image(100, 94, image=img)

canvas.grid(row=1, column=1)



window.mainloop()