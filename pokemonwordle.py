#Updated code with data vis functions
import pandas as pd
import random as rand
import matplotlib.pyplot as plt

def play_game():
  guesses = []
  correct = 0
  incorrect = 0

  with open("/pokemon2 - pokemon2.csv.csv", encoding='utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    sample_info = new_df.sample()
    c = dict(sample_info.iloc[0])
    poke = sample_info.sample().iloc[0]['Name']
  correct_answer = poke
  
  lives = 8
  
  while lives > 0:
    player_guess = input('\nGuess the pokemon: ')
    guesses.append(player_guess)

    if player_guess == correct_answer:
      correct += 1
      print(f"Correct! The Pokemon is {correct_answer}\n")
      play_again = input("Do you want to play again? (y/n) ").lower()
      if play_again == "y":
        play_game()
      else:
        break
        print("thanks for playing")
    elif player_guess != correct_answer: 
      incorrect += 1
      lives -= 1
      hint = c['Name'][0]
      matching_row = new_df.loc[new_df['Name'] == player_guess]
      g = dict(matching_row.iloc[0])
      print(f'Not quite! You have {lives} lives left! Here are some hints: ') 
      if c['Type 1'] == g['Type 1']:
        print("You have the correct Type 1!")
        correct += 1
      else:
        print("Your Type 1 isn't correct.")
        incorrect += 1
      if c['Type 2'] == g['Type 2']:
        print("You have the correct Type 2!")
        correct += 1
      else:
        print("Your Type 2 isn't correct.")
        incorrect += 1
      if c['Generation'] == g['Generation']:
        print("You have the correct Generation!")
        correct += 1
      elif c['Generation'] < g['Generation']:
        print("The correct pokemon's generation is lower than the one you guessed.")
        incorrect += 1
      elif c['Generation'] > g['Generation']:
        print("The correct pokemon's generation is higher than the one you guessed.")
        incorrect += 1
      if lives == 2:
        if c['Legendary'] == g['Legendary']:
          print("Your guess and the correct pokemon have the same legendary status.")
          correct += 1
        else: 
          print("Your guess and the correct pokemon don't have the same legendary status.")
          incorrect += 1
      if lives == 1:
        print(f"Here's one final big hint. The first letter in the name of the correct pokemon is {hint}")
  if lives == 0:
    print(f"You've run out of guesses. The correct pokemon was {correct_answer}.")
    incorrect += 1
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "y":
      play_game()
    else:
      print("Thanks for playing!\n")

  counts = [correct, incorrect]
  
  return guesses, counts

def guessing_stats(counts):
  categories = ['Correct Guesses', 'Incorrect Guesses']

  plt.bar(categories, counts)
  plt.title("Guessing Statistics")
  plt.xlabel("Guessing Outcome")
  plt.ylabel("Count")
  plt.show()

def visualize_guesses(guesses):
  plt.hist(guesses, bins=10, edgecolor="black")
  plt.xlabel("\nPokemon")
  plt.ylabel("Frequency")
  plt.title("Distribution of User Guesses")
  plt.show()
      
      
if __name__ == '__main__':
    guesses, counts = play_game()
    visualize_guesses(guesses)
    guessing_stats(counts)






#This will be the test code for the function

import pandas as pd
import random as rand

class Dataframe:

  def __init__(self):
    with open('Pokemon3.csv', encoding = 'utf-8') as f:
       df = pd.read_csv(f)
       self.new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)


def open_game(file):
  with open('Pokemon3.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    sample_info = new_df.sample()
   
  return sample_info


def play_game():
  data_info = Dataframe
  c = dict(open_game('Pokemon3.csv').iloc[0])
  poke = open_game('Pokemon3.csv').sample().iloc[0]['Name']
  correct_answer = poke
  data = Dataframe()
  

  lives = 8

  while lives > 0:
    player_guess = input('Guess the pokemon: ')
    if player_guess == correct_answer:
        print(f"Correct! The Pokemon is {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()
        else:
          break
    elif player_guess != correct_answer: 
      lives -= 1
      hint = c['Name'][0]
      matching_row = data.new_df.loc[data.new_df['Name'] == player_guess]
      g = dict(matching_row.iloc[0])
      print(f'Not quite! You have {lives} lives left! Here are some hints:') 
      if c['Type 1'] == g['Type 1']:
        print("You have the correct Type 1!")
      else:
        print("Your Type 1 isn't correct.")
      if c['Type 2'] == g['Type 2']:
        print("You have the correct Type 2!")
      else:
        print("Your Type 2 isn't correct.")
      if c['Generation'] == g['Generation']:
        print("You have the correct Generation!")
      elif c['Generation'] < g['Generation']:
        print("The correct pokemon's generation is lower than the one you guessed.")
      elif c['Generation'] > g['Generation']:
        print("The correct pokemon's generation is higher than the one you guessed.")
      if lives == 2:
        if c['Legendary'] == g['Legendary']:
          print("Your guess and the correct pokemon have the same legendary status.")
        else: 
          print("Your guess and the correct pokemon don't have the same legendary status.")
      if lives == 1:
        print(f"Here's one final big hint. The first letter in the name of the correct pokemon is {hint}")
  if lives == 0:
    print(f"You've run out of guesses. The correct pokemon was {correct_answer}.")
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
            play_game()
    else:
      print("Thanks for playing!")
      
      
if __name__ == '__main__':
    play_game()
  
  
  
  
  
  
  
  



          
            
      #Here is the original working game
  
  
  
import pandas as pd
import random as rand



def play_game():
  with open('Pokemon3.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    sample_info = new_df.sample()
    c = dict(sample_info.iloc[0])
    poke = sample_info.sample().iloc[0]['Name']
  correct_answer = poke
  
  lives = 8

  while lives > 0:
    player_guess = input('Guess the pokemon: ')
    if player_guess == correct_answer:
        print(f"Correct! The Pokemon is {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()
        else:
          break
    elif player_guess != correct_answer: 
      lives -= 1
      hint = c['Name'][0]
      matching_row = new_df.loc[new_df['Name'] == player_guess]
      g = dict(matching_row.iloc[0])
      print(f'Not quite! You have {lives} lives left! Here are some hints:') 
      if c['Type 1'] == g['Type 1']:
        print("You have the correct Type 1!")
      else:
        print("Your Type 1 isn't correct.")
      if c['Type 2'] == g['Type 2']:
        print("You have the correct Type 2!")
      else:
        print("Your Type 2 isn't correct.")
      if c['Generation'] == g['Generation']:
        print("You have the correct Generation!")
      elif c['Generation'] < g['Generation']:
        print("The correct pokemon's generation is lower than the one you guessed.")
      elif c['Generation'] > g['Generation']:
        print("The correct pokemon's generation is higher than the one you guessed.")
      if lives == 2:
        if c['Legendary'] == g['Legendary']:
          print("Your guess and the correct pokemon have the same legendary status.")
        else: 
          print("Your guess and the correct pokemon don't have the same legendary status.")
      if lives == 1:
        print(f"Here's one final big hint. The first letter in the name of the correct pokemon is {hint}")
  if lives == 0:
    print(f"You've run out of guesses. The correct pokemon was {correct_answer}.")
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
            play_game()
    else:
      print("Thanks for playing!")
      
      
if __name__ == '__main__':
    play_game()
