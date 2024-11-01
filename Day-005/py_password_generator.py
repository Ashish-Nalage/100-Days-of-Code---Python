import random

# Character pools
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# User input for password criteria
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Generate password components
for item in range(0, no_letters):
    password_list.append(random.choice(letters))

for item in range(0, no_numbers):
    password_list.append(random.choice(numbers))

for item in range(0, no_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)  # Shuffle the list

# Build the final password string
password = ""
for item in password_list:
    password += item

print(f"Your password is: {password}")
