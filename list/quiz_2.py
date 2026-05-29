#difference btn two lists
li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 6, 7]

difference = list(set(li1) - set(li2))

print("Difference between lists:", difference)