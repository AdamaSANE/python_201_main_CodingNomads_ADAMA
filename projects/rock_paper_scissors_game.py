# Rock-Paper-Scissors Game
# This script lets a user play rock-paper-scissors against the computer.
import random

def get_hand(hand):
	"""
	Returns the string representation of the hand.
	0 = scissor, 1 = rock, 2 = paper
	"""
	hands = ["scissor", "rock", "paper"]
	return hands[hand]

def determine_winner(user, computer):
	"""
	Determines the winner: returns 'User', 'Computer', or 'Tie'.
	"""
	if user == computer:
		return "Tie"
	# Rules: scissor beats paper, paper beats rock, rock beats scissor
	if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
		return "User"
	else:
		return "Computer"

# Get user input
user_input = int(input("Enter your hand (0 = scissor, 1 = rock, 2 = paper): "))
computer_input = random.randint(0, 2)

# Get hand names
user_hand = get_hand(user_input)
computer_hand = get_hand(computer_input)

# Determine winner
winner = determine_winner(user_input, computer_input)

# Print results
print(f"You played: {user_hand}")
print(f"Computer played: {computer_hand}")
if winner == "Tie":
	print("It's a tie!")
else:
	print(f"{winner} wins!")
