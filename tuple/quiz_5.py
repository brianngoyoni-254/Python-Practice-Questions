#compute the sum of all elements
list_of_tuples = [(1, 2, 6),
                  (2, 3, -6),
                  (3, 4),
                  (2, 2, 2, 2)]

result = [sum(x) for x in list_of_tuples]

print(result)