import json
import csv

file_name = "std.json"

# Load existing students or create empty list
try:
    with open(file_name, "r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

# --- Grading function ---
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# --- View all students ---
def view_students():
    if not students:
        print("No student records found!")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")

# --- Search student by roll ---
def search_students(roll):
    for s in students:
        if s['roll'] == roll:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
            return
    print("Student not found!")

# --- Delete student ---
def delete_students(roll):
    global students
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            with open(file_name, "w") as file:
                json.dump(students, file, indent=4)
            print("Student deleted successfully!")
            return
    print("Student not found!")

# --- Update student marks ---
def update_students_marks(roll, new_marks):
    for s in students:
        if s['roll'] == roll:
            s['marks'] = new_marks
            s['grade'] = calculate_grade(new_marks)
            with open(file_name, "w") as file:
                json.dump(students, file, indent=4)
            print("Marks updated successfully!")
            return
    print("Student not found!")

# --- Topper list ---
def topper_list():
    if not students:
        print("No student records found!")
        return
    sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)
    print("\nTopper List:")
    for s in sorted_students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")

# --- Export to CSV ---
def export_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["roll", "name", "marks", "grade"])
        for s in students:
            writer.writerow([s['roll'], s['name'], s['marks'], s['grade']])
    print("Data exported to students.csv successfully!")

# ---------------- MAIN PROGRAM ---------------- #

print("Welcome to Student Management System")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("\nLogin successful")
    print("Role: Admin")

    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Update Marks")
        print("4. View/Search Students")
        print("5. Sorting & Topper List")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")

            try:
                marks = int(input("Enter Marks: "))
            except:
                marks = 0
                print("Invalid input! Marks set to 0.")

            student = {
                "roll": roll,
                "name": name,
                "marks": marks,
                "grade": calculate_grade(marks)
            }

            students.append(student)

            with open(file_name, "w") as file:
                json.dump(students, file, indent=4)

            print("Student Added Successfully!")

        elif choice == "2":
            roll = input("Enter Roll Number to delete: ")
            delete_students(roll)

        elif choice == "3":
            roll = input("Enter Roll Number to update marks: ")
            try:
                new_marks = int(input("Enter new Marks: "))
            except:
                new_marks = 0
                print("Invalid input! Marks set to 0.")
            update_students_marks(roll, new_marks)

        elif choice == "4":
            roll = input("Enter Roll Number to search: ")
            if roll:
                search_students(roll)
            else:
                view_students()

        elif choice == "5":
            topper_list()

        elif choice == "6":
            export_csv()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

elif username == "user" and password == "user123":
    print("\nLogin successful")
    print("Role: User")

    print("1. View/Search Students")
    print("2. Sorting & Topper List")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number to search (or leave blank to view all): ")
        if roll:
            search_students(roll)
        else:
            view_students()

    elif choice == "2":
        topper_list()

else:
    print("Invalid username or password")