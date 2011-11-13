#! /usr/local/bin/python

#Import statments
from random import randrange
from random import shuffle
from string import *
from player import Player
from board import Board
from gamerules import GameRules

class Game(object):
    
    
    def __init__(self):
        self.case_file = {}
        self.active_player = None
        self.game_status = True
        self.players = []
        self.character_dict = {0 :"Colonel Mustard", 1:"Miss Scarlet", 2:"Prof. Plum", 3:"Mr. Green", 4:"Mrs. White", 5:"Mrs. Peacock"}
        self.weapon_dict = {0 :"Rope", 1:"Lead Pipe", 2:"Knife", 3:"Wrench", 4:"Candlestick", 5:"Pistol"}
        self.room_dict = {0 :"Hall", 1:"Lounge", 2:"Dining Room", 3:"Kitchen", 4:"Ballroom", 5:"Conservatory", 6:"Billiard Room", 7:"Library", 8:"Study"}
        self.characters = ["Miss Scarlet","Colonel Mustard","Mrs. White","Mr. Green","Mrs. Peacock","Prof. Plum"]
        self.suspect = None
        self.room = None
        self.weapon = None
        self.num_players = 0
    
    def get_card(self,card_dict):
        """
        Returns a random card from the card dictionary
        """
        card = card_dict[randrange(0,len(card_dict))]
        return card
    
    
    def create_case(self):
        """
        Returns case dictionary including the suspect, weapon, and room
        """
        case = {}
        case['Suspect'] = self.get_card(self.character_dict)
        case['Weapon'] = self.get_card(self.weapon_dict)
        case['Room'] = self.get_card(self.room_dict)
        return case
    
    
    def make_card_list(self,case):
        """
        Returns suffled list of cards not in case file
        """
        cards = []
        for value in self.character_dict.values():
            if value != case['Suspect']:
                cards.append(value)
        
        for value in self.weapon_dict.values():
            if value != case['Weapon']:
                cards.append(value)  
        
        for value in self.room_dict.values():
            if value != case['Room']:
                cards.append(value)
                
        shuffle(cards)
        return cards
    
    
    def get_remaining_card(self,card_list):
        """
        Returns a random card from the remaing card list and removes
        it from the list
        """
        card = card_list.pop(randrange(0,len(card_list)))
        return card
    
    def initialize(self,players):
        """
        Initializes game
        """
        self.players = players
        self.case_file = self.create_case()
        self._card_list = self.make_card_list(self.case_file)
        self.game_board = Board()
        self.gamerules = GameRules()
        self.active_player = self.players[0]
        
        for player in self.players:
            player.character = self.get_remaining_card(self.characters)
            
        while len(self._card_list) > 0:
            for player in self.players:
                card = self.get_remaining_card(self._card_list)
                player.hand[card] = card

    
    @property
    def get_case(self):
        """
        Returns the case file
        """
        return self.case_file
    
    @property
    def get_active_player(self):
        """
        Returns the active player
        """
        return self.active_player.get_name
    
    @property
    def get_game_state(self):
        """
        Returns the state of the game
        """
        return self.game_status
    
    def set_active_player(self):
        """
        Set the next active player
        """
        player_inplay = False
        while player_inplay == False:    
            try:
                self.active_player = self.players[self.players.index(self.active_player) + 1]
                current_player = self.players[self.players.index(self.active_player) + 1]
                player_inplay = current_player.inplay
            except IndexError:
                self.active_player = player = self.players[0]
                current_player = self.players[0]
                player_inplay = current_player.inplay
    
    def add_player(self, incr_player):
        self.num_players += 1
    
    def get_num_players(self):
        return self.num_players
    
    def get_board(self):
        """
        Return the state of the game board
        """
        return self.game_board
    
    def make_move(self,move_to):
        """
        Movement of player
        """
        if self.gamerules.is_valid_move(self.game_board,self.active_player,move_to):
            self.active_player.update_position(move_to)
            return True
        else:
            return False

    
    def make_suggestion(self,suspect,weapon):
        """
        Player makes suggestion
        """ 
        pass
    
    def make_accusation(self,room,suspect,weapon):
        """
        Player makes accusation
        """
        if (suspect == case["Suspect"]) and (room == case["Room"]) and (weapon == case["Weapon"]):
            print "You are correct. You have won"
            self.game_status = False
        else:
            self.active_player.inplay = False
            print "Your guess was incorrect"
            return "It was not %s in the %s with the %s" % (suspect,room,weapon)
    