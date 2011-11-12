#! /usr/local/bin/python

import unittest
from player import Player

class PlayerTestCase(unittest.TestCase):
    
    def setUp(self):
        """ Sets up test senario """
        self.player = Player("Venkat")
        self.player.character = "Miss Scarlet"
        self.player.position = "Hall"
        self.player.hand = {"Rope":"Rope","Knife":"Knife","Kitchen":"Kitchen","Ballroom":"Ballroom"}
    
    def test_get_name(self):
        """ Tests to see if player class resutns Name """
        self.player.get_name
        
    def test_get_character(self):
        """ Tests to see if player class returns Character """
        self.player.get_character
    
    def test_get_position(self):
        """ Tests to see if player class returns Position """
        self.player.get_position
        
    def test_return_hand(self):
        """ Tests to see if player class returns hand """
        self.player.get_hand
    
    def test_reveal_card(self):
        """ Tests to see if player class can revel card from hand"""
        self.player.reveal_card("Rope")
    
    def test_update_position(self):
        """ Tests to see if player class can update position"""
        self.player.update_position("Ballroom")
        self.player.position

if __name__ == '__main__':
    unittest.main()
