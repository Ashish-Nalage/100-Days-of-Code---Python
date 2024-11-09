# Day 14 - Higher or Lower Game

## Overview
The **Higher or Lower Game** asks players to guess which of two Instagram profiles has more followers. The game continues until the player makes an incorrect guess, with the score increasing for each correct answer.

## Key Concepts
- **Random Selection**: Using `random.choice()` to pick random accounts from a dataset.
- **Functions**:
  - `account_selector()`: Chooses a random profile.
  - `compare()`: Checks which profile has more followers based on the player's choice.
- **Loop for Game Flow**: A `while` loop keeps the game running as long as guesses are correct.
- **Score Tracking**: The score is updated with each correct guess and displayed to the player.

## Game Logic
1. **Select Profiles**: Choose two random Instagram profiles.
2. **Display Choices**: Show details of "Account A" and "Account B" (name, description, country).
3. **Player Guess**: The player guesses which account has more followers by typing 'A' or 'B'.
4. **Comparison**: Check if the player's guess is correct.
   - If correct, increase the score and replace the lower profile.
   - If incorrect, end the game and show the final score.

## How to Play
1. Run the script.
2. Guess which profile has more followers by typing 'A' or 'B'.
3. Keep guessing correctly to increase your score.
4. The game ends when you make an incorrect guess.

## Improvements
- Add more profiles for variety.
- Implement a leaderboard to track high scores.
- Enhance user experience with a GUI version.
