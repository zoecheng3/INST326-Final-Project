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
                     
                     
            if __name__ == '__main__':
  
  
  
  
