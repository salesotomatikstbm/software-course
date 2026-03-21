
import tkinter as tk
from tkinter import ttk, messagebox


# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------
def reset_form():
    task_name_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    important_var.set("No")
    due_entry.delete(0, tk.END)


def add_task():
    task_name = task_name_entry.get().strip()
    description = desc_entry.get().strip()
    important = important_var.get()
    due_date = due_entry.get().strip()

    if not task_name:
        messagebox.showerror("Error", "Task Name is required")
        return

    data = (task_name, description, important, due_date)

    tree.insert("", "end", values=data)

    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------
def delete_selected_task():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to delete")
        return

    for item in selected:
        tree.delete(item)


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------
window = tk.Tk()
window.title("Task Manager")
window.geometry("800x500")

# ---------------------------------------------------------
# FORM FRAME
# ---------------------------------------------------------
form_frame = tk.Frame(window, padx=10, pady=10)
form_frame.pack(fill="x")

tk.Label(form_frame, text="Task Name:").grid(row=0, column=0, sticky="w")
task_name_entry = tk.Entry(form_frame, width=25)
task_name_entry.grid(row=0, column=1, padx=5)

tk.Label(form_frame, text="Description:").grid(row=0, column=2, sticky="w")
desc_entry = tk.Entry(form_frame, width=25)
desc_entry.grid(row=0, column=3, padx=5)

tk.Label(form_frame, text="Important:").grid(row=1, column=0, sticky="w")
important_var = tk.StringVar(value="No")

important_box = ttk.Combobox(
    form_frame,
    textvariable=important_var,
    values=["Yes", "No"],
    state="readonly",
    width=22
)
important_box.grid(row=1, column=1, padx=5)

tk.Label(form_frame, text="Due Date (dd-mm-yyyy):").grid(row=1, column=2, sticky="w")
due_entry = tk.Entry(form_frame, width=25)
due_entry.grid(row=1, column=3, padx=5)

tk.Button(form_frame, text="Add", width=12, command=add_task)\
    .grid(row=2, column=1, pady=10)

tk.Button(form_frame, text="Reset", width=12, command=reset_form)\
    .grid(row=2, column=2, pady=10)

# ---------------------------------------------------------
# TABLE FRAME
# ---------------------------------------------------------
table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("Task Name", "Description", "Important", "Due Date")

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True)

# ---------------------------------------------------------
# BOTTOM CONTROLS
# ---------------------------------------------------------
bottom_frame = tk.Frame(window, pady=10)
bottom_frame.pack(fill="x")

tk.Button(
    bottom_frame,
    text="Delete Selected",
    width=15,
    command=delete_selected_task
).pack(side="left", padx=20)

# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------
window.mainloop()