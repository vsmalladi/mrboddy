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
        self.assertEquals(self.player.get_name,"Venkat")
        
    def test_get_character(self):
        """ Tests to see if player class returns Character """
        self.assertEquals(self.player.get_character,"Miss Scarlet")
    
    def test_get_position(self):
        """ Tests to see if player class returns Position """
        self.assertEquals(self.player.get_position,"Hall")
        
    def test_return_hand(self):
        """ Tests to see if player class returns hand """
        self.player.get_hand
    
    def test_reveal_card(self):
        """ Tests to see if player class can revel card from hand"""
        self.assertEquals(self.player.reveal_card("Rope"),"Rope")
    
    def test_update_position(self):
        """ Tests to see if player class can update position"""
        self.player.update_position("Ballroom")
        self.assertEquals(self.player.position,"Ballroom")

if __name__ == '__main__':
    unittest.main()
