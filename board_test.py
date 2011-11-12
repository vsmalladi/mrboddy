#! /usr/local/bin/python

import unittest
from board import Board
from player import Player

class BoardTestCase(unittest.TestCase):
    
    def setUp(self):
        """Sets up test senario"""
        self.board = Board()
        self.Player1 = Player("Player1")
        self.Player2 = Player("Player2")
        self.Player3 = Player("Player3")
        self.board.set_player_location(self.Player1,'Study')
        self.board.set_player_location(self.Player2,'Library-Conservatory')
        self.board.set_player_location(self.Player3,'Hall')

    def test_get_player_location(self):
        """Test if Board class can return the player's position"""
        self.board.get_player_location(self.Player1)
        
    def test_get_player_list(self):
        """Test if Board class can return locations of all players"""
        self.board.get_player_list
    
    def test_set_player_location(self):
        """ Test if Board class can set new location for player"""
        self.board.set_player_location(self.Player2,'Hall')
        self.board.get_player_location(self.Player2)
    
    def test_set_weapon_location(self):
        """Test if Board class can set weapon location"""
        self.board.set_weapon_location("Rope","Hall")
    
    def test_get_weapon_location(self):
        """Test if Board class can return location of a weapon"""
        self.board.set_weapon_location("Lead Pipe","Study")
        self.board.get_weapon_location("Lead Pipe")
    
    def test_get_rooms(self):
        """Test if Board class can return the list of rooms"""
        self.board.get_rooms
    
    def test_display_player_location(self):
        """Test if Board class can print the location of a player"""
        self.Player1.character = "Miss Scarlet"
        self.board.display_player_location(self.Player1)
    
    def test_display_weapon_location(self):
        """Test if Board class can print the location of a weapon"""
        self.board.display_weapon_location("Pistol")
        self.board.set_weapon_location("Pistol","Study")
        self.board.display_weapon_location("Pistol")
    
if __name__ == '__main__':
    unittest.main() 