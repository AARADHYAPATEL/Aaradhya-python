import json

# Python dictionary to be encoded to JSON
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Encode the Python Dictionary to JSON
json_data = json.dumps(data)

print("Encoded JSON", json_data)
