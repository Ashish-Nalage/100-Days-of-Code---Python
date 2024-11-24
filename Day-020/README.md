# Day 20 - Snake Game: Part 1

## What I Learned
Today, I started building the classic **Snake Game** using the Turtle module. This was the first part of the project where I:
- **Created the Snake Body**: Used multiple Turtle objects to represent the segments of the snake.
- **Implemented Movement**: Made the snake move forward and ensured all segments followed the head.
- **Controlled the Snake**: Added keyboard controls to allow the user to turn the snake in all directions while preventing it from reversing on itself.

## Key Concepts

### 1. Snake Body Creation
- Used a list of Turtle objects to represent the snake's body.
- Positioned each segment in a row using predefined coordinates for initialization.

### 2. Movement Logic
- Updated the position of each segment in reverse order to make the snake appear as one continuous entity.
- Moved the head forward by a fixed distance and adjusted the rest of the segments to follow.

### 3. Keyboard Controls
- Used **Turtle's event listeners** (`screen.onkey`) to bind arrow keys for directional control.
- Ensured the snake doesn't reverse on itself by restricting turns based on the current heading.

## Project Highlights
1. **Snake Movement**:
   - Continuous forward movement using a `while` loop and screen updates with `screen.tracer(0)` and `screen.update()`.
   - Smooth animation achieved by adding a small delay using `time.sleep(0.1)`.

2. **Modular Design**:
   - Encapsulated the snake's logic in a separate `Snake` class within `snake.py` to ensure better readability and reusability.

3. **Directional Controls**:
   - Added methods (`up()`, `down()`, `left()`, `right()`) to manage direction changes while preventing the snake from moving in the opposite direction.

## Summary
This part of the project laid the foundation for the Snake Game by:
- Creating a modular snake structure.
- Implementing basic movement and controls.
- Preparing the game for future features like collision detection and food collection.

Feel free to check the code and play the game by running the `main.py` file!
