#! /usr/local/bin/python

import unittest
from player import Player
from board import Board
from gamerules import GameRules

class GameRulesTestCase(unittest.TestCase):
    
    def setUp(self):
        """Sets up test senario"""
        self.gamerules = GameRules()
        self.board = Board()
        self.gamerules.rooms = self.board.get_rooms
        self.gamerules.player_list = self.board.get_player_list
        self.Player1 = Player("Player1")
        self.Player2 = Player("Player2")
        self.Player3 = Player("Player3")
        self.board.set_player_location(self.Player1,'Study')
        self.board.set_player_location(self.Player2,'Study-Hall')
        self.board.set_player_location(self.Player3,'Hall')
    
    def test_is_adjacent_to(self):
        """ Test if a room is adjacent to another room"""
        self.assertFalse(self.gamerules.is_adjacent_to("Library","Hall")) #Not adjacent
        self.assertTrue(self.gamerules.is_adjacent_to("Study","Study-Hall")) #Adjacent
    
    def test_has_secret_passage(self):
        """ Test if a room has a secret passage"""
        self.assertTrue(self.gamerules.has_secret_passage("Conservatory")) #Has Passage
        self.assertFalse(self.gamerules.has_secret_passage("Ballroom")) #Doesn't Have passage
     
    def test_is_hallway(self):
        """ Test if a room is a hallway"""
        self.assertFalse(self.gamerules.is_hallway("Dinning Room")) #Not hallway
        self.assertTrue(self.gamerules.is_hallway("Hall-Lounge")) #Is a hallway

    def test_is_empty_room(self):
        """ Test if a room is empty."""
        self.assertTrue(self.gamerules.is_empty_room("Dining")) # Room can be occupided by more than 1 person
        self.assertTrue(self.gamerules.is_empty_room("Study-Library")) #Empty Hallway, is empty
        self.assertFalse(self.gamerules.is_empty_room("Study-Hall")) #Occupied Hallway
    
    def test_is_valid_move(self):
        """ Test if a player's move is valid."""
        self.assertTrue(self.gamerules.is_valid_move(self.board,self.Player1,"Kitchen")) #valid move
        self.assertFalse(self.gamerules.is_valid_move(self.board,self.Player1,"Study-Hall")) #Not valid move
   


if __name__ == '__main__':
    unittest.main() 