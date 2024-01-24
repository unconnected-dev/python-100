from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    #Write your code here.

    #Will raise HTTP error if unsuccessful status code
    response.raise_for_status()

    response_data = response.json()
    # print(response_data)
    quote = response_data["quote"]
    canvas.itemconfig(quote_text, text=quote, fill="Black")


relative_images_path = "./033_apis/kanyeQuotes/"
BACKGROUND = relative_images_path + "background.png"
KANYE = relative_images_path + "kanye.png"

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()