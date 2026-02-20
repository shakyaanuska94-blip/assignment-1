import json
import csv

file_name = "std.json"

# Load existing data
try:
    with open(file_name, "r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

# -------- Grade Function --------
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

# -------- Roll Validation Function --------
def get_valid_roll():
    while True:
        roll = input("Enter Roll Number (numbers only): ")
        if roll.isdigit():
            return roll
        else:
            print("❌ Invalid Roll Number! Only numbers allowed.")

# -------- Add Student --------
def add_student():
    roll = get_valid_roll()
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

    print("✅ Student Added Successfully!")

# -------- View Students --------
def view_students():
    if not students:
        print("No student records found!")
        return

    print("\nAll Students:")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")

# -------- Search Student --------
def search_student():
    roll = get_valid_roll()

    for s in students:
        if s['roll'] == roll:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
            return

    print("Student not found!")

# -------- Delete Student --------
def delete_student():
    roll = get_valid_roll()

    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            with open(file_name, "w") as file:
                json.dump(students, file, indent=4)
            print("Student deleted successfully!")
            return

    print("Student not found!")

# -------- Update Marks --------
def update_marks():
    roll = get_valid_roll()

    for s in students:
        if s['roll'] == roll:
            try:
                new_marks = int(input("Enter New Marks: "))
            except:
                new_marks = 0
                print("Invalid input! Marks set to 0.")

            s['marks'] = new_marks
            s['grade'] = calculate_grade(new_marks)

            with open(file_name, "w") as file:
                json.dump(students, file, indent=4)

            print("Marks Updated Successfully!")
            return

    print("Student not found!")

# -------- Topper List --------
def topper_list():
    if not students:
        print("No student records found!")
        return

    sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)

    print("\nTopper List:")
    for s in sorted_students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")

# -------- Export CSV --------
def export_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["roll", "name", "marks", "grade"])
        for s in students:
            writer.writerow([s['roll'], s['name'], s['marks'], s['grade']])

    print("Exported to students.csv successfully!")

# -------- MAIN PROGRAM --------

print("Welcome to Student Management System")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Topper List")
    print("7. Export to CSV")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_marks()

    elif choice == "6":
        topper_list()

    elif choice == "7":
        export_csv()

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")