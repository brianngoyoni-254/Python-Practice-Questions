#convert tuple into a positive integer
tup = (10, 20, 40, 5, 70)

result = int(''.join(map(str, tup)))

print(result)