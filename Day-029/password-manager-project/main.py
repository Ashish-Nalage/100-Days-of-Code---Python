from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("Arial", 9, "italic")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list) # final generated password

    password_entry.insert(0, password) # insert to password_entry
    pyperclip.copy(password) # copies the generated password to clipboard
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # getting inputed data
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Opps", message="Please dont leave any feilds empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nIS IT OK TO SAVE?")

        if is_ok:
        # appending in data.txt
            with open("C:/Users/nalag/OneDrive/Personal Vault/data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")

                # clearing input and refocuing the cursor 
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="./Day-029/password-manager-project/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1,row=0)

# lable
website_lable = Label(text="Website:")
website_lable.grid(column=0, row=1)
website_lable.config(font=FONT)

email_lable = Label(text="Email/Username:")
email_lable.grid(column=0, row=2)
email_lable.config(font=FONT)

password_lable = Label(text="Password:")
password_lable.grid(column=0, row=3)
password_lable.config(font=FONT)

# entry
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "nalageashish2005@gmail.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")


# button
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()