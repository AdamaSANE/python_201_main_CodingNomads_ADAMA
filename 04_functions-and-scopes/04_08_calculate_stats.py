# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(numbers):
    """Affiche le maximum, minimum, moyenne et somme d'une liste de nombres."""
    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    total_sum = sum(numbers)

    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Average: {average}")
    print(f"Sum: {total_sum}")



# Appel de la fonction avec example_list
stats(example_list)
stats()