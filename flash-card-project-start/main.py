from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict("records")

word = random.choice(to_learn)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text= word["English"], fill="white")
    canvas.configure(bg=BACKGROUND_COLOR)

def next_card():
    global word, timer
    word = random.choice(to_learn)
    window.after_cancel(timer)
    timer = window.after(3000, flip_card)
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=word["French"], fill="Black")
    canvas.configure(bg="white")


window = Tk()
timer = window.after(3000, flip_card)
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=220, bg="White")
card_title = canvas.create_text(200, 60, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(200, 130 , text="", font=("Arial", 45, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()
window.mainloop()
