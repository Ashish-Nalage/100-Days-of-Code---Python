# Day 24 - Mail Merge Project and Snake Game Enhancement

## What I Learned
Today's focus was on mastering **file handling** in Python and applying it in two distinct projects. Key learnings include:
- **File Operations**:
  - Open files using different modes: `read`, `write`, and `append`.
  - Use **relative** and **absolute file paths** for accessing files.
- **String Manipulation**:
  - Used methods like `.replace()`, `.strip()`, and `.readlines()` to process text effectively.
- **Enhancing Existing Projects**:
  - Added a **high score feature** to the Snake Game by reading and writing the high score to a file.

## Key Concepts

### 1. File Handling
- **Opening Files**:
  - Used `with open()` to safely manage file operations.
  - Explored file modes:
    - `r`: Read mode.
    - `w`: Write mode (overwrites existing content).
    - `a`: Append mode (adds to existing content without overwriting).
- **File Paths**:
  - Worked with relative paths to structure project files neatly.
  - Differentiated between absolute and relative paths.

### 2. String Manipulation
- **`replace()`**:
  - Replaced placeholders (`[name]`) in the template letter with actual names.
- **`strip()`**:
  - Removed unnecessary whitespace and newline characters from strings.
- **`readlines()`**:
  - Read file content into a list for iterative processing.

### 3. Snake Game High Score Feature
- Integrated file handling into the Snake Game to add a high score feature:
  - **Reading**: Loaded the saved high score from a file at the start of the game.
  - **Writing**: Updated the file with a new high score whenever the player beat the previous score.

## Projects Overview

### 1. Mail Merge Project
Automated the generation of personalized letters for multiple recipients:
1. Read names from `invited_names.txt`.
2. Used a template letter from `starting_letter.txt`.
3. Replaced `[name]` in the template with actual names.
4. Saved personalized letters in a structured `ReadyToSend` folder.

### 2. Snake Game Enhancement
Improved the Snake Game by adding a high score feature:
- Players' high scores are now persistent across game sessions.
- The game reads the high score from a file and updates it when the player sets a new record.

## Summary
Today's lessons reinforced practical applications of **file handling** and **string manipulation**. The Mail Merge Project demonstrated how to automate repetitive tasks, while the Snake Game enhancement added replay value by introducing a persistent high score feature. Together, these projects highlighted how file operations can significantly enhance program functionality.
