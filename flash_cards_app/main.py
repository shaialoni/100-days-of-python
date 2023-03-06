from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- DATA ------------------------------- #
try:
    data_frame = pandas.read_csv("words_to_learn.csv")
    print("Found the file")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data_frame = pandas.read_csv("./data/spanish_words.csv")
    print("No file found, creating new one")

words_to_learn = data_frame.to_dict(orient="records")
print(words_to_learn)
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_side, image=front_img)
    try:
        current_card = random.choice(words_to_learn)
    except IndexError:
        print("Looks like you are all done learning!")

    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(word, text=current_card['Spanish'], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_side, image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    try:
        words_to_learn.remove(current_card)
    except ValueError:
        print("Looks like you are all done here!")

    words_to_learn_df = pandas.DataFrame(words_to_learn)
    words_to_learn_df.to_csv("words_to_learn.csv", index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
card_side = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

back_img = PhotoImage(file="./images/card_back.png")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

check_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=check_img, highlightthickness=0, command=is_known)
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()
