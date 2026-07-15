# 📂 File Organizer
A Python command-line application that automatically organizes files into folders based on their file extensions.
Instead of manually sorting your Downloads folder, this program categorizes files such as images, videos, documents, music, archives, and source code into separate folders.
---
## Features
- 📁 Organizes files automatically
- 🖼️ Supports image files
- 🎥 Supports video files
- 🎵 Supports music files
- 📄 Supports documents
- 📦 Supports archives
- 💻 Supports source code files
- 📂 Creates folders automatically if they do not exist
- 📋 Places unknown file types into an **Others** folder
---
## Project Structure
```text
file-organizer/
│
├── config.py          # File type configuration
├── organizer.py       # File organization logic
├── main.py            # Program entry point
├── README.md
├── requirements.txt
└── .gitignore
```
---
## Technologies Used
- Python 3
- os
- shutil
---
## Concepts Practiced
This project demonstrates:
- Functions
- Dictionaries
- Loops
- File handling
- Python modules
- Importing modules
- Path manipulation
- Conditional statements
- Modular project structure
---
## How It Works
The program:
1. Asks the user for a folder path.
2. Reads every file in that folder.
3. Determines each file's extension.
4. Matches the extension to a category.
5. Creates the destination folder if needed.
6. Moves the file into the correct folder.
---
## Supported Categories
| Category | Examples |
|----------|----------|
| Images | .jpg, .png, .gif, .jpeg |
| Videos | .mp4, .mkv, .avi |
| Music | .mp3, .wav, .flac |
| Documents | .pdf, .docx, .txt |
| Archives | .zip, .rar, .7z |
| Code | .py, .java, .cpp, .html |
| Others | Any unsupported file type |
---
## Installation
Clone the repository:
```bash
git clone https://github.com/DiMpho-20/file-organizer.git
```
Navigate into the project:
```bash
cd file-organizer
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
## Example
Before:
```text
Downloads/
├── cat.jpg
├── resume.pdf
├── song.mp3
├── project.zip
└── hello.py
```
After:
```text
Downloads/
├── Images/
│   └── cat.jpg
│
├── Documents/
│   └── resume.pdf
│
├── Music/
│   └── song.mp3
│
├── Archives/
│   └── project.zip
│
└── Code/
    └── hello.py
```
---
## Future Improvements
- Recursive folder organization
- Rename duplicate files automatically
- Undo the last organization
- Organize files by date
- Command-line arguments
- Logging
- Dry-run mode
- Unit tests
---
## Author
**Dineo**