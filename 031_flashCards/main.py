from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

#Images
relative_images_path = "./031_flashCards/images/"
CARD_FRONT = relative_images_path + "card_front.png"
CARD_BACK = relative_images_path + "card_back.png"
RIGHT = relative_images_path + "right.png"
WRONG = relative_images_path + "wrong.png"

#Data
relative_data_path = "./031_flashCards/data/french_words.csv"

#GUI
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

#Canvas
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file=CARD_FRONT)
canvas.create_image(400, 263, image=card_front_img)

canvas.create_text(400, 150, text="Title", font=("Arial",40,"italic"))
canvas.create_text(400, 263, text="word", font=("Arial",40,"bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1,column=1)



window.mainloop()