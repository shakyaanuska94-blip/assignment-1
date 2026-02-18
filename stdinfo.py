import json
file_name = "std.json"
try:
    with open(file_name,"r")as file:
        student = json.load(flie)
except:
    students = []

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else :
        return "F"

print("Welocme to Student Management System")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("\nLogin successful")
    print("Role: Admin")

    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Mark")
    print("4. View/search student")
    print("5. Sorting & Topper list")
    print("6. Export to CSV")

    choice=input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = int(input("Enter marks: "))

        grade = calculate_grade(marks)
        print("Student grade is:", grade)

        student = {
            "roll": roll,
            "name": name,
            "marks": marks,
            "grade": grade

        }

        students.append(student)
        with open(file_name,"w") as file:
            json.dump(students,file)
        print("File created and data saved!")
        print("Student Added Successfully ! ")
    
elif username == "user" and password == "user123":
    print("\nLogin sucessful")
    print("Role: user")
    
    print("1. View/Search Stusents")
    print("2. Sorting & Topper List")

else:
    print("Invalid username or password")