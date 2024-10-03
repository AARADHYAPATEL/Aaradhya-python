planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
number_of_planets = len(planets)
print(f"There are {number_of_planets} planets in the solar system")
planets.append("Pluto")
number_of_planets = len(planets)
print(f"There are actually {number_of_planets} planets in the solar system")
planets.pop()
number_of_planets = len(planets)
print(f"No, there are definitely {number_of_planets} planets in the solar system")