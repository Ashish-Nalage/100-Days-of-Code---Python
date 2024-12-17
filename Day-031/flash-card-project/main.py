from tkinter import *
import pandas
import random

random_index = None
df = pandas.read_csv("./Day-031/flash-card-project/data/french_words.csv")
data_dict = df.to_dict(orient="records")


BACKGROUND_COLOR = "#B1DDC6"

    
def generate_french_word():
    global random_index, df, data_dict
    random_index = random.randint(0,100)
    canvas.itemconfig(title_text, text="French")
    french_word = data_dict[random_index]["French"]
    canvas.itemconfig(word_text, text=french_word)
    window.after(3000, english_translater)
    
def english_translater():
    global random_index, df, data_dict
    card_back_img = PhotoImage(file="./Day-031/flash-card-project/images/card_back.png")
    canvas.create_image(400, 263,image=card_back_img )
    english_word = data_dict[random_index]["English"]
    canvas.itemconfig(title_text, text="English")

    canvas.itemconfig(word_text, text=english_word)
# UI

# window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./Day-031/flash-card-project/images/card_front.png")
canvas_img = canvas.create_image(400, 263,image=card_front_img )
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# button
right_img = PhotoImage(file="./Day-031/flash-card-project/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=generate_french_word)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./Day-031/flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_french_word)
wrong_button.grid(column=0, row=1)

window.mainloop()