import json
from pathlib import Path

#STUDENT MANAGEMENT SYSTEM

STUDENTS_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not STUDENTS_FILE.exists():
        return {}

    with STUDENTS_FILE.open("r", encoding="utf-8") as file:
        students_data = json.load(file)

    if not isinstance(students_data, dict):
        raise ValueError("students.json must contain a JSON object.")

    return students_data


def save_students():
    with STUDENTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

#Store student records
students = load_students()

#Display the main menu
def display_menu():
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add a student")
    print("2. Add/update grades")
    print("3. View one student")
    print("4. View all students")
    print("5. Calculate average grade")
    print("6. Find highest/lowest grade")
    print("7. Remove a student")
    print("8. Exit")

#Add a student
def add_student():

     name = input("Enter student name: ") . strip()

     if name == "":
            print("Student name cannot be empty.")
     elif name in students:
            print("Student already exists.")
     else:
            students[name] = []
            save_students()
            print("Student added successfully.")

#Add or update grades
def add_grade():
    name = input("Enter student name: ").strip()

    if name not in students:
        print("Student not found.")
    else:
        try:
            grade = float(input("Enter grade (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if 0 <= grade <= 100:
            students[name].append(grade)
            save_students()
            print("Grade added successfully.")
        else:
            print("Grade must be between 0 and 100.")

#view one student
def view_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print("student name:", name)
        print("grades:", students[name])
    else:
        print("student not found.")

#View all students
def view_all_students():
    if not students:
        print("No students found.")
    else:
        for name, grades in students.items():
            print("student name:" , name)
            print("grades:" , grades)
          
#Calculate average grade
def calculate_average():
    if not students:
        print("No students found.")
        return

    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)

    if not all_grades:
        print("no grades available.")
        return
    average = sum(all_grades) / len(all_grades)
    print("average grade:", average)

#Find highest and lowest grades
def find_highest_lowest():
    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)

    if not all_grades:
        print("no grades available.")
        return

    print("Highest grade:",
    max(all_grades))
    print("Lowest grade:",
    min(all_grades))

#Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    if name in students:
        del students[name]
        save_students()
        print("Student removed successfully.")
    else:
        print("Student not found.")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
          add_grade()
    elif choice == "3":
        view_student()
    elif choice == "4":
        view_all_students()
    elif choice == "5":
        calculate_average()
    elif choice == "6":
        find_highest_lowest()
    elif choice == "7":
        remove_student()
    elif choice == "8":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")

        

        

