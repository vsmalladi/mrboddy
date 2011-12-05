'''
Created on Nov 5, 2011

@author: bryanj
'''

from player import Player
from game import Game
from board import Board
from gamerules import GameRules

def main():
    
   current_game = Game()
   
   # ask for number of players
   while True:
      num_players = int(raw_input("Please choose the number of players to play(3-6): "))
      if num_players >=3 and num_players <=6:
         break
      else:
         print "You must have a minimum of 3 players and max of 6"
   
      # Initialize players
   players = []
   for i in range(1,num_players+1):
      if i == 1:
         name = raw_input("Please Enter name for player 1: ")
         Player1 = Player(name)
         Player1.position = "Hall-Lounge"
         players.append(Player1)
      elif i == 2:
         name = raw_input("Please Enter name for player 2: ")
         Player2 = Player(name)
         Player2.position = "Lounge-Dining"
         players.append(Player2)
      elif i == 3:
         name = raw_input("Please Enter name for player 3: ")
         Player3 = Player(name)
         Player3.position = "Ballroom-Kitchen"
         players.append(Player3)
      elif i == 4:
         name = raw_input("Please Enter name for player 4: ")
         Player4 = Player(name)
         Player4.position = "Conservatory-Ball"
         players.append(Player4)
      elif i == 5:
         name = raw_input("Please Enter name for player 5: ")
         Player5 = Player(name)
         Player5.position = "Library-Conservatory"
         players.append(Player5)
      else:
         name = raw_input("Please Enter name for player 6: ")
         Player6 = Player(name)
         Player6.position = "Study-Library"
         players.append(Player6)
   
   current_game.initialize(players)
   #gameplay loop
   current_game.game_play()

    
if __name__ == '__main__':
    main()