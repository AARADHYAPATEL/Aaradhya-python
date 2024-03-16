try:
    # Code that might raise exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    # Handle the specific exception (division by zero)
    print("Error: Cannot divide by zero")

except ValueError:
    # Handle the specific exception (invalid input for conversion to int)
    print("Error: Please enter a valid number.")
