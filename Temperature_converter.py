def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")


def celsius_to_kelvin():
    celsius = float(input("Enter the temperature in Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}° in Celsius is equivalent to {kelvin}° Kelvin.")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}° in Fahrenheit is equivalent to {celsius}° Celsius.")


def fahrenheit_to_kelvin():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    print(f"{fahrenheit}° in Fahrenheit is equivalent to {kelvin}° Kelvin.")


def kelvin_to_celsius():
    kelvin = float(input("Enter the temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}° in Kelvin is equivalent to {celsius}° Celsius.")


def kelvin_to_fahrenheit():
    kelvin = float(input("Enter the temperature in Kelvin: "))
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    print(f"{kelvin}° in Kelvin is equivalent to {fahrenheit}° Fahrenheit.")

def menu():
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        celsius_to_fahrenheit()
    elif choice == 2:
        celsius_to_kelvin()
    elif choice == 3:
        fahrenheit_to_celsius()
    elif choice == 4:
        fahrenheit_to_kelvin()
    elif choice == 5:
        kelvin_to_celsius()
    elif choice == 6:
        kelvin_to_fahrenheit()
    elif choice == 0:
        print("Thank you for using the temperature converter.")
        exit()
    else:
        print("Invalid choice")

menu()
# Output:
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 1
# Enter the temperature in Celsius: 100
# 100.0° in Celsius is equivalent to 212.0° Fahrenheit.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 2
# Enter the temperature in Celsius: 100
# 100.0° in Celsius is equivalent to 373.15° Kelvin.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 3
# Enter the temperature in Fahrenheit: 212
# 212.0° in Fahrenheit is equivalent to 100.0° Celsius.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 4
# Enter the temperature in Fahrenheit: 212
# 212.0° in Fahrenheit is equivalent to 373.15° Kelvin.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 5
# Enter the temperature in Kelvin: 373.15
# 373.15° in Kelvin is equivalent to 100.0° Celsius.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 6
# Enter the temperature in Kelvin: 373.15
# 373.15° in Kelvin is equivalent to 212.0° Fahrenheit.
#
# 1. Celsius to Fahrenheit
# 2. Celsius to Kelvin
# 3. Fahrenheit to Celsius
# 4. Fahrenheit to Kelvin
# 5. Kelvin to Celsius
# 6. Kelvin to Fahrenheit
# 0. Exit
# Enter choice: 0
# Thank you for using the temperature converter.
#
# Process finished with exit code 0

