#concatenate
sample_list = ['p', 'q']
n = 5

result = [x + str(i) for i in range(1, n + 1) for x in sample_list]

print(result)