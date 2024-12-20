from tkinter import *
import pandas
import random
from tkinter import messagebox
import os


BACKGROUND_COLOR = "#B1DDC6"
current_card = None


try:
    df = pandas.read_csv("./Day-031/flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./Day-031/flash-card-project/data/french_words.csv")
finally:
    data_dict = df.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
   
def is_known():
    if len(data_dict) > 1:
        data_dict.remove(current_card)
        new_df = pandas.DataFrame(data_dict)
        new_df.to_csv("./Day-031/flash-card-project/data/words_to_learn.csv", index=False)
        print(len(data_dict))
        next_card()
    else:
        messagebox.showinfo(title="There's no word to learn",
                            message="Congratulation! You've review all the words!\nGood job, keep up the good work!")
        os.remove("./Day-031/flash-card-project/data/words_to_learn.csv")
        window.quit()
        
# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./Day-031/flash-card-project/images/card_front.png")
card_back_img = PhotoImage(file="./Day-031/flash-card-project/images/card_back.png")
card_background = canvas.create_image(400, 263,image=card_front_img )
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# button
right_img = PhotoImage(file="./Day-031/flash-card-project/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./Day-031/flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()