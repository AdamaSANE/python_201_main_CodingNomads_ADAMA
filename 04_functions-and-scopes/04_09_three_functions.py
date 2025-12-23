# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def get_user_number():
    """Demande à l'utilisateur de saisir un nombre et le retourne."""
    number = int(input("Veuillez entrer un nombre entier : "))
    return number

def square_number(number):
    """Retourne le carré du nombre donné."""
    return number ** 2
def display_result(result):
    """Affiche le résultat donné."""
    print(f"Le résultat est : {result}")



# Chaîne d'appels de fonctions
def main():
    nombre = get_user_number()
    carre = square_number(nombre)
    display_result(carre)

main()
user_number = get_user_number()
squared = square_number(user_number)
display_result(squared)