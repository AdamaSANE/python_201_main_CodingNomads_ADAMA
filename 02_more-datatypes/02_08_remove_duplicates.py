# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]
# Convertir en ensemble puis revenir en liste pour supprimer les doublons
no_duplicates = list(set(list_))
print(no_duplicates)

# Utiliser une boucle et une deuxième liste pour supprimer les doublons manuellement
no_duplicates_manual = []
for item in list_:
    if item not in no_duplicates_manual:
        no_duplicates_manual.append(item)
print(no_duplicates_manual)
