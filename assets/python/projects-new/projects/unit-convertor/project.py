# Unit Converter App

# Function: Meter to Centimeter
def meter_to_cm():
    meter = float(input("Enter length in meters: "))
    cm = meter * 100
    print("Centimeters:", cm)


# Function: Centimeter to Meter
def cm_to_meter():
    cm = float(input("Enter length in centimeters: "))
    meter = cm / 100
    print("Meters:", meter)


while True:
    print("\nUnit Converter")
    print("1. Meter to Centimeter")
    print("2. Centimeter to Meter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        meter_to_cm()

    elif choice == "2":
        cm_to_meter()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")