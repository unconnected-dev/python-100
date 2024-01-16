import turtle

screen = turtle.Screen()
screen.title("State Game")

#Add image to screen background
relative_image_path = "./025_csvFiles/stateGame/blank_states_img.gif"
screen.addshape(relative_image_path)
turtle.shape(relative_image_path)


answer = screen.textinput("Name a state", "")

turtle.mainloop()