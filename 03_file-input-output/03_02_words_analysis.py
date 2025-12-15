
# Lit tous les mots du fichier words.txt, puis affiche :
# 1. Le(s) mot(s) le(s) plus court(s)
# 2. Le(s) mot(s) le(s) plus long(s)
# 3. Le nombre total de mots

with open('words.txt', 'r', encoding='utf-8') as fichier:
	mots = [ligne.strip() for ligne in fichier if ligne.strip()]

if mots:
	longueur_min = min(len(m) for m in mots)
	longueur_max = max(len(m) for m in mots)
	mots_min = [m for m in mots if len(m) == longueur_min]
	mots_max = [m for m in mots if len(m) == longueur_max]

	print(f"Mot(s) le(s) plus court(s) ({longueur_min} caractères) : {', '.join(mots_min)}")
	print(f"Mot(s) le(s) plus long(s) ({longueur_max} caractères) : {', '.join(mots_max)}")
	print(f"Nombre total de mots : {len(mots)}")
else:
	print("Aucun mot trouvé dans le fichier.")
