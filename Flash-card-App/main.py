from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGAUAGE = ("Ariel", 40, "italic")
MYWORD = ("Ariel", 60, "bold")
timer = None
current_word = {}
words = {}

# ---------------------------- GENERATE WORD ------------------------------- #
# data from csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def generate_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    # To change it back the image
    canvas.itemconfig(canvas_image, image = card_front)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white" )
    # To change the image
    canvas.itemconfig(canvas_image, image = card_back)
# ---------------------------- SAVE PROGRESS ------------------------------- #

def correct_answer():
    words.remove(current_word)
    words_to_learn =pandas.DataFrame(words)
    words_to_learn.to_csv("words_to_learn.csv", index=False)
    generate_word()
    
# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
# canvas
canvas = Canvas(width = 800, height = 526,bg= BACKGROUND_COLOR,  highlightthickness=0 )
# front
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# back
card_back = PhotoImage(file="images/card_back.png")

# text
card_title= canvas.create_text(400, 150, text="Title", font=LANGAUAGE)
card_word = canvas.create_text(400, 263, text=f"Word", font= MYWORD)

# Buttons
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=correct_answer)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)


    
    
    
    # create csv file for words
    
# call our generate card
generate_word()


window.mainloop()