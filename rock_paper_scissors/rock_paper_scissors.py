rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#import random module 
import random

#Define a list full of choices the cpu can choose from
choices = [rock, paper, scissors]
print("Welcome to the official 100 Days of Code Python: Rock, Papper, Scissors Game!")

while True:
  #Gather user input
  player_choice = input("Please Choose 0: Rock, 1: Paper, 2: scissors: \n")

  #Validate user input against known options
  if player_choice not in ("0", "1", "2"):
    print("!!!---Invalid Choice, Please enter either: 0, 1, or, 2---!!!")
    continue

  #Computer Chooses an option
  cpu_choice = random.choice(choices)

  #Show Player thier choice
  print("You chose: \n")
  if player_choice == "0":
    print(rock)
  elif player_choice == "1":
    print(paper)
  else:
    print(scissors)
  
  #Player Selects Rock 
  if player_choice == "0":
    if cpu_choice == scissors:
      print(f"CPU Chose: \n {cpu_choice}")
      print("You Win, congratulations, but I am just getting warmed up!")  
    elif cpu_choice == paper:
      print(f"CPU Chose: \n {cpu_choice}")
      print("You Lose, better luck next time!!!")
    elif cpu_choice == rock:
      print(f"CPU Chose: \n {cpu_choice}")
      print("It's a tie, no wayyyyy!!!") 
      
  #Player Selects Paper      
  elif player_choice == "1":
    if cpu_choice == scissors:
      print(f"CPU Chose: \n{cpu_choice}")
      print("You Lose, better luck next time!!!")
    elif cpu_choice == paper:
      print(f"CPU Chose: \n{cpu_choice}")
      print("It's a tie, no wayyyyy!!!")
    elif cpu_choice == rock:
      print(f"CPU Chose: \n{cpu_choice}")
      print("You Win, congratulations, but I'm just getting warmed up!!!")

  #Player Selects scissors
  elif player_choice == "2":
    if cpu_choice == scissors:
      print(f"CPU Chose: \n{cpu_choice}")
      print("It's a tie, no wayyyyy!!!")
    elif cpu_choice == paper:
      print(f"CPU Chose: \n{cpu_choice}")
      print("You Win, congratulations, but I'm just getting warmed up!!!")
    elif cpu_choice == rock:
      print(f"CPU Chose: \n{cpu_choice}")
      print("You Lose, better luck next time!!!")

  #Give user the option to play again
  play_again = input("Would you like to play again, Y - Yes, N - No: \n").lower()
  if play_again != "y":
    break
    
  
    
      
    



