# =========================================
# TO-DO LIST MANAGER — PHASE 1
# (With Task Completion Status)
# =========================================

# Lists to store tasks and their status
tasks = []
status = []   # "Pending" or "Done"


# -----------------------------------------
# Function: Add a new task
# -----------------------------------------
def add_task():
    print("\nAdd New Task")

    task = input("Enter task description: ")

    tasks.append(task)
    status.append("Pending")   # Default status

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
        print(f"{i+1}. {tasks[i]} — {status[i]}")


# -----------------------------------------
# Function: Mark task as completed
# -----------------------------------------
def mark_completed():
    print("\nMark Task as Completed")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    index = int(input("Enter task number to mark as done: ")) - 1

    if 0 <= index < len(tasks):
        status[index] = "Done"
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


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
        status.pop(index)

        print("Removed:", removed_task)
    else:
        print("Invalid task number.")


# =========================================
# MAIN PROGRAM LOOP
# =========================================
while True:

    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_completed()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")