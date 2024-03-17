# Using zip with enum
names = ["Alice", "Bob", "Charlie"]

# Combine with enum to get both index and value
indexed_names = list(zip(range(len(names)), names))

# Displaying the result
for index, name in indexed_names:
    print(f"Index: {index}, Name: {name}")
