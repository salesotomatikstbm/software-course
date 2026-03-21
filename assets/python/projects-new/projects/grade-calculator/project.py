# Grade Calculator App (Fixed Subjects)

# Function to calculate result
def calculate_grade():
    print("\nEnter Marks for 5 Subjects")

    english = float(input("English: "))
    tamil = float(input("Tamil: "))
    maths = float(input("Maths: "))
    science = float(input("Science: "))
    social = float(input("Social Studies: "))

    # Total and Average
    total = english + tamil + maths + science + social
    average = total / 5

    print("\nTotal Marks:", total)
    print("Average Marks:", average)

    # Grade Calculation
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "Fail"

    # Pass / Fail
    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("Grade:", grade)
    print("Result:", result)


# Main Menu
while True:
    print("\nGrade Calculator")
    print("1. Enter Marks & Calculate Grade")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculate_grade()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")