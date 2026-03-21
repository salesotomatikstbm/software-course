import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# GLOBAL TOTAL
# ---------------------------------------------------------

grand_total = 0
ticket_price = 150  # price per ticket


# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------

def reset_form():
    name_entry.delete(0, tk.END)
    movie_var.set("")
    ticket_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_var.set("")


def add_booking():
    global grand_total

    name = name_entry.get().strip()
    movie = movie_var.get().strip()
    tickets = ticket_entry.get().strip()
    date = date_entry.get().strip()
    time_slot = time_var.get().strip()

    # Validation
    if not name or not movie or not tickets or not date or not time_slot:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        tickets = int(tickets)
        if tickets <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Number of tickets must be a valid number!")
        return

    total = tickets * ticket_price
    grand_total += total

    data = (name, movie, date, time_slot, tickets, total)

    booking_table.insert("", "end", values=data)

    update_total()
    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------

def delete_selected():
    global grand_total

    selected = booking_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a booking to delete")
        return

    for item in selected:
        values = booking_table.item(item)["values"]
        total = values[5]
        grand_total -= total
        booking_table.delete(item)

    update_total()


def update_total():
    total_label.config(text=f"Grand Total: ₹ {grand_total}")


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------

window = tk.Tk()
window.title("Movie Ticket Booking System")
window.geometry("950x550")


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title_label = tk.Label(
    window,
    text="MOVIE TICKET BOOKING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#8A2BE2",
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

tk.Label(form_frame, text="Customer Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(form_frame, text="Movie:").grid(row=0, column=2, sticky="w")

movie_var = tk.StringVar()

movie_dropdown = ttk.Combobox(
    form_frame,
    textvariable=movie_var,
    values=[
        "Action Movie",
        "Comedy Movie",
        "Drama Movie",
        "Sci-Fi Movie",
        "Animation Movie"
    ],
    state="readonly",
    width=20
)
movie_dropdown.grid(row=0, column=3, padx=10)

tk.Label(form_frame, text="Tickets:").grid(row=0, column=4, sticky="w")
ticket_entry = tk.Entry(form_frame, width=10)
ticket_entry.grid(row=0, column=5, padx=10)


# -------- ROW 2 --------

tk.Label(form_frame, text="Show Date (dd-mm-yyyy):").grid(row=1, column=0, sticky="w")
date_entry = tk.Entry(form_frame, width=25)
date_entry.grid(row=1, column=1, padx=10)

tk.Label(form_frame, text="Show Time:").grid(row=1, column=2, sticky="w")

time_var = tk.StringVar()

time_dropdown = ttk.Combobox(
    form_frame,
    textvariable=time_var,
    values=[
        "10:00 AM",
        "01:00 PM",
        "04:00 PM",
        "07:00 PM",
        "10:00 PM"
    ],
    state="readonly",
    width=15
)
time_dropdown.grid(row=1, column=3, padx=10)


# -------- ROW 3 (BUTTONS) --------

tk.Button(form_frame, text="Add Booking",
          width=18, command=add_booking)\
    .grid(row=2, column=1, pady=15)

tk.Button(form_frame, text="Reset",
          width=15, command=reset_form)\
    .grid(row=2, column=2, pady=15)


# ---------------------------------------------------------
# TABLE FRAME
# ---------------------------------------------------------

table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("Customer Name", "Movie", "Date", "Time", "Tickets", "Total")

booking_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for col in columns:
    booking_table.heading(col, text=col)
    booking_table.column(col, anchor="center")

booking_table.pack(fill="both", expand=True)


# ---------------------------------------------------------
# BOTTOM CONTROLS
# ---------------------------------------------------------

bottom_frame = tk.Frame(window, pady=10)
bottom_frame.pack(fill="x")

tk.Button(
    bottom_frame,
    text="Delete Selected Booking",
    width=22,
    command=delete_selected
).pack(side="left", padx=20)

total_label = tk.Label(
    bottom_frame,
    text="Grand Total: ₹ 0",
    font=("Arial", 12, "bold")
)
total_label.pack(side="right", padx=20)


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

window.mainloop()