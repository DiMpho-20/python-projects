#💵Expense Tracker
A command-line application written in Python that allows users to manage their expenses.


The application stores user's expense information in a JSON file, making the data persistent between program executions.


# 💰 Expense Tracker

A command-line expense tracking application built with Python that allows users to record, manage, and analyze their personal expenses.

The application stores expenses in a JSON file, making data persistent between program executions while automatically recording the date of each expense.

---
## ✨ Features

- ➕ Add new expenses
- 📋 View all recorded expenses
- ❌ Delete an expense by ID
- 📅 Generate monthly expense reports
- 💵 Calculate total money spent
- 💾 Automatically save expenses to a JSON file
- 📂 Automatically load saved expenses
- 🗓️ Automatically record the current date
- ✅ Input validation for user entries

---

## 📂 Project Structure

```text
expense-tracker/
│
├── config.py          # Configuration settings
├── expense.py         # Expense model
├── tracker.py         # Expense tracker logic
├── main.py            # Program entry point
├── my_expenses.json   # Expense data (ignored by Git)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- JSON
- datetime
- Object-Oriented Programming (OOP)

---

## 📚 Concepts Practiced

This project demonstrates:

- Classes and Objects
- Constructors (`__init__`)
- Methods
- Lists
- Dictionaries
- File Handling
- JSON Serialization
- Date Handling
- Modular Programming
- Data Persistence

---

## ⚙️ How It Works

1. The program loads previously saved expenses.
2. The user selects an option from the menu.
3. Expenses are stored as `Expense` objects.
4. Each expense is automatically assigned:
   - A unique ID
   - The current date
5. All changes are saved to `my_expenses.json`.

---

## 📋 Menu

```text
--------- Expenses ---------

1. Add Expense
2. View All Expenses
3. Delete Expense
4. Monthly Report
5. Total Spent
6. Exit
```

---

## 💡 Example

### Adding an expense

```text
Choose an option: 1

Amount: 120
Category: Food
Description: Lunch

Expense added successfully.
```

### Viewing expenses

```text
ID: 1 | 2026-07-16 | Food | R120 | Lunch
```

### Monthly report

```text
--- Monthly Report: Month 07 ---

Food: R520
Transport: R180
Entertainment: R250

Total: R950
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DiMpho-20/python-projects.git
```

Navigate to the project:

```bash
cd python-projects/expense-tracker
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

## 🔮 Future Improvements

- ✏️ Edit an existing expense
- 🔍 Search expenses by category
- 📅 Search expenses by date
- 📊 Export reports to CSV
- 📈 Generate spending charts
- 💰 Budget tracking
- 🔁 Support recurring expenses
- 🧪 Add unit tests

---

## 📈 Skills Demonstrated

- Object-Oriented Programming
- JSON Data Storage
- File Handling
- Date Management
- Data Aggregation
- Command-Line Interface Development

---

## 👨‍💻 Author

**Dineo**

