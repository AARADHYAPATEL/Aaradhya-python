a = int(input("Enter a temperature value: "))
scale = input("Enter the scale: ")


def convert_temperature(a, scale):
    if scale == "F":
        return (a - 32) * 5 / 9
    elif scale == "C":
        return (a * 9 / 5) + 32
    else:
        return "Invalid scale"


print(convert_temperature(a, scale))
