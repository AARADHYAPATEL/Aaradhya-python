# Basic usage of zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 75]

# Combining lists using zip
combined_data = zip(names, ages)

# Displaying the result
for name, age in combined_data:
    print(f"Name: {name}, Age: {age}")
