moon_temperature = "The temperature on moon is 26.78 C and 87.39832 C"
for item in moon_temperature.split():
    try:
        float(item)
        print(item)
    except ValueError:
        continue