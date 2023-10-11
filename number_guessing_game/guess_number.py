# Import Libraries/Modules
import random
from art import logo
from rich import print as rprint
import os

def main():
	while True: 
		clear_screen()
		number = random.randint(1,100)
		print(logo)
		print("Welcome to the secret number game!")
		print("I'm thinking of a number between 1 - 100.")
		rprint("Please choice a difficulty: [red]'Hard'= 5 guesses[/red], [green]'Easy' 10 guesses[/green]")
		attempts = get_level()
		while attempts > 0:
			rprint(f"You have [blue]{attempts} guesses[/blue] remaining!")
			guess = get_guess()
			if guess == number:
				rprint(f"[green]You Win!! The correct number was {number}. Thanks for playing[/green]")
				break
			elif guess < number:
				rprint("[yellow]Your guess is too low[/yellow]")
				attempts -= 1
				pass
			elif guess > number:
				rprint("[yellow]Your guess is too high[/yellow]")
				attempts -= 1
				pass
			else:
				print("Invalid guess")
				pass
		if attempts == 0:
			rprint(f"[red]Sorry, the correct number was {number}![/red]")
		keep_playing = input("Would you like to keep playing y = yes n = no: ").lower()
		if keep_playing == "y":
			pass
		else:
			clear_screen()
			break
					
# Obtain the level and set guesses	
def get_level():
	while True:
		choice = input("Type 'H' or 'Hard' for Hard | Type 'E' or 'Easy' for easy: ").lower()
		try:
			if choice == "h" or choice == "hard":
				return 5
			elif choice == "e" or choice == "easy":
				return 10
				break
			else:
				rprint("[yellow]Invalid Option Please try again![/yellow]")
		except Exception as e:
			rprint("[red]Error: ", str(e))

# Prompt user for a guess
def get_guess():
	while True:
		try:
			guess = int(input("Please enter your guess: "))
			return guess
		except Exception as e:
			rprint("[red]Error: ", str(e))

# Clear the screen for player
def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')
	
if __name__ == "__main__":
	main()