import tkinter as tk
from tkinter import ttk, messagebox

# ---------------------------------------------------------
# GLOBAL TOTAL
# ---------------------------------------------------------

grand_total = 0


# ---------------------------------------------------------
# FORM FUNCTIONS
# ---------------------------------------------------------

def reset_form():
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)


def add_item():
    global grand_total

    item = item_entry.get().strip()
    qty = qty_entry.get().strip()
    price = price_entry.get().strip()

    # Validation
    if not item or not qty or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        qty = int(qty)
        price = float(price)
    except:
        messagebox.showerror("Error", "Quantity must be integer and price must be number!")
        return

    subtotal = qty * price
    grand_total += subtotal

    data = (item, qty, f"{price:.2f}", f"{subtotal:.2f}")

    bill_table.insert("", "end", values=data)

    update_total()
    reset_form()


# ---------------------------------------------------------
# TABLE FUNCTIONS
# ---------------------------------------------------------

def delete_selected():
    global grand_total

    selected = bill_table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select an item to delete")
        return

    for item_id in selected:
        values = bill_table.item(item_id)["values"]
        subtotal = float(values[3])
        grand_total -= subtotal
        bill_table.delete(item_id)

    update_total()


def update_total():
    total_label.config(text=f"Grand Total: ₹ {grand_total:.2f}")


# ---------------------------------------------------------
# MAIN WINDOW
# ---------------------------------------------------------

window = tk.Tk()
window.title("Simple Billing System")
window.geometry("850x520")


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title_label = tk.Label(
    window,
    text="SIMPLE BILLING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#FF8C00",
    fg="white",
    pady=10
)
title_label.pack(fill="x")


# ---------------------------------------------------------
# FORM FRAME
# ---------------------------------------------------------

form_frame = tk.Frame(window, padx=10, pady=10)
form_frame.pack(fill="x")

# Item Name
tk.Label(form_frame, text="Item Name:").grid(row=0, column=0, sticky="w")
item_entry = tk.Entry(form_frame, width=25)
item_entry.grid(row=0, column=1, padx=5)

# Quantity
tk.Label(form_frame, text="Quantity:").grid(row=0, column=2, sticky="w")
qty_entry = tk.Entry(form_frame, width=12)
qty_entry.grid(row=0, column=3, padx=5)

# Unit Price
tk.Label(form_frame, text="Unit Price (₹):").grid(row=0, column=4, sticky="w")
price_entry = tk.Entry(form_frame, width=12)
price_entry.grid(row=0, column=5, padx=5)

# Buttons
tk.Button(form_frame, text="Add Item", width=15, command=add_item)\
    .grid(row=1, column=1, pady=10)

tk.Button(form_frame, text="Reset", width=15, command=reset_form)\
    .grid(row=1, column=2, pady=10)


# ---------------------------------------------------------
# TABLE FRAME
# ---------------------------------------------------------

table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=10, pady=5)

columns = ("Item Name", "Quantity", "Unit Price", "Subtotal")

bill_table = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    bill_table.heading(col, text=col)
    bill_table.column(col, anchor="center")

bill_table.pack(fill="both", expand=True)


# ---------------------------------------------------------
# BOTTOM CONTROLS
# ---------------------------------------------------------

bottom_frame = tk.Frame(window, pady=10)
bottom_frame.pack(fill="x")

tk.Button(
    bottom_frame,
    text="Delete Selected Item",
    width=20,
    command=delete_selected
).pack(side="left", padx=20)

total_label = tk.Label(
    bottom_frame,
    text="Grand Total: ₹ 0.00",
    font=("Arial", 14, "bold")
)
total_label.pack(side="right", padx=20)


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

window.mainloop()