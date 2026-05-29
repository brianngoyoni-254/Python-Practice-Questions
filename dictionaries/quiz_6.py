#extract list
data = [
    {'Math': 90, 'Science': 92},
    {'Math': 89, 'Science': 94},
    {'Math': 92, 'Science': 88}
]

science_values = [item['Science'] for item in data]

print(science_values)