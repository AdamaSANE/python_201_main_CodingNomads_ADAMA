
# Lit le fichier words.txt et affiche les mots de plus de 20 caractères (hors espaces).
with open('words.txt', 'r', encoding='utf-8') as fichier:
	for ligne in fichier:
		mot = ligne.strip()
		if len(mot.replace(' ', '')) > 20:
			print(mot)
