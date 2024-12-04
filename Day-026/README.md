# Day 26 - List and Dictionary Comprehension, DataFrame Iterrows

## What I Learned
Today’s focus was on **comprehensions** and working with DataFrames iteratively. Key learnings include:
- **List Comprehension**:
  - A concise way to create lists from sequences or conditions.
- **Dictionary Comprehension**:
  - Create dictionaries dynamically using key-value pairs derived from iterable objects.
- **DataFrame `iterrows()`**:
  - Iterated through rows of a Pandas DataFrame to extract and manipulate data.

---

## Project Overview: NATO Phonetic Alphabet

The **NATO Phonetic Alphabet Project** converts a user-inputted word into its phonetic code equivalent using a dictionary created from a CSV file.

### Key Steps:
1. **Load Data**:
   - Read the `nato_phonetic_alphabet.csv` file into a Pandas DataFrame.
2. **Create Dictionary**:
   - Used dictionary comprehension and `iterrows()` to create a dictionary mapping letters to phonetic codes.
3. **User Interaction**:
   - Prompted the user for a word and converted it to uppercase.
   - Generated a list of phonetic codes corresponding to each letter in the input word using list comprehension.
4. **Output**:
   - Displayed the list of phonetic codes.

---

## Summary
Today’s project showcased the power of **comprehensions** and **DataFrame iteration** to streamline tasks. The NATO Phonetic Alphabet Project combined file handling, Pandas operations, and user interaction to create a practical and efficient application.
