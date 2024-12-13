# Day 29 - Password Manager with Tkinter

## What I Learned
Today, I built a **Password Manager** application using Tkinter and Python. The project focused on creating a practical tool to securely generate, store, and manage passwords. Key learnings include:
- **File Handling**:
  - Opened a file in append mode to store website credentials.
  - Ensured data is written persistently for future reference.
- **Messagebox Integration**:
  - Used `messagebox.showwarning()` to display warnings for empty fields.
  - Implemented `messagebox.askokcancel()` to confirm user actions.
- **Password Generation**:
  - Utilized `random` module (`choice`, `randint`, `shuffle`) to generate secure passwords with a mix of letters, numbers, and symbols.
  - Leveraged **list comprehension** for efficient password generation.
- **Clipboard Integration**:
  - Used the `pyperclip` module to automatically copy the generated password to the clipboard.

---

## Project Overview: Password Manager

### Features:
1. **Password Generation**:
   - Generates strong passwords using random letters, numbers, and symbols.
   - Automatically copies the password to the clipboard for convenience.
   
2. **Data Storage**:
   - Saves website credentials (website, email, password) in a local text file (`data.txt`).
   - Ensures each entry is stored on a new line.

3. **Interactive UI**:
   - Uses **Tkinter widgets** like `Entry`, `Label`, and `Button` for a clean user interface.
   - Automatically focuses the cursor on the website input field after saving.

4. **Validation**:
   - Displays a warning if required fields are left empty.
   - Prompts the user for confirmation before saving data.

---

## Summary
The **Password Manager** project provided hands-on experience in integrating GUI development with backend logic. Key takeaways include working with file operations, creating dynamic UI interactions, and generating secure passwords. This tool is a practical application of Python for enhancing personal productivity and security.
