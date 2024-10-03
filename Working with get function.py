planet = {
    'name': 'Earth',
    'moons': 1
}
print(planet.get('name'))
print(planet['name'])
planet.update({'name': 'makemake'})
planet['name'] = 'makemake'
print(planet)
planet.update({
    'name': 'jupiter',
    'moons': 79
})
print(planet)
planet['orbital period'] = 4333
print(planet)
planet.pop('orbital period')
print(planet)
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)
print(f"{planet["name"]} polar diameter: {planet['diameter (km)']['polar']}")
print(f"{planet['name']} equatorial diameter: {planet['diameter (km)']['equatorial']}")