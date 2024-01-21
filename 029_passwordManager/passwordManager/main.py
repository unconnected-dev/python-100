from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from passwordGenerator import PasswordGenerator

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def makePassword():
    generator = PasswordGenerator()
    password_entry.insert(0, generator.makePassword())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData(website, email, password):
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing information",message="All fields must be filled in")
    else:
        response = messagebox.askokcancel(title=website, message=f"Confirm details: \n Website: {website} \n Email: {email} \n Password: {password}")
        
        if response == True:
            relative_file_path = "./029_passwordManager/passwordManager/data.txt"
            with open(relative_file_path, "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")

            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)


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
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")

email_entry = Entry(width=52)
email_entry.insert(0, "email@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="W")


#Buttons
generate_password_button = Button(text="Generate Password", command=makePassword)
generate_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=lambda: saveData(website_entry.get(), email_entry.get(), password_entry.get()))
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()