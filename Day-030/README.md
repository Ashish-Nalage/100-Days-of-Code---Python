# Day 30 - Enhanced Password Manager and Exception Handling

## What I Learned
Today's focus was on improving the Password Manager by integrating **JSON file handling** and exploring **exception handling**. Key learnings include:

### 1. Exception Handling
- **`try`/`except`/`else`/`finally` Blocks**:
  - Managed errors gracefully by handling exceptions like `FileNotFoundError` and `KeyError`.
  - Used `else` to execute code if no exceptions occurred.
  - Leveraged `finally` for clean-up actions, ensuring consistent behavior.

- **Raising Errors**:
  - Learned how to use `raise` to create custom exceptions for specific scenarios, such as invalid BMI calculations.

### 2. JSON File Handling
- **Read and Write Operations**:
  - Used `json.load()` to read data from a JSON file and convert it into a Python dictionary.
  - Applied `json.dump()` to save updated data back to the JSON file in a structured format.

- **Data Persistence**:
  - Enhanced the Password Manager to persist data across sessions, storing credentials in `data.json`.

- **Search Functionality**:
  - Implemented a search feature to retrieve saved credentials based on the website name.
  - Displayed the results in a pop-up and copied the password to the clipboard.

---

## Project Overview: Enhanced Password Manager

### Features:
1. **Password Generation**:
   - Generates secure passwords with a mix of letters, numbers, and symbols.
   - Automatically copies the password to the clipboard.

2. **Data Storage and Retrieval**:
   - Saves website credentials (website, email, password) in a JSON file.
   - Updates existing data without overwriting previous entries.
   - Searches for stored credentials by website name and displays the results.

3. **Error Handling**:
   - Handles missing files (`FileNotFoundError`) by creating a new JSON file.
   - Provides user-friendly warnings when no data or invalid inputs are found.

4. **Interactive UI**:
   - Clean and functional interface using Tkinter widgets (`Entry`, `Button`, `Label`).
   - Added a **Search** button for quick credential lookup.

---

## Summary
Today’s project showcased the importance of **exception handling** for robust application design and introduced **JSON** as a tool for managing persistent data. The enhanced Password Manager is now a more complete application, integrating secure password generation, storage, and retrieval with a user-friendly interface.


