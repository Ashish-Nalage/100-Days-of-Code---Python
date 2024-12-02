import random
from art import logo

def calculating_answer(users_input, actual_answer, no_turns):
    if users_input > actual_answer:
        print("Too High")
        return no_turns- 1
    elif users_input < actual_answer:
        print("Too Low")
        return no_turns- 1  
    else:
        print(f"You got it the number was {actual_answer}")
        return 
# create an random no. for guessing
answer = random.randint(1,100)

    
def game():

    # Welcome message and logo for better user experience
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(answer)

    # input for game level
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if game_level == "hard":
        no_of_chances = 5
    else:
        no_of_chances = 10

    # while loop for giving user respected chances to guess the no.
    user_guess = 0
    while user_guess != answer:
        print(f"You have {no_of_chances} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        no_of_chances = calculating_answer(user_guess, answer, no_of_chances)
        if no_of_chances == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return 
        elif user_guess != answer:
            print("guess again")

game()