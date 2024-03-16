import json

# JSON data with a syntax error
json_data = '{"name": "John", "age": 30, "city": "New York"'

try:
    # Attempt to decode JSON data
    data = json.loads(json_data)
except json.JSONDecodeError as e:
    # Handle JSON decoding error
    print("Error decoding JSON:", e)
