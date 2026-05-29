#filter dictionary based on values
students = {
    'Cierra Vega': 175,
    'Alden Cantrell': 180,
    'Kierra Gentry': 165,
    'Pierre Cox': 190
}

result = {key: value for key, value in students.items() if value > 170}

print("Marks greater than 170:")
print(result)