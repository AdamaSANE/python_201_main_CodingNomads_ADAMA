# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
    Convertit une distance en kilomètres en miles.

    Args:
        km (float): La distance en kilomètres à convertir.

    Returns:
        float: La distance convertie en miles.
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
