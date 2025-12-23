# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def display_advertisement(**info):
    """Affiche les informations d'une annonce immobilière.

    Args:
        **info: Arguments mot-clé représentant les détails de l'annonce.
    """
    print("Annonce Immobilière:")
    print("---------------------")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")


# Exemple d'appel de la fonction
display_advertisement(type="Appartement", location="Dakar", price="350,000 FCFA", bedrooms=2, bathrooms=1)