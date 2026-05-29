#Remove empty tuples
sample_data = [(), (), ('',),
               ('a', 'b'),
               ('a', 'b', 'c'),
               ('d',)]

result = [x for x in sample_data if x]

print(result)