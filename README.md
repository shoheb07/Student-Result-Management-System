# Student-Result-Management-System
The Student Result Management System is a web-based application developed to manage and store student academic records efficiently. The system allows administrators or teachers to add, update, delete, and view student results in a centralized database.  

# Student Result Management System

## Project Overview
The Student Result Management System is a web-based application developed using Python Flask, HTML, CSS, and SQLite. The system helps schools and colleges manage student academic records digitally.

It allows users to:
- Add student details
- Store subject marks
- Calculate percentage automatically
- Generate grades
- View all student results
- Delete records

---

# Features

- Add Student Results
- Automatic Percentage Calculation
- Automatic Grade Generation
- View Results in Table Format
- Delete Student Records
- SQLite Database Integration
- Responsive User Interface

---

# Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python Flask

## Database
- SQLite

---

# Project Structure

Student-Result-Management-System/
│
├── app.py
├── students.db
│
├── templates/
│   ├── index.html
│   └── add_student.html
│
├── static/
│   └── style.css
│
└── README.md

---

# Installation

## Step 1: Clone Repository

git clone <repository-link>

## Step 2: Open Project Folder

cd Student-Result-Management-System

## Step 3: Install Flask

pip install flask

---

# Run Project

python app.py

---

# Open Browser

http://127.0.0.1:5000

---

# Database Schema

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no TEXT,
    name TEXT,
    subject1 INTEGER,
    subject2 INTEGER,
    subject3 INTEGER,
    total INTEGER,
    percentage REAL,
    grade TEXT
);

---

# Percentage Formula

Percentage = (Obtained Marks / Total Marks) × 100

---

# Grade System

| Percentage | Grade |
|------------|-------|
| 90 and above | A+ |
| 75 - 89 | A |
| 60 - 74 | B |
| 40 - 59 | C |
| Below 40 | F |

---

# Future Enhancements

- Student Login System
- Admin Authentication
- PDF Result Generation
- Email Notifications
- Charts and Analytics Dashboard
- Attendance Management



# Advantages

- Reduces Manual Work
- Saves Time
- Accurate Result Calculation
- Easy Data Management
- User-Friendly Interface



# Author

Your Name

Shoheb07

