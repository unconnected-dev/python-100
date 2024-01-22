from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from passwordGenerator import PasswordGenerator
import pyperclip
import json

WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def makePassword():
    generator = PasswordGenerator()
    password_entry.insert(0, generator.makePassword())

    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData(website, email, password):
    relative_file_path = "./029_passwordManager/passwordManager/data.json"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing information",message="All fields must be filled in")
    else:
        response = messagebox.askokcancel(title=website, message=f"Confirm details: \n Website: {website} \n Email: {email} \n Password: {password}")
        
        if response == True:
            new_data = {
                        website:{
                            "email": email,
                            "password": password,
                        }
                    }

            try:    
                with open(relative_file_path, "r") as data_file:
                    # data_file.write(f"{website} | {email} | {password} \n")

                    data = json.load(data_file)                                     #Read old data

            except FileNotFoundError:                                               #Create a new file if needed
                with open(relative_file_path, "w") as data_file:
                    json.dump(new_data, indent=4)

            else:
                data.update(new_data)                                               #Update old data with new data

                #You need to read first as opening with w will empty the file
                with open(relative_file_path, "w") as data_file:
                    json.dump(data, data_file, indent=4)                            #Save updated data

            finally:
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)


def searchData():
    search_term = website_entry.get()

    relative_file_path = "./029_passwordManager/passwordManager/data.json"

    try:
        with open(relative_file_path) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if search_term in data:
            email = data[search_term]["email"]
            password = data[search_term]["password"]
            messagebox.showinfo(title=search_term, message=f"Email:{email}\nPassword:{password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_term}")


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
website_label = Label(text="Website:", bg="white", pady=5)
website_label.grid(row=1, column=0, sticky="W")

email_label = Label(text="Email/Username:", bg="white", pady=5)
email_label.grid(row=2, column=0, sticky="W")

password_label = Label(text="Password:", bg="white", pady=5)
password_label.grid(row=3, column=0, sticky="W")


#Entries
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky="W")

email_entry = Entry(width=52)
email_entry.insert(0, "email@email.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="W")


#Buttons
search_button = Button(text="Search", width=15, command=searchData)
search_button.grid(row=1, column=2, stick="W")

generate_password_button = Button(text="Generate Password", command=makePassword)
generate_password_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=44, command=lambda: saveData(website_entry.get(), email_entry.get(), password_entry.get()))
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()