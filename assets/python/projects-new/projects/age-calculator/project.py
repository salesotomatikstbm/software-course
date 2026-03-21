# Age Calculator

def calculate_age(birth_year):
    current_year = 2025
    age = current_year - birth_year
    return age

def print_results(name, birth_year):
    age = calculate_age(birth_year)
    print(f"\n--- Results for {name} ---")
    print(f"You are {age} years old")

# --- Main Program ---
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

print_results(name, birth_year)