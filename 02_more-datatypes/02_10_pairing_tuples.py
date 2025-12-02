# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

# Trier la liste
sorted_numbers = sorted(randlist) 
# Créer une nouvelle liste de tuples
paired_tuples = []
for i in range(0, len(sorted_numbers), 2):
    if i + 1 < len(sorted_numbers):
        paired_tuples.append((sorted_numbers[i], sorted_numbers[i + 1]))
    else:
        paired_tuples.append((sorted_numbers[i], 0))
for pair in paired_tuples:
    print(pair)

