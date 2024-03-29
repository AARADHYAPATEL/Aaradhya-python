# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter even numbers using a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
