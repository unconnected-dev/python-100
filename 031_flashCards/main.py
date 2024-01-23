from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#Images
relative_images_path = "./031_flashCards/images/"
CARD_FRONT = relative_images_path + "card_front.png"
CARD_BACK = relative_images_path + "card_back.png"
RIGHT = relative_images_path + "right.png"
WRONG = relative_images_path + "wrong.png"

#Data
relative_data_path = "./031_flashCards/data/french_words.csv"

data = pandas.read_csv(relative_data_path)
data_dict = data.to_dict(orient="records")


def nextCard():
    card = random.choice(data_dict)
    french_word = card["French"]

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)

#GUI
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

#Canvas
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="language", font=("Arial",40,"italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial",40,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0,command=nextCard)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image, highlightthickness=0,command=nextCard)
right_button.grid(row=1,column=1)


nextCard()

window.mainloop()