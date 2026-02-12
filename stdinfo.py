print("Welocme to Student Management System")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("\nLogin successful")
    print("Role: Admin")

    print("1. select Student")
    print("2. Delete Student")
    print("3. Update Mark")
    print("4. View/search student")
    print("5. Sorting & Topper list")
    print("6. Export to CSV")
    
elif username == "user" and password == "user123":
    print("\nLogin sucessful")
    print("Role: user")
    
    print("1. View/Search Stusents")
    print("2. Sorting & Topper List")

else:
    print("Invalid username or password")