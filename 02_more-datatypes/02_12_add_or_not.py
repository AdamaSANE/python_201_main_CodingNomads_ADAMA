# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.


user_numbers = set()
points = 0
while points > -5 and len(user_numbers) <= 10:
    user_input = input("Entrez un nombre entier : ")
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        if number in user_numbers:
            points -= 1
            print(f"Nombre en double ! Points restants : {points}")
        else:
            user_numbers.add(number)
            print(f"Nombre ajouté ! Ensemble actuel : {user_numbers}")
    else:
        print("Veuillez entrer un nombre entier valide.")

if points <= -5:
    print("Vous avez perdu ! Trop de doublons.")
else:
    print("Félicitations ! Vous avez gagné en collectant plus de 10 nombres uniques.")

