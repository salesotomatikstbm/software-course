import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------

def reset_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    doctor_var.set("")
    date_entry.delete(0, tk.END)
    time_var.set("")
    reason_entry.delete(0, tk.END)


def add_appointment():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    doctor = doctor_var.get().strip()
    date = date_entry.get().strip()
    time_slot = time_var.get().strip()
    reason = reason_entry.get().strip()

    if not name or not age or not doctor or not date or not time_slot:
        messagebox.showerror("Error", "Please fill all required fields!")
        return

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Age must be a valid number!")
        return

    data = (name, age, doctor, date, time_slot, reason)

    appointment_table.insert("", "end", values=data)

    update_count()
    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------

def delete_selected():
    selected = appointment_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select an appointment to delete")
        return

    for item in selected:
        appointment_table.delete(item)

    update_count()


def update_count():
    count = len(appointment_table.get_children())
    count_label.config(text=f"Total Appointments: {count}")


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------

window = tk.Tk()
window.title("Clinic Appointment System")
window.geometry("950x550")


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title_label = tk.Label(
    window,
    text="CLINIC APPOINTMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#20B2AA",
    fg="white",
    pady=10
)
title_label.pack(fill="x")


# ---------------------------------------------------------
# FORM FRAME
# ---------------------------------------------------------

form_frame = tk.Frame(window, padx=15, pady=15)
form_frame.pack(fill="x")

# -------- ROW 1 --------

tk.Label(form_frame, text="Patient Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(form_frame, text="Age:").grid(row=0, column=2, sticky="w")
age_entry = tk.Entry(form_frame, width=8)
age_entry.grid(row=0, column=3, padx=10)

tk.Label(form_frame, text="Doctor:").grid(row=0, column=4, sticky="w")

doctor_var = tk.StringVar()
doctor_dropdown = ttk.Combobox(
    form_frame,
    textvariable=doctor_var,
    values=[
        "Dr. Sharma (General)",
        "Dr. Rao (Cardiologist)",
        "Dr. Khan (Dermatologist)",
        "Dr. Patel (Orthopedic)",
        "Dr. Mehta (Pediatrician)"
    ],
    state="readonly",
    width=25
)
doctor_dropdown.grid(row=0, column=5, padx=10)


# -------- ROW 2 --------

tk.Label(form_frame, text="Date (dd-mm-yyyy):").grid(row=1, column=0, sticky="w")
date_entry = tk.Entry(form_frame, width=25)
date_entry.grid(row=1, column=1, padx=10)

tk.Label(form_frame, text="Time Slot:").grid(row=1, column=2, sticky="w")

time_var = tk.StringVar()
time_dropdown = ttk.Combobox(
    form_frame,
    textvariable=time_var,
    values=[
        "09:00 AM", "10:00 AM", "11:00 AM",
        "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"
    ],
    state="readonly",
    width=15
)
time_dropdown.grid(row=1, column=3, padx=10)

tk.Label(form_frame, text="Reason (optional):").grid(row=1, column=4, sticky="w")
reason_entry = tk.Entry(form_frame, width=25)
reason_entry.grid(row=1, column=5, padx=10)


# -------- ROW 3 (BUTTONS) --------

tk.Button(form_frame, text="Add Appointment",
          width=18, command=add_appointment)\
    .grid(row=2, column=1, pady=15)

tk.Button(form_frame, text="Reset",
          width=15, command=reset_form)\
    .grid(row=2, column=2, pady=15)


# ---------------------------------------------------------
# TABLE FRAME
# ---------------------------------------------------------

table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("Patient Name", "Age", "Doctor", "Date", "Time", "Reason")

appointment_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for col in columns:
    appointment_table.heading(col, text=col)
    appointment_table.column(col, anchor="center")

appointment_table.pack(fill="both", expand=True)


# ---------------------------------------------------------
# BOTTOM CONTROLS
# ---------------------------------------------------------

bottom_frame = tk.Frame(window, pady=10)
bottom_frame.pack(fill="x")

tk.Button(
    bottom_frame,
    text="Delete Selected Appointment",
    width=25,
    command=delete_selected
).pack(side="left", padx=20)

count_label = tk.Label(
    bottom_frame,
    text="Total Appointments: 0",
    font=("Arial", 12, "bold")
)
count_label.pack(side="right", padx=20)


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

window.mainloop()