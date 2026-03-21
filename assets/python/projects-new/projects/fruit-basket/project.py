# Fruit Basket Menu System

# Create an empty basket
fruit_basket = []

# Main program loop
while True:
    # Show the menu
    print("\n===== FRUIT BASKET MENU =====")
    print("1. Add a fruit")
    print("2. Remove a fruit")
    print("3. List all fruits")
    print("4. Exit")
    print("=============================")
    
    # Get user's choice
    choice = input("Enter your choice (1-4): ")
    
    # Add a fruit
    match choice:        
        case "1":
            print("\n You chose to add a fruit.")
            fruit = input("Enter fruit name to add: ")
            fruit_basket.append(fruit)
            print(f"{fruit} has been added to the basket!")
    
        # Remove a fruit
        case "2":
            print("\n You chose to remove a fruit.")
            fruit = input("Enter fruit name to remove: ")
            if fruit in fruit_basket:
                fruit_basket.remove(fruit)
                print(f"{fruit} has been removed from the basket!")
            else:
                print(f"{fruit} is not in the basket!")
    
        # List all fruits
        case "3":
            print("\n You chose to list all fruits.")
            print("\n Fruits in your basket:")
            if len(fruit_basket) == 0:
                print("  Your basket is empty!")
            else:
                for i in range(len(fruit_basket)):
                    print(f"  {i+1}. {fruit_basket[i]}")
    
        # Exit the program
        case "4":
            print("\n Thank you for using Fruit Basket! Goodbye!")
            break
        
        # Invalid choice
        case _:
            print("\n Invalid choice! Please enter 1, 2, 3, or 4.")
