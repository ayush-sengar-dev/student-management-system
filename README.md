# Student Management System

A console-based student management and college portal application built using Python and MySQL.

**Created by Ayush Sengar**

## Features

- Student login and authentication
- Student details
- Subject-wise attendance
- Overall attendance calculation
- Results and grade information
- Fee management
- Optional services
  - Transport
  - Hostel
  - Mess
  - Canteen
- Timetable
- Notices module placeholder

## Tech Stack

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv

## Project Structure

```text
student_management_system/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── student_management_db.sql
├── README.md
│
├── main.py
├── database.py
├── student.py
├── attendance.py
├── results.py
├── fees.py
├── timetable.py
└── notices.py

`.env` is required for local database configuration but is intentionally excluded from the repository for security reasons. Use `.env.example` as a template.
```

## Author

**Ayush Sengar**

This project was designed and developed by me as a Python + MySQL "student management system" project.
