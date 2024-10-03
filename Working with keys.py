rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
