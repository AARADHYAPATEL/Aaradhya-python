# Zip with different lengths in input iterables
names = ["Alice", "Bob", "Charlie"]
age = [25, 30]

# Using zip with different lengths will stop at the shortest iterable
combined_data = zip(names, age)

# Displaying the result
for name, age in combined_data:
    print(f"Name: {name}, Age: {age}")
