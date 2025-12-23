# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def is_divisible_by_4_or_7(number):
    """Détermine si un nombre est divisible par 4 ou 7.

    Args:
        number (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est divisible par 4 ou 7, sinon False.
    """
    return number % 4 == 0 or number % 7 == 0


def is_divisible_by_4_and_7(number):
    """Détermine si un nombre est divisible par 4 ET 7.

    Args:
        number (int): Le nombre à vérifier.

    Returns:
        bool: True si le nombre est divisible par 4 et 7, sinon False.
    """
    return number % 4 == 0 and number % 7 == 0

# Saisie utilisateur
number = int(input("Entrez un nombre entre 1 et 1 000 000 000 : "))

# Appels des fonctions
result_or = is_divisible_by_4_or_7(number)
result_and = is_divisible_by_4_and_7(number)

# Affichage des résultats
print(f"Le nombre {number} est divisible par 4 ou 7 : {result_or}")
print(f"Le nombre {number} est divisible par 4 et 7 : {result_and}")

