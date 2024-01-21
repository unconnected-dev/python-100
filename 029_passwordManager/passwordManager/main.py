import math
from tkinter import *
from PIL import ImageTk, Image

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=20, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)

relative_image_path = "./029_passwordManager/passwordManager/logo.png"
img = ImageTk.PhotoImage(Image.open(relative_image_path))
canvas.create_image(100, 94, image=img)

canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky="W")

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky="W")

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky="W")


#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="W")


#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()