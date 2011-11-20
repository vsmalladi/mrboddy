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
   #get the number of players and set up characters
   Player1 = Player("Player1")
   Player2 = Player("Player2")
   Player3 = Player("Player3")
   Player1.position = "Hall-Lounge"
   Player2.position = "Lounge-Dining"
   Player3.position = "Ballroom-Kitchen"
   players = [Player1,Player2,Player3]
   current_game.initialize(players)
   #gameplay loop
   current_game.game_play()
    
if __name__ == '__main__':
    main()