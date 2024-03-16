# List of dictionaries representing people with names and ages
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 40},
    {"name": "Charlie", "age": 22}]

# Sort by age and then name using a lambda function
sorted_people = sorted(people, key=lambda person: (person["age"], person["name"]))

print("Sorted people:", sorted_people)
