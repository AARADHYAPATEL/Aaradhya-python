# List of numbers
numbers = [10, 5, 8, 20, 15]

# Use a lambda function with a conditional expression to filter and square even numbers.
filtered_and_squared = list(map(lambda x: x**2 if x % 2 == 0 else x, numbers))
filtered_and_cubed = list(map(lambda x: x**3 if x % 2 == 0 else x, numbers))
filtered_and_squared_odd = list(map(lambda x: x**2 if x % 2 != 0 else x, numbers))
filtered_and_cubed_odd = list(map(lambda x: x**3 if x % 2 != 0 else x, numbers))

print("Filtered and Squared Numbers:", filtered_and_squared)
print("Filtered and Cubed numbers:", filtered_and_cubed)
print("Filtered and Squared Odd Numbers:", filtered_and_squared_odd)
print("Filtered and Cubed Odd Numbers:", filtered_and_cubed_odd)
