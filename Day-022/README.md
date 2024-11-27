# Day 22 - Pong Game: Building a Classic Arcade Game

## What I Learned
Today, I implemented the **Pong Game** using Python and the Turtle module. This project involved integrating multiple object-oriented programming concepts and improving collision detection and game logic. Key learnings include:
- **Object Collaboration**: Managing interactions between multiple classes (`Paddle`, `Ball`, `Scoreboard`).
- **Game Physics**: Implemented simple collision detection for the ball with walls and paddles.
- **Adjustable Difficulty**: The ball's speed increases with each successful paddle collision.

## Key Concepts

### 1. Object Collaboration
- **Paddle Class**:
  - Created two paddle objects to represent the players.
  - Added methods for moving the paddles up and down using keyboard controls.
- **Ball Class**:
  - Managed ball movement, direction changes, and speed adjustments.
  - Handled collisions with the walls and paddles.
- **Scoreboard Class**:
  - Tracked and displayed scores for both players.
  - Updated the scoreboard dynamically after each point.

### 2. Game Logic and Collision Detection
- **Wall Collision**:
  - Bounced the ball vertically when it hits the top or bottom walls.
- **Paddle Collision**:
  - Detected proximity to paddles and reversed the ball’s direction horizontally.
  - Increased the ball's speed after each paddle collision to add difficulty.
- **Score Reset**:
  - Reset the ball's position and updated the score when a player missed the ball.

### 3. Screen Setup and Event Handling
- Configured the screen dimensions, title, and background color.
- Used **event listeners** to handle keyboard inputs for paddle movement.

## Project Overview
The **Pong Game** is a two-player arcade game where each player controls a paddle to prevent the ball from passing their side. The game includes:
1. **Dynamic Ball Movement**:
   - Ball bounces off walls and paddles.
   - Speed increases with each paddle collision.
2. **Scoring System**:
   - Tracks and displays scores for both players.
   - Resets the ball’s position after a point is scored.
3. **Responsive Controls**:
   - Players can move paddles up and down using the `Up`/`Down` keys (right paddle) and `W`/`S` keys (left paddle).

## Summary
This project reinforced my understanding of object-oriented programming and collision detection while building a classic game. It was an engaging way to practice creating interactive programs with real-time feedback. The Pong Game demonstrates the power of combining multiple classes and implementing game mechanics in Python.
