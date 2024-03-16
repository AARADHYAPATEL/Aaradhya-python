import json

# JSON data to be decoded to Python
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Decode the JSON data to a python dictionary
data = json.loads(json_data)

print("Decoded python data:", data)
