#! /usr/local/bin/python

import unittest
from player import Player

class PlayerTestCase(unittest.TestCase):
    
    def setUp(self):
        """ Sets up test senario """
        self.player = Player()
        self.player.character = "Miss Scarlet"
        self.player.position = "Hall"
        self.player.hand = {"Rope":"Rope","Knife":"Knife","Kitchen":"Kitchen","Ballroom":"Ballroom"}
        self.case_file = {"Suspect":"Prof. Plum","Weapon":"Rope","Room":"Hall"}
        
    def test_return_character(self):
        """ Tests to see if player class returns Character """
        self.player.character
    
    def test_return_position(self):
        """ Tests to see if player class returns Position """
        self.player.position
        
    def test_return_hand(self):
        """ Tests to see if player class returns hand """
        self.player.hand
    
    def test_reveal_card(self):
        """ Tests to see if player class can revel card from hand"""
        self.player.reveal_card("Rope")
    
    def test_update_position(self):
        """ Tests to see if player class can update position"""
        self.player.update_position("Ballroom")
        self.player.position
        
    def test_accusation(self):
        """ Tests to see if player class can make accusation """
        negative_guess = self.player.make_accusation("Mr.Green","Hall","Rope",self.case_file)
        positive_guess = self.player.make_accusation("Prof. Plum","Hall","Rope",self.case_file)

if __name__ == '__main__':
    unittest.main()
