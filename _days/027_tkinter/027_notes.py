# import tkinter
from tkinter import *

if True:
    window = Tk()
    window.title("Window Title")
    window.minsize(600, 600)

    #Labels
    a_label = Label(text="Label name", font=("Arial", 24, "bold"))
    a_label.pack()

    #Alternative ways to update properties in tkinter
    # a_label["text"] = "New Text"
    # a_label.config(text="updated text")


    #Entry
    input = Entry(width=10)
    input.pack()


    #Buttons
    a_button = Button(text="button text")
    a_button.pack()

    def button_clicked():
        a_label["text"] = input.get()

    #Assign function to button
    a_button["command"] = button_clicked


    #Text entry
    a_text_box = Text(height=5, width=30)
    #Puts cursor in textbox
    a_text_box.focus()
    #Add initial text into the box
    a_text_box.insert(END, "example of multi-line text entry")
    #Get's current value in textboat from line 1, character 0 to END
    print(a_text_box.get("1.0", END))#END is an index
    a_text_box.pack()


    #Spinbox
    def spinbox_used():
        print(spinbox.get())

    spinbox = Spinbox(from_=0,to_=10,width=5,command=spinbox_used)
    spinbox.pack()


    #Scale
    def scale_used(value):
        print(value)

    scale = Scale(from_=0,to_=100,command=scale_used)
    scale.pack()


    #Checkbutton
    def checkbutton_used():
        print(checked_state.get())

    #variable to hold on to checked state, 0 is off, 1 is on
    checked_state = IntVar()#This is a class
    checkbutton = Checkbutton(text="is on?", variable=checked_state,command=checkbutton_used)
    # checked_state.get()
    checkbutton.pack()


    #Radiobutton
    def radio_used():
        print(radio_state.get())
    
    #variable to hold on to which radio button value is checked
    radio_state = IntVar()
    radiobutton1 = Radiobutton(text="option 1", value=1, variable=radio_state, command=radio_used)
    radiobutton2 = Radiobutton(text="option 2", value=2, variable=radio_state, command=radio_used)
    radiobutton3 = Radiobutton(text="option 3", value=3, variable=radio_state, command=radio_used)

    radiobutton1.pack()
    radiobutton2.pack()
    radiobutton3.pack()


    #Listbox
    def listbox_used(event):
        #get current selection from listbox
        print(listbox.get(listbox.curselection()))
    
    listbox = Listbox(height=4)
    fruits=["apple","pear","orange","strawberry"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)

    listbox.bind("<<ListboxSelect>>", listbox_used)#Sets command
    listbox.pack()
    

    window.mainloop()#Place at the end of script


#Default arguments
if False:
    def a_function(a=1,b=2,c=3):
        return a + b + c

    print(a_function())
    print(a_function(c=5))


#Unlimited positional arguments
if False:    
    def add(*args):
        total = 0
        for n in args:
            total += n
        
        return total
    
    print(f"{add(1,2,3,4,5)}")


#Unlimited keyword arguments
#kwargs creates a dictionary
if False:
    def calculate(n, **kwargs):
        # for key, value in kwargs.items():
        #     print(key)
        n+=kwargs["add"]
        n*=kwargs["mult"]
        
        return n
    
    print(f"{calculate(10, add=3, mult=5)}")


if False:
    class Example:
        def __init__(self, **kwargs) -> None:
            # self.make = kwargs["make"]
            # self.model = kwargs["model"]
            #.get will return None if it can't find the reference in **kwargs
            self.make = kwargs.get("make")
            self.model = kwargs.get("model")

    my_example = Example(make="Test")
    print(my_example.make)
    print(my_example.model)