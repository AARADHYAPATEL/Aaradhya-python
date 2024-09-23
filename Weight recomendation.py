# Python

def calculate_weight(age, height):
    weight_chart = {
        60: (78, 88),
        61: (79, 90),
        62: (80, 91),
        63: (80, 92),
        64: (81, 91),
        65: (85, 92),
        66: (87, 95),
        67: (89, 96),
        68: (90, 99),
        69: (90, 102),
        70: (90, 105),
        71: (90, 110),
        72: (90, 112)
    }

    if age in weight_chart and 4 <= height <= 5.3:
        min_weight, max_weight = weight_chart[age]
        print(f"Your weight is between {min_weight}-{max_weight}Kg")
    else:
        print("No data available for the given age and height")

def menu():
    import sys
    while True:
        print("1. Calculate weight")
        print("2. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                age = int(input("Enter your age: "))
                height = float(input("Enter your height: "))
                calculate_weight(age, height)
            elif choice == 2:
                sys.exit()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")

menu()