# Day 25 - Working with CSV Files and Data Analysis Using Pandas

## What I Learned
Today's focus was on mastering the **Pandas** module for working with CSV files and performing data analysis. Key learnings include:
- **Reading CSV Files**: Used `pandas.read_csv()` to load data into a **DataFrame**.
- **Understanding DataFrame and Series**:
  - **DataFrame**: A 2D table-like data structure with rows and columns.
  - **Series**: A one-dimensional array of data.
- **DataFrame Operations**:
  - Extract columns and rows using labels or conditions.
  - Convert DataFrames and Series to other data types like lists or dictionaries.
- **Creating CSV Files**: Used `pandas.DataFrame.to_csv()` to save analyzed data into a CSV file.

---

## Projects Overview

### Project 1: Central Park Squirrel Data Analysis
Analyzed the **2018 Central Park Squirrel Census** dataset to count the number of squirrels by their primary fur color and saved the results in a new CSV file.

#### Key Steps:
1. **Load Data**:
   - Used `pandas.read_csv()` to load the dataset.
2. **Analyze Data**:
   - Filtered rows based on fur color (`Gray`, `Cinnamon`, `Black`) and counted the occurrences.
3. **Create Summary**:
   - Organized the data into a dictionary and converted it into a **DataFrame**.
4. **Save Results**:
   - Exported the summary data as a CSV file (`squirrel_count.csv`).

---

### Project 2: U.S. States Game
Built an interactive game where the user identifies U.S. states on a map. Missing states are saved in a CSV file for further learning.

#### Key Features:
1. **User Input**:
   - Collected user guesses using `screen.textinput()` and displayed correctly guessed states on the map.
2. **State Verification**:
   - Matched user input with state names in the CSV file.
   - Checked for duplicates and ignored case sensitivity using `.title()`.
3. **Interactive Map**:
   - Displayed state names on the map at their respective coordinates using the Turtle module.
4. **Learning Enhancement**:
   - Saved unguessed states in a CSV file (`states_to_learn.csv`) for the user to review.

---

## Summary
These projects provided hands-on experience with **Pandas** for reading, analyzing, and writing CSV files. The **Central Park Squirrel Data Analysis** project focused on data manipulation and summarization, while the **U.S. States Game** showcased how to integrate data analysis with interactive visual elements. Together, these projects reinforced skills in working with structured data and building engaging, data-driven applications.
