# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)
user_numbers = randlist  # Replace this with user input if desired
# Trouver le plus grand nombre
largest_number = max(user_numbers)
print(f"The largest number is: {largest_number}")
# Calculer le produit de tous les nombres
product = 1
for number in user_numbers:
    product *= number
print(f"The product of all numbers is: {product}")