from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGAUAGE = ("Ariel", 40, "italic")
MYWORD = ("Ariel", 60, "bold")
timer = None
# ---------------------------- GENERATE WORD ------------------------------- #
# data from csv
data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

def generate_word():
    current_word = choice(words)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_word["French"])
    
# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    window.after(3000 )
    
    
# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width = 800, height = 526,bg= BACKGROUND_COLOR,  highlightthickness=0 )
# front
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# back
card_back = PhotoImage(file="images/card_back.png")

# To change the image
canvas.itemconfig(canvas_image, image = card_back)

# text
card_title= canvas.create_text(400, 150, text="Title", font=LANGAUAGE)
card_word = canvas.create_text(400, 263, text=f"Word", font= MYWORD)

# Buttons
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=generate_word)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)


# create txt file for words

# call our generate card
generate_word()


window.mainloop()