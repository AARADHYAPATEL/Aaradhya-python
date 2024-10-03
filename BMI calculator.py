weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

# Calculate BMI using the correct formula
BMI = weight / (height * height)

# Check BMI category
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight")
elif 25 <= BMI <= 29.9:
    print("Overweight")
elif 30 <= BMI <= 34.9:
    print("Obesity class 1")
elif 35 <= BMI <= 39.9:
    print("Obesity class 2")
elif BMI >= 40:
    print("Extreme obesity")
else:
    print("Out of bounds")
