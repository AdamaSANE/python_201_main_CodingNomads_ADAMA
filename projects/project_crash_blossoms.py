# Crash Blossoms : exemple unique
# Ce script détecte et génère des titres ambigus (crash blossoms)
import random

def detect_crash_blossom(headline):
	"""Détecte la présence de mots ambigus dans un titre."""
	ambiguous_words = ['push', 'holds', 'helps', 'leaves', 'blossoms', 'bites', 'shoots', 'strikes']
	return any(word in headline.lower() for word in ambiguous_words)

def generate_crash_blossom():
	"""Génère un titre crash blossom aléatoire."""
	templates = [
		"{subject} {verb} {object}",
		"{object} {verb} by {subject}",
		"{subject} {verb} up {object}",
	]
	subjects = ["Squad", "Red tape", "Violinist", "Army", "Dog", "Infant"]
	verbs = ["helps", "holds", "pushes", "bites", "pulls", "shoots"]
	objects = ["dog bite victim", "new bridge", "bottles up German rear", "JAL crash blossoms", "car", "Germans"]
	template = random.choice(templates)
	return template.format(subject=random.choice(subjects), verb=random.choice(verbs), object=random.choice(objects))

print("Analyse d'exemples :")
headlines = [
	"Violinist linked to JAL crash blossoms",
	"Squad helps dog bite victim",
	"Red tape holds up new bridge",
	"French push bottles up German rear",
	"Infant pulled from wrecked car involved in short police pursuit"
]
for h in headlines:
	print(f"{h} : {'Crash Blossom' if detect_crash_blossom(h) else 'Clair'}")

print("\nGénération de crash blossoms :")
for _ in range(3):
	print(generate_crash_blossom())
