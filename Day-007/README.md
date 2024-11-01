# Day 7 - Hangman Game

## What I Learned
- **Lists and Strings:** Used lists to store correct guesses and strings for displaying the word.
- **While Loops:** Implemented loops to allow continuous guessing until the game ends.
- **Game Logic:** Managed game state using conditions to track lives and wins.
- **Importing Modules:** Utilized imported lists from separate files to enhance the game's functionality.

## Project Overview
The Hangman Game is a text-based guessing game where players attempt to guess a word by suggesting letters within a limited number of attempts.

## How It Works
- The player is prompted to guess letters, with feedback provided for correct and incorrect guesses.
- The game continues until the player either guesses the word or runs out of lives.

## Code Highlights
- Randomly selecting a word from a predefined list imported from `hangman_words.py`
- Using stages and artwork from `hangman_art.py` for visual feedback
- Using loops and conditionals to manage the game's flow
- Displaying the current state of the word with guessed letters
