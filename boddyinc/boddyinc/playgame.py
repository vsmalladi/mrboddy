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
   while True:
      num_players = int(raw_input("Enter the number of players (3-6): "))
      if num_players >=3:
         break
      else:
         print "Please enter a number between 3-6"

   
   for i in range(1,num_players):
      player_name = raw_input("Enter the name for Player %s " % (i))
      current_game.add_player(player_name)
   
   current_game.initialize()
   #gameplay loop
   current_game.game_play()
    
if __name__ == '__main__':
    main()