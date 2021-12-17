import random
import pdb

rock = 0
paper = 1
scissors =2

ACTION = ["smashes","smothers","slices"]
WIN_CONDITIONS = [(rock,scissors),(paper,rock),(scissors,paper)]
USER_INPUT = {
	'r':rock,
	'rock':rock,
	'p':paper,
	'paper':paper,
	's':scissors,
	'scissors':scissors
}

def getuser():
	while True:
		print("Take your pick : Rock,Scissors, Paper")
		user_input = USER_INPUT.get(input().lower())
		if user_input is not None:
			return user_input

def display_winner(user, comp):
	if user==comp:
		print("Draw!")
	else:
		user_wins = (user,comp) in WIN_CONDITIONS
		winner,loser = (user,comp) if user_wins else (comp,user)
		print(f'Winner Sample {winner}, loser Sample {loser}')
		print(f"You {'win' if user_wins else 'lose'} - {winner} {ACTION[winner]} {loser}")

if __name__ == "__main__":
	again ='yes'
	while again != 'no':
		user = getuser()
		print(f'User : {user}')
		keyss = random.choice(list(USER_INPUT))
		comp = USER_INPUT.get(keyss)
		print(f'{comp}, comp input')
		display_winner(user,comp)
		again = input('yes or no?')
