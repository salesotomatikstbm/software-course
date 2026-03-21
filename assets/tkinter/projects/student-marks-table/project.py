import tkinter as tk
from tkinter import ttk as widgets
from tkinter import messagebox

# ========================================
# STEP 1: CREATE THE MAIN WINDOW
# ========================================
window = tk.Tk()
window.title("Table Basics - Student Marks Display")
window.geometry("700x500")

# ========================================
# STEP 2: ADD A TITLE
# ========================================
title_label = tk.Label(
    window,
    text="Student Marks Table",
    font=("Arial", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    pady=15
)
title_label.pack(fill="x")  # Stretch across the window

# ========================================
# CREATE THE INPUT FORM
# ========================================

# Create a frame to hold the form
form_frame = tk.Frame(window, pady=10)
form_frame.pack(fill="x", padx=20)

# Student Name field
tk.Label(form_frame, text="Student Name:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(form_frame, width=20, font=("Arial", 10))
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Subject field (Dropdown)
tk.Label(form_frame, text="Subject:", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
subject_var = tk.StringVar()
subject_dropdown = widgets.Combobox(
    form_frame,
    textvariable=subject_var,
    width=17,
    font=("Arial", 10),
    state="readonly"  # Prevents typing, only selection
)
subject_dropdown['values'] = ("Mathematics", "Science", "English", "History", "Geography", "Physics", "Chemistry", "Biology")
subject_dropdown.grid(row=0, column=3, padx=5, pady=5)

# Marks field
tk.Label(form_frame, text="Marks:", font=("Arial", 10)).grid(row=0, column=4, padx=5, pady=5, sticky="e")
marks_entry = tk.Entry(form_frame, width=10, font=("Arial", 10))
marks_entry.grid(row=0, column=5, padx=5, pady=5)

# ========================================
# FUNCTION TO ADD STUDENT TO TABLE
# ========================================
def add_student():
    # Get values from the entry fields
    name = name_entry.get().strip()
    subject = subject_var.get().strip()
    marks = marks_entry.get().strip()
    
    # Validate that all fields are filled
    if not name or not subject or not marks:
        messagebox.showerror("Error", "Please fill in all fields!")
        return
    
    # Validate that marks is a number
    try:
        marks_value = int(marks)
        if marks_value < 0 or marks_value > 100:
            messagebox.showerror("Error", "Marks should be between 0 and 100!")
            return
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number!")
        return
    
    # Add the student to the table
    student_table.insert("", "end", values=(name, subject, marks_value))
    
    # Clear the entry fields
    name_entry.delete(0, tk.END)
    subject_dropdown.set('')
    marks_entry.delete(0, tk.END)
    
    # Update the footer count
    update_student_count()
    
    # Focus back on name entry
    name_entry.focus()

# Add Button (below the fields, centered)
add_button = tk.Button(
    form_frame,
    text="Add Student",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=30,
    pady=8,
    command=add_student,
    cursor="hand2"
)
add_button.grid(row=1, column=0, columnspan=6, pady=10)

# ========================================
# STEP 4: ADD AN INSTRUCTION LABEL
# ========================================
instruction_label = tk.Label(
    window,
    text="Fill in the form above to add students, or view existing records below",
    font=("Arial", 10),
    pady=10
)
instruction_label.pack()

# ========================================
# STEP 5: CREATE THE TABLE (TREEVIEW)
# ========================================

student_table = widgets.Treeview(
    window,
    columns=("column1", "column2", "column3"),
    show="headings",
    height=10
)

# ========================================
# STEP 6: DEFINE COLUMN HEADINGS
# ========================================

student_table.heading("column1", text="Student Name")
student_table.heading("column2", text="Subject")
student_table.heading("column3", text="Marks")

# ========================================
# STEP 7: SET COLUMN WIDTHS
# ========================================

student_table.column("column1", width=200, anchor="w")
student_table.column("column2", width=180, anchor="center")
student_table.column("column3", width=100, anchor="e")

# ========================================
# STEP 8: ADD INITIAL DATA TO THE TABLE
# ========================================

student_table.insert("", "end", values=("Rahul Kumar", "Mathematics", 85))
student_table.insert("", "end", values=("Priya Sharma", "Science", 92))
student_table.insert("", "end", values=("Amit Patel", "English", 78))
student_table.insert("", "end", values=("Sneha Reddy", "Mathematics", 88))
student_table.insert("", "end", values=("Arjun Singh", "Science", 95))
student_table.insert("", "end", values=("Kavya Nair", "English", 82))

# ========================================
# STEP 9: DISPLAY THE TABLE
# ========================================

student_table.pack(padx=20, pady=10)

# ========================================
# STEP 10: ADD A FOOTER LABEL
# ========================================

footer_label = tk.Label(
    window,
    text="",
    font=("Arial", 9),
    fg="gray",
    pady=10
)
footer_label.pack()

# Function to update student count
def update_student_count():
    count = len(student_table.get_children())
    footer_label.config(text=f"Total Students: {count}")

# Initialize the count
update_student_count()

# ========================================
# START THE APPLICATION
# ========================================
window.mainloop()