# Day 23 - Turtle Crossing Game: A Classic Arcade Challenge

## What I Learned
Today, I built the **Turtle Crossing Game**, inspired by the classic arcade game *Frogger*. This project combined concepts like object-oriented programming, collision detection, and dynamic difficulty adjustment. Key learnings include:
- **Dynamic Object Management**: Created, moved, and managed multiple car objects with varying positions and speeds.
- **Collision Detection**: Implemented logic to detect collisions between the player (turtle) and cars.
- **Game Progression**: Incorporated a leveling system that increases the car speed with each successful crossing.

## Key Concepts

### 1. Object Collaboration
- **Player Class**:
  - Controlled the turtle's movement and managed its starting and finishing positions.
- **CarManager Class**:
  - Created cars at random positions and managed their movement across the screen.
  - Increased car speed with each level.
- **Scoreboard Class**:
  - Tracked and displayed the player's current level.
  - Displayed "Game Over" when the player collided with a car.

### 2. Game Mechanics
- **Collision Detection**:
  - Checked the distance between the turtle and each car to determine if a collision occurred.
- **Dynamic Difficulty**:
  - Cars moved faster with each level, making the game progressively harder.
- **Winning Condition**:
  - When the turtle reached the top of the screen, the level increased, the turtle reset to the starting position, and car speed increased.

### 3. Screen and Event Handling
- Set up the screen with a 600x600 grid and used the **Turtle module's event listeners** to control the player's movement with the `Up` arrow key.

## Project Overview
The **Turtle Crossing Game** is a fun and challenging game where the player navigates a turtle across a busy road while avoiding cars. Each successful crossing increases the level and the car speed.

### Features:
1. **Player Movement**:
   - The turtle moves forward when the `Up` arrow key is pressed.
   - Returns to the starting position after a successful crossing.
2. **Car Generation and Movement**:
   - Cars are created at random intervals and move from right to left.
   - Their speed increases as the levels progress.
3. **Level System**:
   - Tracks the player's current level and updates it on the screen.
   - Displays "Game Over" upon collision with a car.

## Summary
This project showcased the power of object-oriented programming for building interactive games. I practiced managing multiple objects, detecting collisions, and implementing a dynamic difficulty system. The Turtle Crossing Game is a fun example of how Python can be used to recreate classic games with modern programming techniques.
