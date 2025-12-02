# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

power_dict = {}
for n in range(1, 11):
    power_dict[n] = n * n
print(power_dict) 

