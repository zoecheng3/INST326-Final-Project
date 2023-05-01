import pandas as pd
import random

class Pokemon:
  def __init__(self,fire, grass, water):
    self.fire = fire
    self.grass = grass
    self.water = water
    

  def attribute_checker(self, object):
    self.object = object
    if self.object == self.fire:
      print('Youve chosen a fire pokemon')


def play_game():
  correct_answer = random.choice()
  lives = 5
  while lives > 0:
    guess = input("Guess a Pokemon: ")
    if guess = correct answer:
      print(f"Correct! The Pokemon is {correct_answer}")
    else:
      lives -=1
      print(f"Incorrect, you have {lives} guesses left")
    if lives == 0:
      print(f"You ran out of guesses, the Pokemon was {correct_answer}")
  play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
      play_game()
    else:
      print("Thanks for playing!")
      
                     
                     
                     
                     
def get_rand_poke(poke_list):
  return random.choice(poke_list)
  
  
  

 
if __name__ == '__main__':
  main()
  
