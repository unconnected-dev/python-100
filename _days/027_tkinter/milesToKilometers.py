from tkinter import *


window = Tk()
window.title("Miles to Kilometer")
window.minsize(300, 150)
window.config(padx=20, pady=20)


#Entry
input = Entry(width=20)
input.grid(row=0,column=1)


#Label
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(row=0,column=2)

equal_to_label = Label(text="is equal to", font=("Arial", 10))
equal_to_label.grid(row=1,column=0)

kilometer_coversion_label = Label(text="", font=("Arial", 10, "bold"))
kilometer_coversion_label.grid(row=1, column=1)

kilometer_label = Label(text="Kilometers", font=("Arial", 10))
kilometer_label.grid(row=1, column=2)


def button_clicked():
    kilometer_coversion_label["text"] = float(input.get()) *  1.609

#Button
a_button = Button(text="Convert")
a_button["command"] = button_clicked
a_button.grid(row=2, column=1)

window.mainloop()