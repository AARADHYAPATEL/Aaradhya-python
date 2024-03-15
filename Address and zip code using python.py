from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="geoapiExercises")

# Get the city name from the user
place = input("Enter the city name: ")

# Geocode the location
location = geolocator.geocode(place)

# print the geolocation details
print(location)
