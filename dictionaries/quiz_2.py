#print all distinct values
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": "S005"},
        {"V": "S009"}, {"VIII": "S007"}]

unique_values = set()

for item in data:
    for value in item.values():
        unique_values.add(value)

print("Unique Values:", unique_values)