import turtle
import pandas

screen = turtle.Screen()
screen.title("State Game")

#Add image to screen background
relative_image_path = "./025_csvFiles/stateGame/blank_states_img.gif"
screen.addshape(relative_image_path)
turtle.shape(relative_image_path)

relative_csv_path = "./025_csvFiles/stateGame/50_states.csv"
with open(relative_csv_path) as data_file:
    state_data = pandas.read_csv(data_file)


answers = []
while len(answers) < 50:
    answer = screen.textinput(f"{len(answers)}/50 - Name a state", "").lower()
    if len(state_data[state_data["state"] == answer.capitalize()]) == 1 and answer.lower() not in answers:
        answers.append(answer.lower())

    print(answers)

turtle.mainloop()