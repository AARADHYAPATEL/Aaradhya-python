mars_temperature = "The temperature in mars is 30 C to 40 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)