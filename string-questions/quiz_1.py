def first_three(s):
    if len(s) < 3:
        return s
    return s[:3]

# Examples
print(first_three('ipy'))      # ipy
print(first_three('python'))   # pyt