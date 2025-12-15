
# Lit le contenu de words.txt et écrit les lignes à l'envers dans words_reverse.txt
with open('words.txt', 'r', encoding='utf-8') as fichier:
	lignes = fichier.readlines()

with open('words_reverse.txt', 'w', encoding='utf-8') as fichier_reverse:
	for ligne in reversed(lignes):
		fichier_reverse.write(ligne)

print("Le contenu a été écrit à l'envers dans words_reverse.txt")
