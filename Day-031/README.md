# Day 31 - Flash Card App with Tkinter and Pandas

## What I Learned
Today's focus was on creating a **Flash Card App** to aid in learning French-English vocabulary. Key learnings include:
- **File Handling with Pandas**:
  - Used `pandas.read_csv()` to load vocabulary data from a CSV file.
  - Saved progress by updating and exporting a new CSV file (`words_to_learn.csv`).
- **Data Manipulation**:
  - Converted a DataFrame to a list of dictionaries for dynamic data handling.
  - Removed known words from the data and saved the updated list for future sessions.
- **Interactive Timed UI**:
  - Used `window.after()` to implement a 3-second timer for flipping flashcards.
  - Dynamically updated the card content (word and translation) and styling based on user actions.
- **Error Handling**:
  - Implemented `try/except` to handle missing files gracefully, creating new progress files as needed.

---

## Project Overview: Flash Card App

### Features:
1. **Flash Card Functionality**:
   - Displays a French word on the front of the card.
   - Flips to show the English translation after 3 seconds.

2. **Progress Tracking**:
   - Tracks known words and removes them from the review list.
   - Saves the remaining words to `words_to_learn.csv`, ensuring persistent progress across sessions.

3. **Dynamic UI**:
   - Used a canvas to display images and text for the flashcards.
   - Integrated "Right" and "Wrong" buttons with image icons for user interaction.

4. **User Feedback**:
   - Notifies the user when all words have been learned.
   - Deletes the progress file when no words remain.

---

## Summary
The Flash Card App is a practical tool for vocabulary learning. It combines file handling, data manipulation, and an interactive GUI to create a personalized and efficient learning experience. The integration of progress tracking ensures that users can resume their learning journey seamlessly.



