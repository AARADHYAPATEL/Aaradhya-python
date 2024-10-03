mass_percentage = "1/6"
print("Your weight on the moon will be {} of your weight on Earth".format(mass_percentage))
print("Your weight on the moon will be %s of your weight on Earth" % mass_percentage)
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
print(round(100/6, 10))
print(f"One the moon, your weight would be {round(100/6, 2)}% of your weight on earth")
subject = "Interesting things on the moon"
heading = f"{subject.title()}"
print(heading)