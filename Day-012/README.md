# Day 12 - Number Guessing Game

## What I Learned in Lessons
- **Local Scope**: Variables and functions defined inside a function are only accessible within that function.
- **Namespacing**: Anything you give a name to, like variables and functions within a function, is only accessible in that function.
- **Global Scope**: Variables and functions created outside of any function or at the top level are accessible everywhere in the code.
- **Block Scope**: Variables created in indented blocks (like in `if` statements, `for` loops, or `while` loops) are considered to be in global scope in Python.

## Overview
This **Number Guessing Game** allows the player to guess a randomly selected number between 1 and 100. The player has a set number of attempts based on the chosen difficulty level. The game provides feedback after each guess, letting the player know if their guess is too high or too low. The game continues until the player guesses the number correctly or runs out of attempts.

## Key Concepts
- **Random Selection**: Using `random.randint()` to select a random number between 1 and 100.
- **Functions**:
  - `calculating_answer()`: Checks the player's guess against the actual answer, providing feedback on whether it's too high, too low, or correct.
  - `game()`: The main game function that handles the game flow, difficulty selection, and manages the number of attempts.
- **Game Flow**:
  - A `while` loop controls the guessing process, allowing the player to make guesses until they run out of attempts or guess the number correctly.
  - The game checks after each guess whether the number is too high, too low, or correct.

## Game Logic
1. **Dealing with Input**:
   - The player selects a difficulty level (`easy` or `hard`), which determines the number of attempts (10 for easy, 5 for hard).
   - The game then generates a random number between 1 and 100.
2. **Player’s Turn**:
   - The player is asked to guess a number, and the game provides feedback after each guess (too high, too low, or correct).
   - The number of attempts is reduced after each guess.
   - If the player runs out of attempts, the game ends.
3. **Feedback**:
   - After each guess, the game tells the player how many attempts they have left and whether their guess was too high or too low.

## How to Play
1. Run the script.
2. Choose a difficulty by typing 'easy' (10 attempts) or 'hard' (5 attempts).
3. Make guesses to try and guess the correct number between 1 and 100.
4. The game will provide feedback after each guess.
5. If you guess correctly, you win; if you run out of attempts, the game ends.

## Improvements
- **Additional Features**: Implement a scoring system based on how many attempts were used to guess the number.
- **User Input Validation**: Add input validation to ensure the player enters valid numbers and difficulty levels.
- **Multiple Rounds**: Allow the player to play multiple rounds without restarting the script.
