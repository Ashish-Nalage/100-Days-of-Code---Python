# Day 9 - Blind Auction Project

## What I Learned
- **Dictionaries:** 
  - **Definition:** A dictionary is a collection of key-value pairs in Python.
  - **Accessing, Adding, and Editing:** Practiced accessing values using keys, adding new key-value pairs, and updating existing ones.
  - **For Loops with Dictionaries:** Learned how to loop through dictionaries, where each iteration stores the key in a variable.
- **Nested Lists and Dictionaries:** Explored creating more complex data structures by nesting lists and dictionaries.

## Project Overview
The Blind Auction program simulates an auction where multiple users can anonymously place bids. The program keeps track of each bid and identifies the highest bidder once all bids are complete.

## How It Works
1. The program continuously accepts bids until the user decides there are no more participants.
2. Each bid is stored in a dictionary with the participant's name as the key and the bid amount as the value.
3. After all bids are entered, the program identifies the highest bid and announces the winner.

## Code Highlights
- **Using Dictionaries to Store Bids:** Each bid is saved with the participant’s name as the key, making it easy to reference or update.
- **Clearing the Screen:** Added a screen-clearing effect after each entry to maintain bid confidentiality.
- **Loop to Identify the Highest Bidder:** Iterated through the dictionary to find the participant with the highest bid.

---
