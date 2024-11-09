# Day 11 - Blackjack Game

## Overview
This **Blackjack Game** is a simplified version of the classic card game. The player competes against the computer to get as close to a score of 21 as possible without going over. The game includes standard Blackjack rules, like handling aces as 1 or 11 and recognizing a Blackjack (score of 21 with the first two cards).

## Key Concepts
- **Random Selection**: Using `random.choice()` to deal a random card from the deck.
- **Functions**:
  - `deal_card()`: Returns a random card from a predefined deck.
  - `calculate_score()`: Calculates the total score of a hand, handling special rules for aces.
  - `compare()`: Compares the final scores of the user and computer to determine the winner.
- **Game Flow**: 
  - A `while` loop manages the game flow, allowing the player to draw cards or pass until the game ends.
- **Score Calculation**: Special conditions are included to handle Blackjack and bust scenarios.

## Game Logic
1. **Dealing Cards**:
   - The player and the computer each start with two cards.
   - Cards are drawn using the `deal_card()` function.
2. **Calculating Scores**:
   - The `calculate_score()` function checks for a Blackjack (score 0) or adjusts aces from 11 to 1 if needed.
3. **Player's Turn**:
   - The player can choose to draw another card or pass.
   - If the player's score exceeds 21, they bust, and the game ends.
4. **Computer's Turn**:
   - The computer draws cards until its score is 17 or higher.
   - The computer stops drawing if it hits a Blackjack (score 0) or exceeds 21.
5. **Determine Winner**:
   - The `compare()` function evaluates the scores and returns the result (win, lose, draw).

## How to Play
1. Run the script.
2. Choose to play by typing 'y'. 
3. View your initial hand and the computer's first card.
4. Decide whether to draw another card ('y') or pass ('n').
5. The game ends when either the player passes, goes over 21, or gets a Blackjack.
6. The result is displayed based on the final scores.

## Improvements
- **Additional Features**: Implement betting or a points system for added complexity.
- **GUI Version**: Enhance the game with a graphical user interface for better interaction.
- **Multiple Decks**: Increase the challenge by using multiple decks of cards for more realistic gameplay.
