# Import libraries/modules
from coffe_machine_data import menu, resources, logo
from rich import print as rprint
import os
import sys

total_money = 0

def main():
    clear_screen()
    print(logo)
    print("Welcome to the Java Express Coffe Machine!")
    option_screen()

# Print out the options
def option_screen():
    while True:
        print("""Menu:
            1: Show available resources
            2: Purchase a coffee
            3: Maintenance Mode
            Q: Quit
            """)
        choice = input("Please Select a menu item: ")
        match choice:
            case "1": 
                show_resources()
            case "2": 
                purchase_coffee(choose_coffee())
            case "3":
                maintenance_mode(total_money)
            case "q":
                sys.exit("Have a good day!")
            case _:
                "Please choose a valid option"

# Show Resources
def show_resources():
    rprint(f"""[blue]Current resources available:
          Water: {resources["water"]} ml
          Milk: {resources["milk"]} ml
          Coffee: {resources["coffee"]} ml
          [/blue]""")

# Maintenance mode
def maintenance_mode(money=None):
    clear_screen()
    rprint("[yellow]System is now in maintenance mode[/yellow]")
    while True:
        print("""Menu:
        1: Show money being stored in system
        2: Unlock maintenance door bays
        3: Main Menu
        4: Turn off
        """)
        option = input("Please select an option: ")
        match option:
            case "1":
                total_money = money if money is not None else 0
                print(f"Total: ${total_money:.2f}")
            case "2":        
                print("[green]Door Bays unlocked[/green]")
            case "3":
                option_screen()
            case "4":
                sys.exit("System is shut down")

# Choose which coffee they want
def choose_coffee():
    clear_screen()
    print("""Please Select a Coffee:
        1: Espresso
        2: Latte
        3: Cappuccino
        """)
    coffee_choice = input("Please select an option: ")
    match coffee_choice:
        case "1":
            cost = menu['espresso']['cost']
            print(f"Esspresso costs ${cost:.2f}.")
            return cost
        case "2":  
            cost = menu['latte']['cost']      
            print(f"Latte costs ${cost:.2f}.")
            return cost
        case "3":
            cost = menu['cappuccino']['cost']
            print(f"Cappuccino costs ${cost:.2f}.")
            return cost

# Purchase Coffee
def purchase_coffee(total):
    global total_money
    amount_owed = total
    print(f"Amount due: ${amount_owed:.2f}")
    while amount_owed > 0:
        try:
            deposit = float(input("Please insert change: $"))
            if deposit >= 0:
                amount_owed -= deposit
                if amount_owed < 0:
                    change_due = abs(amount_owed)
                    rprint(f"[green]Change due: ${change_due:.2f}[/green]")
                    total_money += amount_owed
                elif amount_owed == 0:
                    rprint("[green]Thank you for your payment[/green]")
                    total_money += amount_owed
                else:
                    rprint(f"[blue]Remaining amount due: ${amount_owed:.2f}[/blue]")
            else:
                rprint("[yellow]Error: [/yellow] Please enter a positive amount.")
        except ValueError as e:
            rprint("[yellow]Error: [/yellow]", str(e))

# Clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()