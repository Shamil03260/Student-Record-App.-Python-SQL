# Student Management System (Python + SQLite)

This is a **Student Management System** written in **Python** using **SQLite** for data storage. It allows admins, teachers, and students to manage and view student records, including grades and statistics.

> **Note:** The original version of this program was implemented **without SQL**, using only Python dictionaries. This updated version now leverages **SQLite** to store and manage student data, making it more robust and persistent.

---

## Features

- **Admin Panel**
  - Add new students
  - View all students
  - Delete students by ID or Name
  - Show average score of all students
  - View top and lowest scoring students

- **Teacher Panel**
  - Add new students
  - View all students
  - Show average score
  - View top and lowest scoring students

- **Student Panel**
  - View all students
  - Show average score
  - View top and lowest scoring students

- **Automatic Letter Grade**
  - Scores are automatically converted into letter grades (A-F) when added.

---

## Technologies Used

- **Python 3**
- **SQLite3** (built-in Python library)
- **Statistics module** for calculating averages

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Shamil03260/Student-Record-App.-Python-SQL.git
    ```

2. Navigate to the project folder:
    ```bash
    cd student-management-system
    ```

3. Run the program:
    ```bash
    python student_system_sql.py
    ```

> The program will automatically create a SQLite database (`school2.db`) in the same directory if it doesn't exist.

---

## Usage

1. Run the program.
2. Select your role:
   - **Admin**: Password is `123qwerty`
   - **Teacher**: Password is `1234`
   - **Student**: Enter your name to log in
3. Follow the on-screen menu to add, view, delete students or check statistics.
4. Exit by choosing the "Exit" option in the menus.

---

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade INTEGER,
    score INTEGER,
    letter TEXT
);
