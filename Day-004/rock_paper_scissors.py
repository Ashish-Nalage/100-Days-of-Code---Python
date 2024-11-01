import random

# ASCII art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices
choices = [rock, paper, scissors]

# Get user input and validate
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice > 2 or user_choice < 0:
    print("Invalid choice! You must choose 0, 1, or 2.")
else:
    print("You chose:")
    print(choices[user_choice])

    # Generate computer choice
    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[comp_choice])

    # Determine the result
    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("You won!")
    else:
        print("You lost!")
