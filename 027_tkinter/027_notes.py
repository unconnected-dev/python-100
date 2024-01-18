import tkinter

if False:
    window = tkinter.Tk()
    window.title("Window Title")
    window.minsize(600, 600)

    #Labels
    a_label = tkinter.Label(text="Label name", font=("Arial", 24, "bold"))
    a_label.pack(side="left")


    window.mainloop()#Place at the end of script


#Default arguments
if False:
    def a_function(a=1,b=2,c=3):
        return a + b + c

    print(a_function())
    print(a_function(c=5))
