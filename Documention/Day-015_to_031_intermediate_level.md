# Intermediate Level: Comprehensive Overview (Days 15–31)

This document provides a complete overview of the topics learned during the Intermediate Level of the **100 Days of Python** course. It covers every concept and feature introduced during this stage, focusing on practical usage.

---

## Object-Oriented Programming (OOP)
- **Classes and Objects**:
  - Defined classes using the `class` keyword and created objects to encapsulate attributes and methods.
  - Syntax:
    ```python
    class Dog:
        def __init__(self, name):
            self.name = name

    my_dog = Dog("Buddy")
    ```
- **Attributes**:
  - Instance attributes are defined within the `__init__` method and represent object-specific data.
- **Methods**:
  - Functions inside a class that define the behavior of an object.
  - Called using the syntax: `object.method()`.
- **Inheritance**:
  - Created child classes that inherit properties and methods from parent classes.
  - Example:
    ```python
    class Animal:
        def __init__(self, species):
            self.species = species

    class Dog(Animal):
        def bark(self):
            print("Woof!")
    ```
- **Slicing in OOP**:
  - Used list slicing for object collections, such as iterating through specific segments of data in games.

---

## Data Structures and Comprehensions
- **Tuples**:
  - Immutable sequences for storing ordered collections of data.
  - Example: `coordinates = (10, 20)`
- **List Comprehensions**:
  - Used to create new lists from iterables with concise syntax.
  - Example:
    ```python
    numbers = [x**2 for x in range(10)]
    even_numbers = [x for x in range(10) if x % 2 == 0]
    ```
- **Dictionary Comprehensions**:
  - Similar to list comprehensions but used for creating dictionaries.
  - Example:
    ```python
    squares = {x: x**2 for x in range(5)}
    ```

---

## GUI Development with Tkinter
- **Core Widgets**:
  - Learned to use `Label`, `Button`, `Entry`, `Canvas`, `Text`, `Listbox`, and more.
- **Layout Managers**:
  - Arranged widgets using:
    - `pack()`: Packs widgets vertically or horizontally.
    - `grid()`: Places widgets in a grid layout with rows and columns.
    - `place()`: Positions widgets precisely using x and y coordinates.
- **Event Handling**:
  - Used `onkey()` and button commands to interact with user input.

---

## File Handling
- **Text Files**:
  - Read, wrote, and appended data using:
    ```python
    with open("file.txt", "r") as file:
        content = file.read()
    ```
- **JSON Handling**:
  - Managed structured data using the `json` module:
    - `json.dump()`: Write data to a JSON file.
    - `json.load()`: Read data from a JSON file.
    - `json.update()`: Update or append data within a JSON object.

---

## Pandas: Data Manipulation
- **DataFrames and Series**:
  - DataFrame: Tabular data structure with rows and columns.
  - Series: 1D array-like structure.
  - Example:
    ```python
    import pandas as pd
    data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
    df = pd.DataFrame(data)
    ```
- **Loading CSV Files**:
  - Read CSV data into a DataFrame:
    ```python
    df = pd.read_csv("data.csv")
    ```
- **Exporting to CSV**:
  - Save DataFrame to a CSV file:
    ```python
    df.to_csv("output.csv", index=False)
    ```
- **DataFrame Operations**:
  - Filter rows: `df[df["column_name"] == value]`
  - Convert DataFrame to a dictionary:
    ```python
    data_dict = df.to_dict(orient="records")
    ```

---

## Exception Handling
- **try/except/else/finally**:
  - Used to handle errors gracefully:
    ```python
    try:
        file = open("data.txt")
    except FileNotFoundError:
        print("File not found!")
    else:
        content = file.read()
    finally:
        file.close()
    ```
- **Raising Exceptions**:
  - Raised errors intentionally using `raise` to handle invalid input or logic.

---

## Time Management and Scheduling
- **Tkinter Timer**:
  - Used `window.after(milliseconds, function)` to schedule repetitive tasks like countdowns or animations.

---

## Algorithms and Logic
- **Randomization**:
  - Used `random.choice()`, `random.randint()`, and `random.shuffle()` for generating random outputs.
- **Collision Detection**:
  - Implemented logical checks for overlaps or boundaries in applications like games.

---

## Clipboard Integration
- Used the `pyperclip` module to copy generated text (like passwords) to the system clipboard:
  ```python
  import pyperclip
  pyperclip.copy("Copied text")

## Miscellaneous
- **State Management**:
  - Tracked application states using global variables.
- **File Paths**:
  - Distinguished between absolute and relative paths for accessing files.

---

## Summary
The **Intermediate Level** built on foundational Python knowledge by introducing advanced concepts like OOP, comprehensions, and Pandas. These skills were combined with GUI development and file handling to create dynamic and interactive applications. This level provides a strong base for tackling real-world challenges.
