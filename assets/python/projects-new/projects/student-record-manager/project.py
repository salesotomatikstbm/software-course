# =========================================
# STUDENT RECORD MANAGER (MEDIUM)
# =========================================

# Lists to store student data
student_names = []
student_classes = []
student_sections = []
student_marks = []


# -----------------------------------------
# Function: Add a new student
# -----------------------------------------
def add_student():
    print("\nAdd New Student")

    name = input("Enter student name: ")
    s_class = input("Enter class: ")
    section = input("Enter section: ")
    marks = float(input("Enter marks: "))

    student_names.append(name)
    student_classes.append(s_class)
    student_sections.append(section)
    student_marks.append(marks)

    print(name, "added successfully.")


# -----------------------------------------
# Function: View all student records
# -----------------------------------------
def view_students():
    print("\nStudent Records")

    if len(student_names) == 0:
        print("No records found.")
        return

    for i in range(len(student_names)):
        print(
            f"{i+1}. {student_names[i]} | "
            f"Class: {student_classes[i]} | "
            f"Section: {student_sections[i]} | "
            f"Marks: {student_marks[i]}"
        )


# -----------------------------------------
# Function: Search student by name
# -----------------------------------------
def search_student():
    print("\nSearch Student")

    name = input("Enter student name to search: ")

    found = False

    for i in range(len(student_names)):
        if student_names[i].lower() == name.lower():
            print(
                f"Found: {student_names[i]} | "
                f"Class: {student_classes[i]} | "
                f"Section: {student_sections[i]} | "
                f"Marks: {student_marks[i]}"
            )
            found = True
            break

    if not found:
        print("Student not found.")


# -----------------------------------------
# Function: Delete a student record
# -----------------------------------------
def delete_student():
    print("\nDelete Student")

    if len(student_names) == 0:
        print("No records to delete.")
        return

    view_students()

    index = int(input("Enter student number to delete: ")) - 1

    if 0 <= index < len(student_names):
        removed_name = student_names.pop(index)
        student_classes.pop(index)
        student_sections.pop(index)
        student_marks.pop(index)

        print(removed_name, "deleted successfully.")
    else:
        print("Invalid student number.")


# -----------------------------------------
# Function: Calculate average marks
# -----------------------------------------
def calculate_average():
    print("\nAverage Marks")

    if len(student_marks) == 0:
        print("No records available.")
        return

    total = 0

    for marks in student_marks:
        total = total + marks

    average = total / len(student_marks)

    print("Average Marks:", average)


# =========================================
# MAIN PROGRAM LOOP
# =========================================
while True:

    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Calculate Average Marks")
    print("6. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        calculate_average()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")