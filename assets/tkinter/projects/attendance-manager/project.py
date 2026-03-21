import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------

def reset_form():
    name_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    section_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    status_var.set("")


def add_record():
    name = name_entry.get().strip()
    student_class = class_entry.get().strip()
    section = section_entry.get().strip()
    date = date_entry.get().strip()
    status = status_var.get().strip()

    # Validation
    if not name or not student_class or not section or not date or not status:
        messagebox.showerror("Error", "All fields are required!")
        return

    data = (name, student_class, section, date, status)

    attendance_table.insert("", "end", values=data)

    update_summary()
    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------

def delete_selected():
    selected = attendance_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return

    for item in selected:
        attendance_table.delete(item)

    update_summary()


def update_summary():
    present = 0
    absent = 0

    for item in attendance_table.get_children():
        status = attendance_table.item(item)["values"][4]

        if status == "Present":
            present += 1
        else:
            absent += 1

    total = present + absent

    summary_label.config(
        text=f"Total: {total}   Present: {present}   Absent: {absent}"
    )


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------

window = tk.Tk()
window.title("Student Attendance Manager")
window.geometry("850x520")


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title_label = tk.Label(
    window,
    text="STUDENT ATTENDANCE MANAGER",
    font=("Arial", 18, "bold"),
    bg="#4169E1",
    fg="white",
    pady=10
)
title_label.pack(fill="x")


# ---------------------------------------------------------
# FORM FRAME
# ---------------------------------------------------------

form_frame = tk.Frame(window, padx=10, pady=10)
form_frame.pack(fill="x")

# Student Name
tk.Label(form_frame, text="Student Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, width=22)
name_entry.grid(row=0, column=1, padx=5)

# Class
tk.Label(form_frame, text="Class:").grid(row=0, column=2, sticky="w")
class_entry = tk.Entry(form_frame, width=12)
class_entry.grid(row=0, column=3, padx=5)

# Section
tk.Label(form_frame, text="Section:").grid(row=0, column=4, sticky="w")
section_entry = tk.Entry(form_frame, width=8)
section_entry.grid(row=0, column=5, padx=5)

# Date
tk.Label(form_frame, text="Date (dd-mm-yyyy):").grid(row=1, column=0, sticky="w")
date_entry = tk.Entry(form_frame, width=22)
date_entry.grid(row=1, column=1, padx=5)

# Status Dropdown
tk.Label(form_frame, text="Status:").grid(row=1, column=2, sticky="w")

status_var = tk.StringVar()

status_dropdown = ttk.Combobox(
    form_frame,
    textvariable=status_var,
    values=["Present", "Absent"],
    state="readonly",
    width=10
)
status_dropdown.grid(row=1, column=3, padx=5)

# Buttons
tk.Button(form_frame, text="Add Record", width=15, command=add_record)\
    .grid(row=2, column=1, pady=10)

tk.Button(form_frame, text="Reset", width=15, command=reset_form)\
    .grid(row=2, column=2, pady=10)


# ---------------------------------------------------------
# TABLE FRAME
# ---------------------------------------------------------

table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("Name", "Class", "Section", "Date", "Status")

attendance_table = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    attendance_table.heading(col, text=col)
    attendance_table.column(col, anchor="center")

attendance_table.pack(fill="both", expand=True)


# ---------------------------------------------------------
# BOTTOM CONTROLS
# ---------------------------------------------------------

bottom_frame = tk.Frame(window, pady=10)
bottom_frame.pack(fill="x")

tk.Button(
    bottom_frame,
    text="Delete Selected",
    width=18,
    command=delete_selected
).pack(side="left", padx=20)

summary_label = tk.Label(
    bottom_frame,
    text="Total: 0   Present: 0   Absent: 0",
    font=("Arial", 12, "bold")
)
summary_label.pack(side="right", padx=20)


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

window.mainloop()