#This will be the test code for the function
import pandas as pd
import random as rand




def play_game():
  with open('pokemon3.csv', encoding = 'utf -8') as f:
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
      
  
  
  
  
  
  
  
  



          
            
      
  
  
  
#Beginning of a hint class

 class Hint:
    def __init__(self, pokemon_file):
        self.pokemon_file = pokemon_file
    
    def give_hint(self, player_answer):
        with open(self.pokemon_file, 'r') as file:
                values = line.strip().split(',’) 
                if player_answer.lower() == values[1].lower():
                    pokemon_type = values[2]
                    generation = values[3]
                    legendary = values[12]
                    hint = f"The Pokemon is a {pokemon_type} type from generation {generation}."
                    if legendary == 'True':
                        hint = "It is a legendary Pokemon."
                    else:
                        hint = "It is not a legendary Pokemon."
                    return hint
        return "Sorry, I couldn't find that Pokemon. Please try again."
Give_hint= HintGiver('pokemon.csv')
player_answer = input("Guess the Pokemon: ")
hint = give_hint.give_hint(player_answer)
print(hint)

