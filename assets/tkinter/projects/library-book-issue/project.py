import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------

def reset_form():
    name_entry.delete(0, tk.END)
    book_var.set("")
    issue_entry.delete(0, tk.END)
    return_entry.delete(0, tk.END)


def add_record():
    student_name = name_entry.get().strip()
    book_name = book_var.get().strip()
    issue_date = issue_entry.get().strip()
    return_date = return_entry.get().strip()

    # Validation
    if not student_name or not book_name or not issue_date or not return_date:
        messagebox.showerror("Error", "All fields are required!")
        return

    data = (student_name, book_name, issue_date, return_date)

    library_table.insert("", "end", values=data)

    update_count()
    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------

def delete_selected():
    selected = library_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return

    for item in selected:
        library_table.delete(item)

    update_count()


def update_count():
    count = len(library_table.get_children())
    count_label.config(text=f"Total Issued Books: {count}")


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------

window = tk.Tk()
window.title("Library Book Issue System")
window.geometry("800x500")


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title_label = tk.Label(
    window,
    text="LIBRARY BOOK ISSUE SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#2E8B57",
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
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=5)

# Book Title Dropdown
tk.Label(form_frame, text="Book Title:").grid(row=0, column=2, sticky="w")

book_var = tk.StringVar()

book_dropdown = ttk.Combobox(
    form_frame,
    textvariable=book_var,
    values=[
        "Python Basics",
        "Science Encyclopedia",
        "Mathematics Guide",
        "English Grammar",
        "World History",
        "Computer Fundamentals",
        "AI for Beginners"
    ],
    state="readonly",
    width=22
)
book_dropdown.grid(row=0, column=3, padx=5)

# Issue Date
tk.Label(form_frame, text="Issue Date (dd-mm-yyyy):").grid(row=1, column=0, sticky="w")
issue_entry = tk.Entry(form_frame, width=25)
issue_entry.grid(row=1, column=1, padx=5)

# Return Date
tk.Label(form_frame, text="Return Date (dd-mm-yyyy):").grid(row=1, column=2, sticky="w")
return_entry = tk.Entry(form_frame, width=25)
return_entry.grid(row=1, column=3, padx=5)

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

columns = ("Student Name", "Book Title", "Issue Date", "Return Date")

library_table = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    library_table.heading(col, text=col)
    library_table.column(col, anchor="center")

library_table.pack(fill="both", expand=True)


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

count_label = tk.Label(
    bottom_frame,
    text="Total Issued Books: 0",
    font=("Arial", 12, "bold")
)
count_label.pack(side="right", padx=20)


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

window.mainloop()