# 🎓 Student Grade Calculator

A command-line application written in Python that allows users to manage student records and automatically calculate grades based on marks.

The application stores student information in a JSON file, making the data persistent between program executions.

---

## Features

- ➕ Add new students
- 📋 View all students
- 🔍 Search for a student by student number
- ❌ Delete a student
- 💾 Automatically save data to a JSON file
- 📂 Automatically load saved student records
- 🏆 Automatically calculate grades

---

## Grade Classification

| Mark | Grade |
|------:|-------|
| 0 - 49 | Fail |
| 50 - 74 | Pass |
| 75 - 100 | Distinction |

---

## Project Structure

```text
grade-calculator/
│
├── calculator.py       # Grade calculator logic
├── student.py          # Student class
├── config.py           # Application configuration
├── main.py             # Program entry point     
├── README.md
└── requirements.txt
```

---

## Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)

---

## Concepts Practiced

This project demonstrates:

- Classes and Objects
- Constructors (`__init__`)
- Methods
- Object composition
- JSON serialization
- File handling
- Exception handling
- Loops
- Conditional statements
- Modular programming
- Importing modules

---

## How It Works

1. The program starts and loads any previously saved students.
2. The user chooses an option from the menu.
3. Student information is stored as `Student` objects.
4. Grades are calculated automatically.
5. All changes are saved to `students.json`.

---

## Menu

```text
--- Student Grade Calculator ---

1. Add student
2. View all students
3. Search student
4. Delete student
5. Exit
```

---

## Example

### Adding a student

```text
Choose an option: 1

Name: Dineo
Student number: 123456
Module: Software Design
Mark: 89

Student Dineo added.
```

### Viewing students

```text
Name: Dineo | Student No: 2816258 | Module: Software Design | Mark: 89 | Grade: Distinction
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DiMpho-20/grade-calculator.git
```

Navigate to the project:

```bash
cd python-projects/grade-calculator
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

- Update student information
- Sort students by mark
- Calculate class average
- Find highest and lowest marks
- Export results to CSV
- Validate user input
- Prevent duplicate student numbers
- Unit tests

---

## What I Learned

While building this project I practiced:

- Designing classes
- Separating application logic into modules
- Working with JSON files
- Persisting data between program runs
- Building interactive command-line applications
- Applying object-oriented programming principles

---

## Author

**Dineo| https://github.com/DiMpho-20**

