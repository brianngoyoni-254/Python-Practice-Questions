#concatenate dictionaries
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}

result = {}

result.update(d1)
result.update(d2)
result.update(d3)

print(result)