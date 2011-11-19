#! /usr/local/bin/python

import unittest
from player import Player
from game import Game
from board import Board
from gamerules import GameRules

class GameTestCase(unittest.TestCase):
    
    def setUp(self):
        """Sets up test senario"""
        self.game = Game()
        Player1 = Player("Player1")
        Player2 = Player("Player2")
        Player3 = Player("Player3")
        self.players = [Player1,Player2,Player3]
        
    def test_get_card(self):
        """ Tests to return radom card from dictionary """
        dict = {0 :"Rope", 1:"Lead Pipe", 2:"Knife", 3:"Wrench", 4:"Candlestick", 5:"Pistol"}
        self.game.get_card(dict)
    
    def test_get_case(self):
        """ Tests to see if case file can be made"""
        self.game.create_case()
    
    def test_make_card_list(self):
        """ Tests to see if list of cards not in case file can be made """
        case = self.game.create_case()
        self.game.make_card_list(case)
    
    def test_get_remaning_card(self):
        """ Tests to see if the function to get a card from the list of eligible cards"""
        case = self.game.create_case()
        card_list = self.game.make_card_list(case)
        self.game.get_remaining_card(card_list)
    
    def test_game_initialization(self):
        """ Tests game initialization """
        self.game.initialize(self.players)
        

    def test_get_case(self):
        """ Tests that case file can be returned """
        self.game.get_case
    
    def test_get_active_player(self):
        """ Test that the active player can be returned"""
        self.game.initialize(self.players)
        self.game.get_active_player
    
    def test_return_game_state(self):
        """ Tests that the game state can be returned"""
        self.game.get_game_state
    
    def test_set_active_player(self):
        """ Tests that the game can move to the next player """
        self.game.initialize(self.players)
        self.game.set_active_player()
        self.game.get_active_player
    
    def test_make_move(self):
        """ Test that a player can move to a new location """
        self.game.initialize(self.players)
        self.game.active_player.position = "Hall"
        self.game.make_move("Study-Hall")
        self.assertEquals(self.game.active_player.get_position,"Study-Hall")
    
    def test_make_suggestion(self):
        """ Test that a player can make a suggestion """
        self.game.initialize(self.players)
        self.game.active_player.position = "Hall"
        self.game.make_suggestion("Mr. Green","Rope")
    
    def test_check_disprove_suggestion(self):
        """ Test that if a player makes a suggestion, method can check if they can disprove it."""
        self.game.initialize(self.players)
        self.game.active_player.position = "Hall"
        self.game.make_suggestion("Mr. Green","Rope")
        
        # Checks that if player doesn't have card returns false
        self.game.active_player.hand = {"Knife":"Knife"}
        self.assertFalse(self.game.check_disprove_suggestion(self.game.active_player)) 
        
        # Checks that if player does have weapon card
        self.game.active_player.hand = {"Rope":"Rope"}
        self.assertTrue(self.game.check_disprove_suggestion(self.game.active_player))
        
        # Checks that if player does have suspect card
        self.game.active_player.hand = {"Mr. Green":"Mr. Green"}
        self.assertTrue(self.game.check_disprove_suggestion(self.game.active_player))
        
        # Checks that if player does have a room card
        self.game.active_player.hand = {"Hall":"Hall"}
        self.assertTrue(self.game.check_disprove_suggestion(self.game.active_player))
    
    def test_available_cards_disprove(self):
        """ Test that method can return set of cards available in hand that can be used to disprove suggestion"""
        self.game.initialize(self.players)
        self.game.active_player.position = "Hall"
        self.game.make_suggestion("Mr. Green","Rope")
        self.game.active_player.hand = {"Hall":"Hall","Rope":"Rope","Colonel Mustard":"Colonel Mustard","Lead Pipe":"Lead Pipe"}
        print self.game.available_cards_disprove(self.game.active_player)
    
    def test_make_accusation(self):
        """ Test that if a player makes an accusation """
        self.game.initialize(self.players)
        self.game.case_file = {"Suspect":"Mrs. White","Weapon":"Lead Pipe","Room":"Lounge"}
        
        #Check that if player is incorrect player's status is set to False
        self.game.make_accusation("Hall","Colonel Mustard","Lead Pipe")
        self.assertFalse(self.game.active_player.get_player_status)
        
        #Check that a player can accuratley set the status of 
        self.game.make_accusation("Lounge","Mrs. White","Lead Pipe")
 

if __name__ == '__main__':
    unittest.main()