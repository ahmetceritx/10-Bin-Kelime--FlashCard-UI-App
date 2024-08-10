import turtle

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
from itertools import cycle



current_card = {}
to_learn = {}
try:
    data= pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") #bunu yapmasaydık sözlüğü full french çıkartıp sonra english çıkartıyordu. Bu yöntemle bir french bir english çıkarttık.


card_cyle= cycle(to_learn)

def next_card():
    global current_card, flip_timer
    current_card = next(card_cyle)
    #random.choice(to_learn))
    canvas.itemconfig(canvas_title, text="English", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["word"], fill="black")
    canvas.itemconfig(front_image, image=photo_front)



is_front= True
def flip_card():
    global is_front

    if is_front:
        # Kartı arkaya çevir
        canvas.itemconfig(canvas_title, text="TURKISH", fill="white")
        canvas.itemconfig(canvas_word, text=current_card["kelime"], fill="white")
        canvas.itemconfig(front_image, image=photo_back)
        is_front = False
    else:
        # Kartı öne çevir
        canvas.itemconfig(canvas_title, text="English", fill="black")
        canvas.itemconfig(canvas_word, text=current_card["word"], fill="black")
        canvas.itemconfig(front_image, image=photo_front)
        is_front = True


def is_known():
    to_learn.remove(current_card)
    how_many_words= (len(to_learn))
    canvas.itemconfig(to_learn_word, text=f"You need to learn {how_many_words} more", fill="red")

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


photo_front = PhotoImage(file="images/card_front.png")
photo_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
front_image = canvas.create_image(400,263, image=photo_front)

canvas_title = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
to_learn_word= canvas.create_text(400, 450, text="", font=("Ariel", 12, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column=0, columnspan=3)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_image= PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=2,)

flip_png= PhotoImage(file="images/flip.png", width=100, height=100)
flip_button = Button(image=flip_png, command=flip_card)
flip_button.grid(row=1, column=1,)


next_card()






window.mainloop()

