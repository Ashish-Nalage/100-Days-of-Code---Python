import random
import art
from game_data import data
import os

# function to clear terminal
def clear():
    """clears terminal"""
    os.system('cls')

# function to select random dictionary from data list
def account_selector():
    return random.choice(data)

# function to compare instagram followers according to users guess
def compare(a_followers, b_followers, choice):
    """comapres followers of both individuals and return True or False according to users choice"""
    if choice == "a":
        return a_followers > b_followers
    else:
        return b_followers > a_followers

def game():

    score = 0
    a = account_selector()
    b = account_selector()
    if a == b:
        b = account_selector()

    while True:
        print(art.logo)
        
        if score > 0:
            print(f"You're right! Current score: {score}.")
            
        print(f"Compare A: {a["name"]}, {a["description"]}, {a["country"]}")
        print(art.vs)
        print(f"Against B: {b["name"]}, {b["description"]}, {b["country"]}")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        compare_result = compare(a["follower_count"], b["follower_count"], user_input)

        if compare_result == True:
            score += 1
            a = b
            b = account_selector()
            clear()
        else:
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return   
game()