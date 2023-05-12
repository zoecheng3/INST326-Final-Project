import pandas as pd
import random as rand
import matplotlib.pyplot as plt

class Player:
  """Creates player objects for use in a guessing game.
  
  Attributes:
    name  (str) - name of player in the game
    lives (int) - number of lives the player has left
    guess (str) - guess of the player 
  """
  def __init__(self, name, lives = 8):
    """Initializes names, lives and lives for players.
    Args:
      name  (str) - name of player in the game
      lives (int) - number of lives the player has left
    """
    self.name = name
    self.lives = lives
    self.guess = None

  def guess_poke(self):
    """Allows for players to input their guesses into the game.
    """
    guess = (input(f"\n{self.name}, Guess a Pokemon: "))
    self.guess = guess

class Game(Player):
    """Creates a game object for players to use in the guessing game.
  
  Attributes:
    player1 (str) - player 1 of the game
    player2 (str) - player 2 of the game
    """
    
    def __init__(self, player1, player2):
        """Inializes players for the guessing game.
      
    Args:
      player1 (Player) - player 1 of the game
      player2 (Player) - player 2 of the game
      
    Side effects:
      Initializes player lives for each player.
      Initializes each player.
      Drops unnecessary columns in the pokemon csv file. 
      """

        self.players = [player1, player2]
        self.current_player = player1
        self.other_player = player2
        self.lives = 8
        with open("pokemon3.csv", encoding='utf -8') as f:
          df = pd.read_csv(f)
          self.new_df = df.drop(['#','HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                    axis = 1)
          sample_info = self.new_df.sample()
          self.c = dict(sample_info.iloc[0])
          answer = sample_info.sample().iloc[0]['Name']
          self.correct = answer

    def switch_turn(self):
        """Switches player turns.
        """
        self.current_player, self.other_player = self.other_player, self.current_player

    def play(self):
      """Plays pokemon guessing game and takes players guesses. Checks players guesses
    with the correct answer and gives hints depending on what each player got correct
    and incorrect. 
    
    Side effects:
      Prints player names, hints, and the number of lives each player has.
      Appends player guesses to "guesses" list for tracking. 
      
    Returns:
      Returns "guesses" - list of a players guesses
      Returns "counts"  - number of correct guesses

    """
        
      guesses = []
      correct = 0
      incorrect = 0
      print("Game Start!")
      print(self.current_player.name)
      print(self.other_player.name)
      

      while True:
        self.current_player.guess_poke()
        guesses.append(self.current_player.guess)

        if self.current_player.guess == self.correct:
          correct += 1
          print(f"Correct! The Pokemon is {self.correct}\n")
          play_again = input("Do you want to play again? (y/n) ").lower()
          if play_again == "y":
            Game.play()
          else:
            print("thanks for playing")
            break
        
        elif self.current_player.guess != self.correct: 
          incorrect += 1
          self.lives -= 1
          hint = str(self.c['Name'])[0]
          matching_row = self.new_df.loc[self.new_df['Name'] == self.current_player.guess]
          g = dict(matching_row.iloc[0])
          print(f'Not quite! You have {self.lives} lives left! Here are some hints: ') 
          if self.c['Type 1'] == g['Type 1']:
            print("You have the correct Type 1!")
            correct += 1
          else:
            print("Your Type 1 isn't correct.")
            incorrect += 1
          if self.c['Type 2'] == g['Type 2']:
            print("You have the correct Type 2!")
            correct += 1
          else:
            print("Your Type 2 isn't correct.")
            incorrect += 1
          if self.c['Generation'] == g['Generation']:
            print("You have the correct Generation!")
            correct += 1
          elif self.c['Generation'] < g['Generation']:
            print("The correct pokemon's generation is lower than the one you guessed.")
            incorrect += 1
          elif self.c['Generation'] > g['Generation']:
            print("The correct pokemon's generation is higher than the one you guessed.")
            incorrect += 1
          if self.lives == 2:
            if self.c['Legendary'] == g['Legendary']:
              print("Your guess and the correct pokemon have the same legendary status.")
              correct += 1
            else: 
              print("Your guess and the correct pokemon don't have the same legendary status.")
              incorrect += 1
          if self.lives == 1:
            print(f"Here's one final big hint. The first letter in the name of the correct pokemon is {hint}")
          if self.lives == 0:
            print(f"You've run out of guesses. The correct pokemon was {self.correct}.")
            incorrect += 1
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again == "y":
              Game.play()
            else:
              print("Thanks for playing!\n")
              break
        self.switch_turn()

      counts = [correct, incorrect]
      
      return guesses, counts

def guessing_stats(counts):
    """Display a bar chart representing the guessing statistics.
      
    Args:
        counts (list): A list containing the counts of correct and incorrect 
        guesses."""

    categories = ['Correct Guesses', 'Incorrect Guesses']

    plt.bar(categories, counts)
    plt.title("Guessing Statistics")
    plt.xlabel("Guessing Outcome")
    plt.ylabel("Count")
    plt.show()

def visualize_guesses(guesses):
    """Display a histogram representing the distribution of user guesses
      
      Args:
        guesses (list): A list of user guesses."""

    plt.hist(guesses, bins=10, edgecolor="black")
    plt.xlabel("\nPokemon")
    plt.ylabel("Frequency")
    plt.title("Distribution of User Guesses")
    plt.show()
      
def main():
  player1 = Player("Player 1")
  player2 = Player("Player 2")
    
  game = Game(player1, player2)
  guesses, counts = game.play()
  visualize_guesses(guesses)
  print("\n")
  guessing_stats(counts)
              
if __name__ == '__main__':
    main()
