# =========================================
# SHOPPING BILL CALCULATOR (EASY)
# Using separate lists (no nested lists)
# =========================================

# Lists to store bill data
item_names = []
item_prices = []
item_quantities = []
item_totals = []


# -----------------------------------------
# Function: Add a new item
# -----------------------------------------
def add_item():
    print("\nAdd New Item")

    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    # Add data to respective lists
    item_names.append(name)
    item_prices.append(price)
    item_quantities.append(quantity)
    item_totals.append(total)

    print(f"{name} added to bill.")


# -----------------------------------------
# Function: View bill
# -----------------------------------------
def view_bill():
    print("\nCurrent Bill")

    if len(item_names) == 0:
        print("No items in bill.")
        return

    grand_total = 0

    for i in range(len(item_names)):
        print(
            f"{i+1}. {item_names[i]} - "
            f"Price: {item_prices[i]}, "
            f"Qty: {item_quantities[i]}, "
            f"Total: {item_totals[i]}"
        )

        grand_total = grand_total + item_totals[i]

    print("--------------------------")
    print("Grand Total:", grand_total)


# -----------------------------------------
# Function: Remove an item
# -----------------------------------------
def remove_item():
    print("\nRemove Item")

    if len(item_names) == 0:
        print("Bill is empty.")
        return

    view_bill()

    index = int(input("Enter item number to remove: ")) - 1

    if 0 <= index < len(item_names):
        removed_name = item_names.pop(index)
        item_prices.pop(index)
        item_quantities.pop(index)
        item_totals.pop(index)

        print(removed_name, "removed from bill.")
    else:
        print("Invalid item number.")


# =========================================
# MAIN PROGRAM LOOP
# =========================================
while True:

    print("\n===== SHOPPING BILL CALCULATOR =====")
    print("1. Add Item")
    print("2. View Bill")
    print("3. Remove Item")
    print("4. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_bill()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        print("Thank you for using the Billing System!")
        break

    else:
        print("Invalid choice. Please try again.")