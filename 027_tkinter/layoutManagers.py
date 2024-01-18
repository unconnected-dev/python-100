from tkinter import *


def button_clicked():
    a_label["text"] = input.get()
    
#tkinter layout managers
#different ways to place GUI elements
window = Tk()
window.title("Window Title")
window.minsize(600, 600)
window.config(padx=20, pady=20)#stops putting GUI elements up to the window edge

#Labels
a_label = Label(text="Label name", font=("Arial", 24, "bold"))
# a_label.pack()
# a_label.place(x=10, y=10)
a_label.grid(column=0,row=0)
a_label.config(padx=10, pady=10)

#Entry
input = Entry(width=10)
# input.pack()
# input.place(x=10, y=110)
input.grid(column=1,row=1)

#Buttons
a_button = Button(text="button text")
a_button["command"] = button_clicked
# a_button.pack()
# a_button.place(x=10, y=210)
a_button.grid(column=3,row=2)

#Second button
another_button = Button(text="another button")
another_button.grid(column=2,row=0)

window.mainloop()