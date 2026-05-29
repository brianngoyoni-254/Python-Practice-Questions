#sort a tuple
sample_data = [('item1', '12.20'),
               ('item2', '15.10'),
               ('item3', '24.5')]

result = sorted(sample_data,
                key=lambda x: float(x[1]),
                reverse=True)

print(result)