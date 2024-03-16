# List of numbers
numbers = [10, 5, 8, 20, 30]

# Find the maximum and minimum using a lambda function
max_number = max(numbers, key=lambda x: x)
min_number = min(numbers, key=lambda x: x)

print("Maximum number: ", max_number)
print("Minimum number: ", min_number)
