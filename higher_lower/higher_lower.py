# Import libraries
from art import logo, vs
from game_data import data
import os
from rich import print as rprint
import random

# Main function
def main():
    play_game()

# Function that runs the game
def play_game():
    score = 0
    lives = 1
    while lives > 0:
        clear_screen()
        print(logo)
        rprint(f"[green]Your current score is: {score}[/green]")
        data_entry1 = get_entry()
        data_entry1_followers = data_entry1['follower_count']
        data_entry2 = get_entry()
        data_entry2_followers = data_entry2['follower_count']
        rprint(f"[blue]Compare A: {data_entry1['name']}, {data_entry1['description']}, {data_entry1['country']} [/blue]")
        print(vs)
        rprint(f"[yellow]Against B: {data_entry2['name']}, {data_entry2['description']}, {data_entry2['country']}[/yellow]")
        print(data_entry1_followers, data_entry2_followers)
        choice = get_choice()
        if choice == "a":
            if data_entry1_followers > data_entry2_followers:
                score += 1
                rprint(f"[green]You're correct {data_entry1['name']} has {data_entry1_followers} followers, while {data_entry2['name']} has {data_entry2_followers}!")
            else:
                rprint(f"[red]Sorry, your choice was not correct. Total score: {score} [/red]")
                break
        elif choice == "b":
            if data_entry2_followers > data_entry1_followers:
                score += 1
                rprint(f"[green]You're correct {data_entry1['name']} has {data_entry1_followers} followers, while {data_entry2['name']} has {data_entry2_followers}!")
            else:
                rprint(f"[red]Sorry, your choice was not correct. Total score: {score} [/red]")
                break

# Function to obtain user's choice
def get_choice():
    while True:
        option = input("Who has more followers? 'A' = A, 'B' = B: ").lower()
        if option == "a":
            return "a"
        elif option == "b":
            return "b"
        else:
            print("Please select a valid option: 'A' or 'B'")
            pass

# Function to get a random data entry
def get_entry():
    return random.choice(data)

# Function to clear screen based on OS
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        print("Unable to clear screen")

if __name__ == "__main__":
    main()