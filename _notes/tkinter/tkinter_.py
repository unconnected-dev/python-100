#Tkinter
#Is a commonly used library for creating graphical user interfaces in Python

from tkinter import *


#Basic window
if False:
    window = Tk()
    window.title("Title")
    window.minsize(600, 600)

    #Place mainloop() at the end or it will close 
    window.mainloop()


#Example window
root = Tk()
root.title("Widgets")
root.minsize(600, 600)
    

#Widgets
#Tkinter provides various widgets to create GUI elements


#Labels
if False:
    a_label = Label(text="Label name", font=("arial", 24, "bold"))
    a_label.pack()

    #Updating properties in Tkinter
    a_label["text"] = "Updated text"
    a_label.config(text="Updated via config")

if False:
    photo_relative_file_path = "./_notes/tkinter/images/right.png"
    a_photo = PhotoImage(file=photo_relative_file_path)

    photo_label = Label(root, image=a_photo)
    photo_label.pack()


#Entries
if False:
    #Width is the number of characters allowed in the text field
    an_entry = Entry(width=10)
    #Add initial text into the entry
    an_entry.insert(END, "Example of a text entry")
    an_entry.pack()

    #Puts cursor in entry
    an_entry.focus()

    print(f"{an_entry.get()}")


#Text entries
if False:
    a_text_entry = Text(height=5, width=30)
    #Add initial text into the box
    a_text_entry.insert(END, "Example of multi-line text entry")
    a_text_entry.pack()

    #Puts cursor in textbox
    a_text_entry.focus()

    #Get's current value in textboat from line 1, character 0 to END
    #END is an index
    print(f"{a_text_entry.get('1.0', END)}")


#Buttons
if False:
    a_button = Button(text="Button text")
    a_button.pack() 


    #Assigning functions to a button
    a_label = Label(text="Empty", font=("arial", 24, "bold"))
    a_label.pack()

    def example_command():
        a_label["text"] = "Updated text"
    
    #Assign function to button
    a_button["command"] = example_command


#Spinbox
if False:
    def spinbox_used():
        print(f"spinbox_used: {a_spinbox.get()}")

    a_spinbox = Spinbox(from_=0,to_=10,width=5,command=spinbox_used)
    a_spinbox.pack()


#Scale
if False:
    def scale_used(value):
        print(f"scale_used: {value}")

    a_scale = Scale(from_=0,to_=100,command=scale_used)
    a_scale.pack()


#Checkbutton
if False:
    def checkbutton_used():
        print(f"checked_state: {checked_state.get()}")

    #checked_state is a variable to hold on to checked state
    #0 is off, 1 is on
    checked_state = IntVar()

    a_checkbutton = Checkbutton(text="Option A", variable=checked_state, command=checkbutton_used)
    a_checkbutton.pack()


#Radiobutton
if False:
    def radio_used():
        print(f"radio_state: {radio_state.get()}")

    #The reason that StringVar() made all buttons active
    #The default for tristatevalue is an empty string and the default value for a StringVar is an empty string
    
    #Best practice with radio buttons is to always make sure the default value corresponds to one
    #of the radiobutton values unless we want tri-state mode
    radio_state = StringVar(value="A")
    a_radiobutton_1 = Radiobutton(text="Option A", value="A", variable=radio_state, command=radio_used, tristatevalue=0)
    a_radiobutton_2 = Radiobutton(text="Option B", value="B", variable=radio_state, command=radio_used, tristatevalue=0)
    a_radiobutton_3 = Radiobutton(text="Option C", value="C", variable=radio_state, command=radio_used, tristatevalue=0)

    a_radiobutton_1.pack()
    a_radiobutton_2.pack()
    a_radiobutton_3.pack()


#Listbox
if False:
    def listbox_used(event):
        #get() will get the current selection from the listbox
        print(f"{a_listbox.get(a_listbox.curselection())}")

    a_listbox = Listbox(height=4)
    fruits=["apple","pear","orange","strawberry"]
    for item in fruits:
        a_listbox.insert(fruits.index(item), item)
    
    #Sets the command
    a_listbox.bind("<<ListboxSelect>>", listbox_used)
    a_listbox.pack()


root.mainloop()