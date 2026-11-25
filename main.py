 #STUDENT MANAGEMENT SYSTEM

#Store student records
students = {}


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
            print("Grade added successfully.")
        else:
            print("Grade must be between 0 and 100.")

          
     

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
          add_grade()
    elif choice == "8":
        print("Thank you for using the Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")

        

