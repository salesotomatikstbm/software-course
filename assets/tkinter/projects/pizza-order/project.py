
import tkinter as tk
from tkinter import ttk as widgets
from tkinter import messagebox

# ========================================
# STEP 1: CREATE THE MAIN WINDOW
# ========================================
window = tk.Tk()
window.title("Pizza Ordering System")
window.geometry("800x650")


# ========================================
# CREATE THE INPUT FORM
# ========================================

# Create a frame to hold the form
form_frame = tk.Frame(window, pady=10)
form_frame.pack(fill="x", padx=20)

# Pizza Type field (Dropdown)
tk.Label(form_frame, text="Pizza Type:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
pizza_type_var = tk.StringVar()
pizza_type_dropdown = widgets.Combobox(
    form_frame,
    textvariable=pizza_type_var,
    width=20,
    font=("Arial", 10),
    state="readonly"  # Prevents typing, only selection
)
pizza_type_dropdown['values'] = ("Margherita", "Pepperoni", "Vegetarian", "BBQ Chicken", "Hawaiian", "Meat Lovers", "Four Cheese", "Mushroom")
pizza_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Pizza Size field (Dropdown)
tk.Label(form_frame, text="Pizza Size:", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
pizza_size_var = tk.StringVar()
pizza_size_dropdown = widgets.Combobox(
    form_frame,
    textvariable=pizza_size_var,
    width=15,
    font=("Arial", 10),
    state="readonly"  # Prevents typing, only selection
)
pizza_size_dropdown['values'] = ("Small", "Medium", "Large")
pizza_size_dropdown.grid(row=0, column=3, padx=5, pady=5)

# Quantity field
tk.Label(form_frame, text="Quantity:", font=("Arial", 10)).grid(row=0, column=4, padx=5, pady=5, sticky="e")
quantity_entry = tk.Entry(form_frame, width=10, font=("Arial", 10))
quantity_entry.grid(row=0, column=5, padx=5, pady=5)

# FUNCTION TO ADD PIZZA ORDER TO TABLE
def add_order():
    # Get values from the entry fields
    pizza_type = pizza_type_var.get().strip()
    pizza_size = pizza_size_var.get().strip()
    quantity = quantity_entry.get().strip()
    
    # Validate that all fields are filled
    if not pizza_type or not pizza_size or not quantity:
        messagebox.showerror("Error", "Please fill in all fields!")
        return
    
    # Validate that quantity is a number
    try:
        quantity_value = int(quantity)
        if quantity_value < 1:
            messagebox.showerror("Error", "Quantity must be at least 1!")
            return
        if quantity_value > 50:
            messagebox.showerror("Error", "Maximum quantity is 50 per order!")
            return
    except ValueError:
        messagebox.showerror("Error", "Quantity must be a number!")
        return
    
    # Calculate price based on size
    price_per_pizza = {
        "Small": 8.99,
        "Medium": 12.99,
        "Large": 16.99
    }
    
    unit_price = price_per_pizza[pizza_size]
    total_price = unit_price * quantity_value
    
    # Insert order into table
    order_table.insert("", "end", values=(pizza_type, pizza_size, quantity_value, f"${unit_price:.2f}", f"${total_price:.2f}"))
    
    # Clear the entry fields
    pizza_type_dropdown.set('')
    pizza_size_dropdown.set('')
    quantity_entry.delete(0, tk.END)
    
    # Update the footer count and total
    update_order_summary()
    
    pizza_type_dropdown.focus()

# Add Order Button
add_button = tk.Button(
    form_frame,
    text="Add to Order",
    font=("Arial", 11, "bold"),
    bg="#FF6347",
    fg="white",
    padx=30,
    pady=8,
    command=add_order,
    cursor="hand2"
)
add_button.grid(row=1, column=0, columnspan=6, pady=10)

# Function to update order summary
def update_order_summary():
    count = len(order_table.get_children())
    
    # Calculate total price
    total = 0.0
    for item in order_table.get_children():
        values = order_table.item(item)['values']
        total_price_str = values[4].replace('$', '')
        total += float(total_price_str)
    
    footer_label.config(text=f"Total Orders: {count}")
    total_amount_label.config(text=f"Grand Total: ${total:.2f}")

# Function to clear all orders
def clear_all_orders():
    if len(order_table.get_children()) == 0:
        messagebox.showinfo("Info", "No orders to clear!")
        return
    
    response = messagebox.askyesno("Confirm", "Are you sure you want to clear all orders?")
    if response:
        for item in order_table.get_children():
            order_table.delete(item)
        update_order_summary()
        messagebox.showinfo("Success", "All orders cleared!")

# Function to delete selected order
def delete_selected_order():
    selected_items = order_table.selection()
    if not selected_items:
        messagebox.showwarning("Warning", "Please select an order to delete!")
        return
    
    for item in selected_items:
        order_table.delete(item)
    
    update_order_summary()

# ========================================
# STEP 2: ADD A TITLE
# ========================================
title_label = tk.Label(
    window,
    text="🍕 Pizza Ordering System 🍕",
    font=("Arial", 18, "bold"),
    bg="#FF6347",
    fg="white",
    pady=15
)
title_label.pack(fill="x")  # Stretch across the window

# ========================================
# STEP 3: ADD AN INSTRUCTION LABEL
# ========================================
instruction_label = tk.Label(
    window,
    text="Select your pizza type, size, and quantity to place an order",
    font=("Arial", 10),
    pady=10
)
instruction_label.pack()

# ========================================
# STEP 4: CREATE THE TABLE (TREEVIEW)
# ========================================

order_table = widgets.Treeview(
    window,
    columns=("column1", "column2", "column3", "column4", "column5"),  # Define 5 columns
    show="headings",  # Show only column headers (not tree structure)
    height=12  # Show 12 rows at a time
)

# ========================================
# STEP 5: DEFINE COLUMN HEADINGS
# ========================================

order_table.heading("column1", text="Pizza Type")
order_table.heading("column2", text="Size")
order_table.heading("column3", text="Quantity")
order_table.heading("column4", text="Unit Price")
order_table.heading("column5", text="Total Price")

# ========================================
# STEP 6: SET COLUMN WIDTHS
# ========================================

order_table.column("column1", width=180, anchor="w")  # w = west (left align)
order_table.column("column2", width=100, anchor="center")  # center align
order_table.column("column3", width=100, anchor="center")  # center align
order_table.column("column4", width=100, anchor="e")  # e = east (right align)
order_table.column("column5", width=100, anchor="e")  # e = east (right align)

# ========================================
# STEP 7: ADD SAMPLE DATA TO THE TABLE
# ========================================

# Sample Order 1
order_table.insert(
    "",
    "end",
    values=("Margherita", "Medium", 2, "$12.99", "$25.98")
)

# Sample Order 2
order_table.insert(
    "",
    "end",
    values=("Pepperoni", "Large", 1, "$16.99", "$16.99")
)

# Sample Order 3
order_table.insert(
    "",
    "end",
    values=("Vegetarian", "Small", 3, "$8.99", "$26.97")
)

# ========================================
# STEP 8: DISPLAY THE TABLE
# ========================================

# Pack the table to make it visible on the window
order_table.pack(padx=20, pady=10)

# ========================================
# STEP 9: ADD ACTION BUTTONS
# ========================================

button_frame = tk.Frame(window, pady=5)
button_frame.pack()

delete_button = tk.Button(
    button_frame,
    text="Delete Selected",
    font=("Arial", 10, "bold"),
    bg="#FF4444",
    fg="white",
    padx=20,
    pady=5,
    command=delete_selected_order,
    cursor="hand2"
)
# delete_button.pack(side="left", padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All Orders",
    font=("Arial", 10, "bold"),
    bg="#FFA500",
    fg="white",
    padx=20,
    pady=5,
    command=clear_all_orders,
    cursor="hand2"
)
# clear_button.pack(side="left", padx=5)

# ========================================
# STEP 10: ADD A FOOTER LABEL
# ========================================

footer_label = tk.Label(
    window,
    text="Total Orders: 3",
    font=("Arial", 10),
    fg="gray",
    pady=5
)
footer_label.pack()

# ========================================
# STEP 11: ADD TOTAL AMOUNT LABEL
# ========================================

total_amount_label = tk.Label(
    window,
    text="Grand Total: $69.94",
    font=("Arial", 14, "bold"),
    fg="#FF6347",
    bg="#FFF3E0",
    pady=10,
    padx=20
)
# total_amount_label.pack(fill="x", padx=20)

# ========================================
# START THE APPLICATION
# ========================================
window.mainloop()