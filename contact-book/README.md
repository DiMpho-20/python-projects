# 📒 Contact Book

A command-line contact management application built with Python.

The application allows users to add, search, and delete contacts while storing all data in a JSON file, ensuring contacts persist between program executions.

---

## Features

- ➕ Add new contacts
- 🔍 Search contacts by name
- ❌ Delete contacts
- 💾 Automatically save contacts to a JSON file
- 📂 Automatically load saved contacts when the program starts
- 📋 Simple interactive command-line interface

---

## Project Structure

```text
contact-book/
│
├── main.py            # User interface and program entry point
├── contacts.py        # Contact management logic
├── config.py          # Configuration variables
├── contacts.json      # Stores contact data
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python 3
- JSON

---

## Concepts Practiced

This project demonstrates:

- Functions
- Modular programming
- File handling
- JSON serialization and deserialization
- Lists and dictionaries
- List comprehensions
- Exception handling
- User input validation
- CRUD operations (Create, Read, Delete)
- Importing Python modules

---

## How It Works

1. The application starts and displays a menu.
2. The user selects an option.
3. Contacts are loaded from `contacts.json`.
4. The requested operation is performed.
5. Changes are automatically saved.
6. The program continues until the user exits.

---

## Menu

```text
--- Contact Book ---

1. Add Contact
2. Search Contact
3. Delete Contact
4. Exit
```

---

## Example

### Adding a contact

```text
Choose an option: 1

Name: Neo
Phone: 0123456789
Email: neo@example.com

Contact Neo added.
```

### Searching for a contact

```text
Choose an option: 2

Search name: Neo

Name: Neo | Phone: 0123456789 | Email: neo@example.com
```

### Deleting a contact

```text
Choose an option: 3

Enter name to delete: Neo

Contact "Neo" deleted.
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DiMpho-20/contact-book.git
```

Navigate to the project folder:

```bash
cd python-projects/contact-book
```

Run the application:

```bash
python main.py
```

or

```bash
python3 main.py
```

---

## Future Improvements

- Update existing contacts
- Prevent duplicate contacts
- Validate phone numbers and email addresses
- Sort contacts alphabetically
- Search by phone number or email
- Export contacts to CSV
- Add unit tests
- Add type hints
- Build a graphical user interface (GUI)

---

## What I Learned

Building this project helped me practice:

- Designing a modular Python application
- Reading from and writing to JSON files
- Persisting data between program runs
- Working with lists and dictionaries
- Separating application logic from the user interface
- Building an interactive command-line application

---

## Author

**Dineo | https://github.com/DiMpho-20**

