import random
import re
from hangman_extras import stages, logo, word_list

#Lists of "Words" bank and choose random word
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guess_list = []

#Welcome user, Run each function
def main():
  #Set Player lives
  lives = 6
  print(logo)
  print("Welcome to 100 Days of coding in Python: Hangman Edition")
  print(f"The secret word is {len(chosen_word)} letters long")

  #Checking if guess is in the word
  while "_" in display and lives > 0:
    guess = get_guess(guess_list)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"Sorry, {guess} is not in the word. You have {lives} lives left")
    else:
      print(stages[lives])
      print(f"Your guess of: {guess} was correct!")
    check_letter(chosen_word, display, guess)

    
  #Checking if "_" is still in display(Win Condition)
  if "_" not in display:
    print(f"Congratulations, You've guessed the word: {chosen_word}")
  else:
    print(f"Sorry, you lose, the correct word was: {chosen_word}")
   
#Ensure the input provided is valid
def get_guess(guess_list):
  try:
    while True:
      guess = input("Please guess a letter: ").lower()
      if _ := re.search(r"[a-z]", guess):
        if guess in guess_list:
          print(f"You have already tried to guess the letter: {guess}")
        else:
          guess_list.append(guess)
          break
      else:
        print("***---Invalid choice, please choose a letter [a-z]---***")
        continue
  except ValueError as e:
    print(f"Error: {e}")
  return guess

#Determine if guessed letter is in chosen_word string and update display
def check_letter(chosen_word, display, guess):
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = guess
  print(" ".join(display))
  

if __name__ == "__main__":
  main()

       
        

  