#round numbers
numbers = [22.4, 4.0, 16.22, 9.1, 11.0,
           12.22, 14.2, 5.2, 17.5]

rounded = [round(x) for x in numbers]

print("Minimum value:", min(rounded))
print("Maximum value:", max(rounded))

multiplied = [x * 5 for x in rounded]

unique_sorted = sorted(set(multiplied))

print("Result:")
print(*unique_sorted)