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