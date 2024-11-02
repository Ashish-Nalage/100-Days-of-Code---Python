# Day 8 - Caesar Cipher

## What I Learned
- **Functions with Input:** Created functions that accept inputs, allowing for modular and reusable code.
- **Arguments vs. Parameters:** 
  - **Parameter**: The variable name defined in the function signature.
  - **Argument**: The actual value passed to the function when it’s called.
- **Modular Arithmetic**: Learned how to use the modulus operator to wrap around the alphabet when shifting letters.
- **Input Validation**: Gained experience in handling user input and providing feedback based on the choices made.

## Project Overview
The Caesar Cipher project implements a simple encryption technique where each letter in the plaintext is shifted by a fixed number of places down or up the alphabet. This is a fun way to explore basic cryptography concepts and string manipulation in Python.

## How It Works
- The user can choose to either encode or decode a message.
- The program asks for the text input and the shift number to determine how many letters to shift.
- It processes each letter in the input text, shifting it according to the specified amount while maintaining any non-alphabetic characters.
- The result is displayed to the user, and they can choose to perform another operation.

## Code Highlights
- Created the `caesar` function, which handles both encoding and decoding based on the user’s choice.
- Used loops and modular arithmetic to manage the letter shifts.
- Implemented input handling to allow the user to run multiple rounds of encoding or decoding until they choose to exit.
