# Écrit les comptes de fichiers dans un fichier `.csv`.
import csv

# Exemple de données à écrire
file_counts = [
	{'type': 'txt', 'count': 5},
	{'type': 'csv', 'count': 3},
	{'type': 'json', 'count': 2}
]

with open('filecounts.csv', 'w', newline='', encoding='utf-8') as csvfile:
	fieldnames = ['type', 'count']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for row in file_counts:
		writer.writerow(row)

print("Comptes de fichiers écrits dans filecounts.csv")
