from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    global current_card
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)

    show_card()

def show_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_canvas_image, image=card_front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_canvas_image, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="./images/card_front.png")
card_canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Answer", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=show_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

show_card()

window.mainloop()