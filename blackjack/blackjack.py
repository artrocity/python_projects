# Import libraries
import os
import random
from art import logo
import sys
from rich import print as rprint



def main():
    # Blackjack Game Intro
    clear_screen()
    print(logo)
    balance = 1_000
    while True:
        print("Would you like to play a round of Blackjack?")
        rprint(f"[blue]Your current balance is: ${balance}[/blue]")
        choice = input("Enter 'y' for yes or 'n' for no: ").lower()
        if choice == "y" or choice == "yes":
            clear_screen()
            print(logo)

            #Obtain player bet
            rprint(f"[blue]Your current balance is: ${balance}[/blue]")
            bet = int(input(f"How much would you like to bet? (1 - {balance}): "))

            #Deal first round of cards
            player_hand = deal_cards(2)
            house_hand = deal_cards(2)
            rprint(f"[green]Your Cards are: {player_hand} with a total score of {calc_sum_hand(player_hand)}[/green]")
            rprint(f"[red]The House's first card is {house_hand[0]}[/red]")

            #Hit or stay
            while True:
                keep_playing = input("Enter 'hit' for a new card or 'stay' to stay: ").lower()
                if keep_playing == "hit":
                    player_hand += deal_cards(1)
                    rprint(f"[green]Your Cards are: {player_hand} with a total score of {calc_sum_hand(player_hand)}[/green]")
                    if calc_sum_hand(player_hand) >= 21:
                        break
                elif keep_playing == "stay":
                    break
                else:
                    rprint("[yellow]Please enter a valid option[/yellow]")
                    continue
            result_message = compare(player_hand, house_hand)
            rprint(result_message)
            
            # Update balance based on the result
            if "win" in result_message:
                balance += bet
            elif "lose" in result_message:
                balance -= bet
            elif "draw" in result_message:
                pass

            # Check if player has enough balance to continue
            if balance <= 0:
                rprint("[red]You've run out of funds! Thanks for playing![/red]")
                break
        elif choice == "n" or choice == "no":
            sys.exit("Come back and play again!")
        else:
            rprint("[yellow]Please enter a valid option[/yellow]")
    
# Deal n cards
def deal_cards(n):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand = []
    for _ in range(n):
        hand.append(random.choice(cards))
    return hand

# Calc sum of n cards
def calc_sum_hand(hand):
    hand_sum = sum(hand)

    ace_count = hand.count(11)
    while hand_sum > 21 and ace_count:
        hand_sum -= 10
        ace_count -=1
    return hand_sum

def is_blackjack(hand):
    return sorted(hand) in [[10, 11], [10, 10]]

# Compare each hand and determine winner
def compare(player_hand, house_hand):
    player_sum = calc_sum_hand(player_hand)
    house_sum = calc_sum_hand(house_hand)
    
    # Checking for Blackjacks or Busts
    if player_sum > 21:
        return f"[red]You busted and lose with: {player_sum}, {player_hand}. The house had: {house_sum}, {house_hand}.[/red]"
    elif house_sum == player_sum:
        return f"[yellow]It's a draw, the house had : {house_sum}, {house_hand}. You had: {player_sum}, {player_hand}.[/yellow]"
    elif is_blackjack(house_hand):
        return f"[red]You lose, House had a Blackjack: {house_sum}, {house_hand}. You had: {player_sum}, {player_hand}.[/red]"
    elif is_blackjack(player_hand):
        return f"[green]You win with a Blackjack: {player_sum}, {player_hand}. The house had: {house_sum}, {house_hand}.[/green]"
    
    
    # Updating house_sum after house takes new cards
    while calc_sum_hand(house_hand) < 17:
        house_hand += deal_cards(1)
    
    # Updating house_sum after house takes new cards
    house_sum = calc_sum_hand(house_hand)  
    
    #Comparing values to determine winner
    if house_sum > 21:
        return f"[green]House busted with: {house_sum}, {house_hand}. You win with: {player_sum}, {player_hand}.[/green]"
    elif player_sum > house_sum:
        return f"[green]You win with: {player_sum}, {player_hand}. The house had: {house_sum}, {house_hand}.[/green]"
    else:
        return f"[red]You lose, House had: {house_sum}, {house_hand}. You had: {player_sum}, {player_hand}.[/red]"
    
# Clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    main()