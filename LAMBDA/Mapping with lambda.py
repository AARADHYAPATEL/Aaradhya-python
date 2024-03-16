# List of numbers
numbers = [1, 2, 3, 4, 5]

# Square each number using a lambda function
squared_numbers = list(map(lambda x: x**2, numbers))
cubed_numbers = list(map(lambda x: x**3, numbers))

print("Squared numbers: ", squared_numbers)
print("Cubed numbers: ", cubed_numbers)
