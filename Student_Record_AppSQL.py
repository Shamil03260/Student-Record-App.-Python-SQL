import statistics
import sqlite3


conn = sqlite3.connect('school2.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade INTEGER,
    score INTEGER,
    letter TEXT
)
""")


def add_student():
    name = input("Name: ").capitalize()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return
    try:
        grade = int(input("Grade: "))
    except ValueError:
        print("Invalid grade.")
        return
    try:
        score = int(input("Score: "))
    except ValueError:
        print("Invalid score.")
        return

    # ===== LETTER GRADE =====
    if score >= 91:
        letter = "A"
    elif score >= 81:
        letter = "B"
    elif score >= 71:
        letter = "C"
    elif score >= 61:
        letter = "D"
    elif score >= 51:
        letter = "E"
    else:
        letter = "F"

    cursor.execute(
        "INSERT INTO students (name, age, grade, score, letter) VALUES (?, ?, ?, ?, ?)",
        (name, age, grade, score, letter)
    )

    conn.commit()
    print("Student added successfully!")


def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("Student list is empty.")
    else:
        print("--- STUDENTS ---")
        for s in students:
            print("ID:", s[0])
            print("Name:", s[1])
            print("Age:", s[2])
            print("Grade:", s[3])
            print("Score:", s[4])
            print("Letter:", s[5])
            print("----------------")


def delete_student():
    cursor.execute("SELECT * FROM students")
    all_students = cursor.fetchall()
    if not all_students:
        print("Student list is empty.")
        return

    choice = input("Delete by ID or Name? (Enter 'ID' or 'Name'): ").lower()

    if choice == 'id':
        try:
            student_id = int(input("Enter the ID you want to delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        result = cursor.fetchall()

        if result:
            for s in result:
                print("Deleted - Name:", s[1], ", Age:", s[2])
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
        else:
            print("Student not found.")

    elif choice == 'name':
        student_name = input("Enter the name you want to delete: ").capitalize()
        if not student_name.isalpha():
            print("Invalid name.")
            return

        cursor.execute("SELECT * FROM students WHERE name = ?", (student_name,))
        result = cursor.fetchall()

        if result:
            for s in result:
                print("Deleted - Name:", s[1], ", Age:", s[2])
            cursor.execute("DELETE FROM students WHERE name = ?", (student_name,))
            conn.commit()
        else:
            print("Student not found.")

    else:
        print("Invalid choice.")


def mean_students():
    cursor.execute("SELECT score FROM students")
    scores = [s[0] for s in cursor.fetchall()]

    if not scores:
        print("The list is empty.")
    else:
        print("Average score:", statistics.mean(scores))


def statistics_student():
    cursor.execute("SELECT name, score FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("The list is empty.")
    else:
        best = max(rows, key=lambda x: x[1])
        worst = min(rows, key=lambda x: x[1])

        print("Top student:")
        print("Name:", best[0])
        print("Score:", best[1])

        print("Lowest student:")
        print("Name:", worst[0])
        print("Score:", worst[1])


while True:
    print("--- STUDENT SYSTEM ---")
    print("1. Admin")
    print("2. Teacher")
    print("3. Student")
    print("4. Exit")

    choice1 = input("Select an option: ")

    if choice1 == "1":
        password = input("Password: ")
        if password != "123qwerty":
            print("Incorrect password!")
        else:
            while True:
                print("--- ADMIN MENU ---")
                print("1. Add student")
                print("2. View students")
                print("3. Delete student")
                print("4. Show average score")
                print("5. Show statistics")
                print("6. Exit")

                choice = input("Select an option: ")

                if choice == "1":
                    add_student()
                elif choice == "2":
                    show_students()
                elif choice == "3":
                    delete_student()
                elif choice == "4":
                    mean_students()
                elif choice == "5":
                    statistics_student()
                elif choice == "6":
                    print("Exiting admin menu...")
                    break
                else:
                    print("Invalid choice.")

    elif choice1 == "2":
        password = input("Password: ")
        if password != "1234":
            print("Incorrect password!")
        else:
            while True:
                print("--- TEACHER MENU ---")
                print("1. Add student")
                print("2. View students")
                print("3. Show average score")
                print("4. Show statistics")
                print("5. Exit")

                choice = input("Select an option: ")

                if choice == "1":
                    add_student()
                elif choice == "2":
                    show_students()
                elif choice == "3":
                    mean_students()
                elif choice == "4":
                    statistics_student()
                elif choice == "5":
                    print("Exiting teacher menu...")
                    break
                else:
                    print("Invalid choice.")

    elif choice1 == "3":
        cursor.execute("SELECT * FROM students")
        all_students = cursor.fetchall()

        if not all_students:
            print("No students have been added yet.")
        else:
            name = input("Name: ").capitalize()
            cursor.execute("SELECT name FROM students WHERE name = ?", (name,))
            if cursor.fetchone() is None:
                print("Name not found.")
            else:
                while True:
                    print("--- STUDENT MENU ---")
                    print("1. View students")
                    print("2. Show average score")
                    print("3. Show statistics")
                    print("4. Exit")

                    choice = input("Select an option: ")

                    if choice == "1":
                        show_students()
                    elif choice == "2":
                        mean_students()
                    elif choice == "3":
                        statistics_student()
                    elif choice == "4":
                        print("Exiting student menu...")
                        break
                    else:
                        print("Invalid choice.")

    elif choice1 == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")

conn.close()
