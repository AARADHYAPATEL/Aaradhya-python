amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_group = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_group
regular_satellite_moons.sort()
print("The regular satellite moons of jupiter are", regular_satellite_moons)
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of jupiter are", regular_satellite_moons)