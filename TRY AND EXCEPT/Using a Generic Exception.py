try:
    # Code that might use an exception
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result: ", y)

except Exception as e:
    # Catch any type of exception
    print(f"An error occured: {e}")