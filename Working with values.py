rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f"There was {total_rainfall}cm in the last quarter")