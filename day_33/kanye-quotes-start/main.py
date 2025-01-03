from tkinter import *
import requests
import json

def get_quote():
    data = requests.get("https://api.kanye.rest") 
    json_data = data.json() 
    quotes = json_data["quote"]
    canvas.itemconfig(quote_text, text = quotes)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="/home/bode/Documents/python_langage/day_33/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text= "Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="/home/bode/Documents/python_langage/day_33/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()