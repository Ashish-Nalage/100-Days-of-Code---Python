# Day 17 - Object-Oriented Programming (OOP): Quiz Game Project

## What I Learned
Today's lessons focused on core Object-Oriented Programming (OOP) concepts in Python:
- **Defining a Class**: A blueprint for creating objects, with attributes (data) and methods (functions).
- **Class Naming Convention**: Using Pascal Case (e.g., `QuizBrain`, `Question`) for class names.
- **`__init__` Method**: Special method to initialize an object's attributes when an instance is created.
- **Attributes**: Variables defined within a class to store object-specific data.
- **Methods**: Functions inside a class that define the object's behavior and interact with its attributes.

## Key Concepts
1. **Classes and Objects**:
   - **Class**: Defines the structure and behavior of objects.
   - **Object**: An instance of a class with its own set of attribute values.

2. **Attributes and Initialization**:
   - **Attributes** are properties of an object, defined in the class using the `__init__` method.
   - Attributes are set when creating an object, allowing for customized object instances.

3. **Methods in a Class**:
   - Methods define the actions or behaviors of an object. They can access and modify object attributes, perform operations, and provide outputs.
   - Common methods in the `QuizBrain` class include:
     - **`next_question()`**: Displays the current question and prompts the user for an answer.
     - **`check_answer()`**: Compares the user's input with the correct answer and updates the score.

## Project Overview: Quiz Game
The project involves building a simple True/False quiz game using OOP principles, structured as follows:

1. **Question Class**:
   - Represents each quiz question with attributes for the text and the correct answer.

2. **QuizBrain Class**:
   - Manages the quiz flow, tracking the question number, displaying questions, and checking user answers.
   - Handles user interaction and score updates throughout the quiz.

3. **Main Program Flow**:
   - Creates a list of `Question` objects using predefined data.
   - Initializes the `QuizBrain` object with this list.
   - Runs a loop to display questions until all have been answered.

## Benefits of Using OOP
- **Modularity**: Code is organized into self-contained classes, making it easier to understand and maintain.
- **Reusability**: Encapsulated logic can be reused across different projects or extended with new features.
- **Maintainability**: Clear structure with methods handling specific tasks, making the code easier to debug and update.

## Summary
This project provided hands-on experience with OOP concepts in Python. I learned how to:
- Define and initialize classes using the `__init__` method.
- Create and manage objects with specific attributes.
- Implement methods to interact with object attributes and handle user input.
- Structure a program using multiple classes for better organization and readability.

Overall, applying OOP principles improved the modularity and maintainability of the code, making it a great approach for building scalable projects.
