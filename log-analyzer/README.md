# 📊 Log Analyzer

A Python command-line application that analyzes log files and provides useful summaries. This project demonstrates file handling, object-oriented programming (OOP), dictionaries, string manipulation, and basic data analysis in Python.

---

## ✨ Features

- Count the number of:
  - ERROR logs
  - WARNING logs
  - INFO logs
- Find the most common error message.
- Determine which hour had the most errors.
- Filter and display logs by level (ERROR, WARNING, INFO).
- Read log data directly from a text file.

---

## 📂 Project Structure

```
log-analyzer/
│── README.md
│── analyzer.py
│── config.py
│── main.py
│── sample.log
└── requirements.txt
```

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (Classes)
- File Handling
- Dictionaries
- String Manipulation

---

## 🚀 How to Run

1. Clone the repository.

```bash
git clone https://github.com/DiMpho-20/python-projects.git
```

2. Navigate to the project.

```bash
cd python-projects/log-analyzer
```

3. Run the program.

```bash
python3 main.py
```

---

## 📖 Sample Log Format

The program expects log entries in the following format:

```text
2026-07-10 08:23:11 ERROR Database connection failed
2026-07-10 08:45:02 INFO Server started
2026-07-10 09:12:33 WARNING High memory usage
2026-07-10 09:15:44 ERROR Timeout on request
```

---

## 📋 Menu

```
----- Log Analyzer -----

1. View log summary
2. Count log levels
3. Most common error
4. Hour with most errors
5. Filter by level
6. Exit
```

---

## 📚 Concepts Practiced

- Reading text files
- Object-Oriented Programming
- Classes and methods
- Dictionaries
- Counting frequencies
- String methods (`split()`, `join()`, `strip()`)
- Loops and conditionals
- Building command-line applications

---

## 📄 License

This project is licensed under the MIT License.