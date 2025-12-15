
# Exemple : Utiliser pathlib pour lire et écrire un fichier CSV, avec gestion du chemin
from pathlib import Path
import csv

# Définir le chemin du fichier CSV de façon relative au script
base_dir = Path(__file__).parent
csv_path = base_dir / 'file-counter' / 'filecounts.csv'

# Lecture du fichier CSV
if csv_path.exists():
	with csv_path.open('r', newline='', encoding='utf-8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(row)
else:
	print(f"Le fichier {csv_path} n'existe pas.")

# Exemple d'écriture (ajout d'une ligne)
with csv_path.open('a', newline='', encoding='utf-8') as csvfile:
	fieldnames = ['type', 'count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	# writer.writeheader()  # Décommente si le fichier est vide
	writer.writerow({'type': 'exemple', 'count': 1})
