import tkinter


window = tkinter.Tk()
window.title("Window Title")
window.minsize(600, 600)

#Labels
a_label = tkinter.Label(text="Label name", font=("Arial", 24, "bold"))
a_label.pack(side="left")


window.mainloop()#Place at the end of script