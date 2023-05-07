#This will be the test code for the function

import pandas as pd
import random as rand
def pokemon_wordle(file):
  with open('pokemon.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    
    poke_choice = list(new_df['Name'])

    for name in poke_choice:
      game_choice = rand.choice(poke_choice)
  return game_choice

    



def play_game():
  
  testf = 'pokemon.csv'
  correct_answer = pokemon_wordle(testf)
  print(f'Correct answer: {correct_answer}')
  lives = 5

  
  while lives > 0:
      answer = input('Guess the pokemon: ') 
      if answer == correct_answer:
        print(f"Correct! The Pokemon is {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()
        else:
            break ; print("Thanks for playing!")
            
      else:
        lives -=1
        print(f"Incorrect, you have {lives} guesses left")
        
      if lives == 0 and answer != correct_answer:
        print(f"You ran out of guesses, the Pokemon was {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()
        else:
            break ;print("Thanks for playing!")
      
      



      #Here is how you choose a specific index from the sample that is randomly chosesn. This syntax will be very useful for our hint class
      ---->  new_df.sample().iloc[0]['Name']
                     
           #this lets us get the entire row of information from the sample and also just take the name of that same so we can compare it with the player's guess
          sample_info = new_df.sample()
l = dict(sample_info.iloc[0])
poke = sample_info.sample().iloc[0]['Name']
print(l)
print(poke)


            if __name__ == '__main__':
  
  
  
  
  
  
  
  
  
  
  
  
  
  #Heres what I was working on with hints
  #This will be the test code for the function

import pandas as pd
import random as rand


"""def pokemon_wordle(file):
  with open('pokemon.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)

    raw_sample = new_df.sample()
    poke_stats = dict(sample_info.iloc[0])
    pokemon = raw_sample.sample().iloc[0]['Name']


  return pokemon"""

def play_game():
  with open('pokemon.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    raw_sample = new_df.sample()
    poke_stats = dict(sample_info.iloc[0])
    pokemon = raw_sample.sample().iloc[0]['Name']
  
  correct_answer = pokemon
  #print(f'Correct answer: {correct_answer}')
  
  lives = 5

  
  while lives > 0:
    player_guess = input('Guess the pokemon: ')
    if player_guess == correct_answer:
        print(f"Correct! The Pokemon is {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()

    elif player_guess != correct_answer: 
      lives -= 1
      hint = poke_stats['Type 1']
      print(f'Good guess but not quite. You have {lives} left! Heres a hint! Youre looking for a {hint} type pokemon')

    elif player_guess != correct_answer:
      lives-= 1
      hint2 = poke_stats['Generation']
      print(f'Not quite. You have {lives} left. Heres another hint: The pokemon is a {hint2} generation')

    elif player_guess != correct_answer:
      lives -= 1
      hint3 = poke_stats['Name'][0]
      print(f'Nope. Heres your final hint: The pokemon begins with the letter {hint3} ')
            
    else:
        lives -=1 
        print(f"Incorrect, you have {lives} guesses left")
        
    if lives == 0 and player_guess != correct_answer:
        print(f"You ran out of guesses, the Pokemon was {correct_answer}")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            play_game()
        else: 
          print("Thanks for playing!")
          print(poke_stats)
          
            
      
  
  
  
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

