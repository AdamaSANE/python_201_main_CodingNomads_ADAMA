# Simple CLI Game with File I/O and Functions
import os
import json

STATE_FILE = "game_state.json"

def load_state(filename: str = STATE_FILE) -> dict:
	"""
	Load the game state from a file. Returns a dictionary.
	"""
	if os.path.exists(filename):
		with open(filename, 'r') as f:
			return json.load(f)
	return {"inventory": [], "score": 0}

def save_state(state: dict, filename: str = STATE_FILE) -> None:
	"""
	Save the game state to a file.
	"""
	with open(filename, 'w') as f:
		json.dump(state, f)

def add_to_inventory(state: dict, item: str) -> None:
	"""
	Add an item to the player's inventory.
	"""
	state["inventory"].append(item)
	print(f"Added {item} to your inventory.")

def show_inventory(state: dict) -> None:
	"""
	Display the player's inventory.
	"""
	print("Your inventory:", state["inventory"])

def increase_score(state: dict, points: int) -> None:
	"""
	Increase the player's score.
	"""
	state["score"] += points
	print(f"Your score is now {state['score']}.")

def main():
	"""
	Main game loop.
	"""
	state = load_state()
	print("Welcome to the CLI Adventure Game!")
	while True:
		print("\nChoose an action:")
		print("1. Add item to inventory")
		print("2. Show inventory")
		print("3. Increase score")
		print("4. Save and quit")
		choice = input("> ")
		if choice == "1":
			item = input("Enter item name: ")
			add_to_inventory(state, item)
		elif choice == "2":
			show_inventory(state)
		elif choice == "3":
			try:
				points = int(input("How many points? "))
				increase_score(state, points)
			except ValueError:
				print("Please enter a valid number.")
		elif choice == "4":
			save_state(state)
			print("Game saved. Goodbye!")
			break
		else:
			print("Invalid choice. Try again.")

main()
