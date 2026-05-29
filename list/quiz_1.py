#print 1st and last 5square numbers

squares = [x**2 for x in range(1, 31) if x**2 <= 30]

print("Square numbers:", squares)
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])