# Day 21 - Snake Game: Part 2

## What I Learned
Today, I learned about **class inheritance** and **list/tuple slicing**. I applied these concepts to complete the Snake Game project by:
- **Class Inheritance**: Used inheritance to create the `Food` and `Scoreboard` classes, extending the `Turtle` class from the `turtle` module. This allowed me to reuse the `Turtle` functionality and add custom behavior to these classes.
- **List/Tuple Slicing**: Applied slicing techniques to manage and manipulate the snake's body segments and extend the snake as it eats food.

## Key Concepts

### 1. Class Inheritance
- **Inheritance** allows a class to inherit properties and methods from another class. 
  - The `Food` and `Scoreboard` classes inherit from `Turtle` to access its drawing and movement functionalities.
  - **`super()`** is used to call the constructor of the parent class (`Turtle`) and initialize the custom behavior.

### 2. List and Tuple Slicing
- **List/tuple slicing** allows accessing parts of the list or tuple.
  - Used for managing the snake's body segments and controlling the movement of each segment by referencing the previous one in the sequence.

## Project Overview: Snake Game - Part 2

In this part of the project, I completed the **Snake Game** by:
1. **Adding Food**: 
   - Created a `Food` class to randomly place food on the screen.
   - Each time the snake eats food, the snake grows, and the score is updated.
   
2. **Scoreboard**:
   - Created a `Scoreboard` class to track and display the player's score.
   - The game ends when the snake collides with the wall or itself, displaying a "Game Over" message.
   
3. **Game Logic**:
   - Integrated keyboard controls for snake movement.
   - Used **event listeners** to change the snake’s direction based on user input.
   - Implemented the logic for snake movement, collision detection, food consumption, and extending the snake's length.

## Summary
Today's lesson reinforced the importance of OOP concepts like inheritance and the use of slicing in handling complex data structures. By completing the Snake Game project, I applied these concepts in a real-world project and gained hands-on experience in building games using Python’s Turtle module.
