#Replace the last value
sample_list = [(10, 20, 40),
               (40, 50, 60),
               (70, 80, 90)]

result = [x[:-1] + (100,) for x in sample_list]

print(result)