#moving zero digits to the end of list
numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0,
           9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

non_zero = [x for x in numbers if x != 0]
zeros = [x for x in numbers if x == 0]

result = non_zero + zeros

print("Original list:")
print(numbers)

print("Move all zero digits to end:")
print(result)