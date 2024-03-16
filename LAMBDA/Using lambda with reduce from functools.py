from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the product and addition of all numbers using a lambda function and reduce
product = reduce(lambda x, y: x * y, numbers)
addition = reduce(lambda x, y: x + y, numbers)

print("Product of Numbers:", product)
print("Sum of Numbers:", addition)
