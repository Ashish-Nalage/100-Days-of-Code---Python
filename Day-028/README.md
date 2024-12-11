# Day 28 - Pomodoro Timer with Tkinter

## What I Learned
Today, I built a **Pomodoro Timer** using the Tkinter library. This project introduced several new concepts related to GUI programming and time management in Python. Here's what I learned in detail:

---

## Key Concepts

### 1. **Time Management with `after()`**
- **`after(milliseconds, function)`**:
  - A Tkinter method to schedule a function to run after a specified delay.
  - Used to implement the countdown mechanism and ensure it updates the UI every second.
  - Example: `window.after(1000, count_down, count - 1)` schedules the `count_down()` function to execute after 1 second with the updated `count` value.

### 2. **Global Variables and State Management**
- Managed the application's state using global variables:
  - `reps`: Tracks the number of work and break sessions completed.
  - `timer`: Stores the `after()` function's ID, which allows us to cancel it when resetting the timer.
- Used state variables to dynamically update the UI and implement different modes (work, short break, long break).

### 3. **Dynamic UI Updates**
- **Canvas Widget**:
  - Created a custom UI element using `Canvas`, which allows adding images and custom text.
  - Example: Displayed the countdown timer dynamically on the canvas with `canvas.itemconfig()`.
- **Label Widget**:
  - Updated text and color to reflect the current mode (work, short break, or long break) using `config()`.

### 4. **Math Operations**
- Used the `math` module for:
  - Converting seconds to minutes and seconds for the countdown timer.
  - Calculating the number of completed work sessions (`math.floor(reps/2)`) to display checkmarks.

### 5. **Working with Images in Tkinter**
- **`PhotoImage`**:
  - Loaded and displayed the `tomato.png` image as part of the timer's design.
  - Managed image placement with `canvas.create_image()`.

---

## Project Overview: Pomodoro Timer

### Features:
1. **Work and Break Cycles**:
   - 25-minute work sessions followed by short (5 minutes) or long (20 minutes) breaks.
   - Automatically transitions between cycles.
   
2. **Start and Reset**:
   - **Start Button**: Starts the timer and cycles through work and breaks.
   - **Reset Button**: Stops the timer, clears the countdown, and resets the UI.

3. **Visual Feedback**:
   - Dynamically updates the countdown and mode (`Timer`, `Break`, `Work`) on the screen.
   - Displays checkmarks for each completed work session.

4. **Custom Styling**:
   - Used constants for colors and fonts to ensure a visually appealing design.

---

## Summary
Today's project combined time management and GUI programming, reinforcing several new and advanced Tkinter concepts. Key takeaways include:
- Using `after()` for scheduling and dynamic updates.
- Managing global variables to track state.
- Enhancing UI with images, labels, and canvas widgets.
The Pomodoro Timer is a practical application of these concepts and demonstrates how to build interactive productivity tools in Python.
