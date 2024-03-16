# List of tuples representing products with names and prices
products = [("Laptop", 120000), ("Phone", 80000), ("Tablet", 50000), ("Smartwatch", 20000)]

# Find the most and least expensive products using lambda function
most_expensive = max(products, key=lambda item: item[1])
least_expensive = min(products, key=lambda item: item[1])

print("Most expensive Item:", most_expensive)
print("Least expensive product:", least_expensive)
