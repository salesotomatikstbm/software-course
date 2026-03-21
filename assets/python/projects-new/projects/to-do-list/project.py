# =========================================
# TO-DO LIST MANAGER (MEDIUM)
# =========================================

# List to store tasks
tasks = []


# -----------------------------------------
# Function: Add a new task
# -----------------------------------------
def add_task():
    print("\nAdd New Task")

    task = input("Enter task description: ")
    tasks.append(task)

    print("Task added successfully.")


# -----------------------------------------
# Function: View all tasks
# -----------------------------------------
def view_tasks():
    print("\nYour Tasks")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")


# -----------------------------------------
# Function: Remove a task
# -----------------------------------------
def remove_task():
    print("\nRemove Task")

    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    view_tasks()

    index = int(input("Enter task number to remove: ")) - 1

    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print("Removed:", removed_task)
    else:
        print("Invalid task number.")


# -----------------------------------------
# Function: Clear all tasks
# -----------------------------------------
def clear_tasks():
    print("\nClear All Tasks")

    if len(tasks) == 0:
        print("No tasks to clear.")
    else:
        tasks.clear()
        print("All tasks cleared.")


# =========================================
# MAIN PROGRAM LOOP
# =========================================
while True:

    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        clear_tasks()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")