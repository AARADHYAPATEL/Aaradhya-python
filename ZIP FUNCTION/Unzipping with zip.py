# Unzipping with zip
names = ["Alice", "Bob", "Charlie"]
age = [25, 30, 35]

# Combining lists using zip
combined_data = zip(names, age)


# Unzipping the result
unzipped_names, unzipped_ages = zip(*combined_data)

# Displaying the result
print("Unzipped Names:", unzipped_names)
print("Unzipped Ages:", unzipped_ages)
