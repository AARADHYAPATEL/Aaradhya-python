# List of tuples
students = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]

# Sort by age using a lambda function
sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted students by age: ", sorted_students)
