# Utilise le module `csv` pour lire le fichier et compter les types de fichiers.
import csv
from collections import Counter

with open('filecounts.csv', newline='', encoding='utf-8') as csvfile:
	reader = csv.DictReader(csvfile)
	types = [row['type'] for row in reader]
	compteur = Counter(types)

print("Nombre de fichiers par type :")
for type_fichier, nombre in compteur.items():
	print(f"{type_fichier}: {nombre}")
