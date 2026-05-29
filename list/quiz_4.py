#convert list to list dictionaries
color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result = []

for name, code in zip(color_names, color_codes):
    result.append({
        "color_name": name,
        "color_code": code
    })

print(result)