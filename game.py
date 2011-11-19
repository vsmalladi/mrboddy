#! /usr/local/bin/python

#Import statments
from random import randrange
from random import shuffle
from string import *
from player import Player
from board import Board
from gamerules import GameRules
import os

class Game(object):
    
    
    def __init__(self):
        self.case_file = {}
        self.active_player = None
        self.__game_status = False
        self.players = []
        self.__character_dict = {0 :"Colonel Mustard", 1:"Miss Scarlet", 2:"Prof. Plum", 3:"Mr. Green", 4:"Mrs. White", 5:"Mrs. Peacock"}
        self.__weapon_dict = {0 :"Rope", 1:"Lead Pipe", 2:"Knife", 3:"Wrench", 4:"Candlestick", 5:"Pistol"}
        self.__room_dict = {0 :"Hall", 1:"Lounge", 2:"Dining Room", 3:"Kitchen", 4:"Ballroom", 5:"Conservatory", 6:"Billiard Room", 7:"Library", 8:"Study"}
        self.__characters = ["Miss Scarlet","Colonel Mustard","Mrs. White","Mr. Green","Mrs. Peacock","Prof. Plum"]
        self.suggest_suspect = None
        self.suggest_room = None
        self.suggest_weapon = None
        self.__num_players = 0
        self.__turn_tracker = None #flatfile to track turns in place of a database
        self.__tracker_name = "turn"
        self.game_board = None
        self.user_tracker = None #flatfile to track number of users playing
        self.user_tracker_name = "users"
        self.gamerules = None
    
    def __get_card(self,card_dict):
        """
        Returns a random card from the card dictionary
        """
        card = card_dict[randrange(0,len(card_dict))]
        return card
    
    
    def __create_case(self):
        """
        Returns case dictionary including the suspect, weapon, and room
        """
        case = {}
        case['Suspect'] = self.__get_card(self.__character_dict)
        case['Weapon'] = self.__get_card(self.__weapon_dict)
        case['Room'] = self.__get_card(self.__room_dict)
        return case
    
    
    def __make_card_list(self,case):
        """
        Returns suffled list of cards not in case file
        """
        cards = []
        for value in self.__character_dict.values():
            if value != case['Suspect']:
                cards.append(value)
        
        for value in self.__weapon_dict.values():
            if value != case['Weapon']:
                cards.append(value)  
        
        for value in self.__room_dict.values():
            if value != case['Room']:
                cards.append(value)
                
        shuffle(cards)
        return cards
    
    
    def __get_remaining_card(self,card_list):
        """
        Returns a random card from the remaing card list and removes
        it from the list
        """
        card = card_list.pop(randrange(0,len(card_list)))
        return card
    
    
    def update_turntracker(self, player):
        """
        Updates a flatfile to use to track whose turn it is
        
        May need to update this to incorporate authentication (pyramid_who)
        """
        try:
            self.__turn_tracker = open(self.tracker_name, 'w')
            self.__turn_tracker.write(player.character)
            self.__turn_tracker.close()
        except IOError:
            return false
        
        return true
    
        
    def create_turntracker(self, player):
        
        try:
            if path.exists(self.tracker_name):
                print("A game is already in progress. Please try again later.")
        except IOError:
            return false    
            
        return true
       
    
    def cleanup(self):
        """
        Remove turn and user trackers at end of game
        """
        
        try:
            self.__turn_tracker.close
            remove(self.__turn_tracker)
            self.__user_tracker.close
            remove(self.__user_tracker)
        except IOError:
            print "Something went wrong cleaning up the game"
            return false
        
        return true
    
    
    def read_truntracker(self):
        """
        Get the current player
        """
        
        pass
    
        
    def initialize(self,players):
        """
        Initializes game
        """
        self.players = players
        self.case_file = self.__create_case()
        self._card_list = self.__make_card_list(self.case_file)
        self.game_board = Board()
        self.gamerules = GameRules()
        self.active_player = self.players[0]
        
        for player in self.players:
            player.character = self.__get_remaining_card(self.__characters)
            
        while len(self._card_list) > 0:
            for player in self.players:
                card = self.__get_remaining_card(self._card_list)
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
        return self.__game_status
    
    
    def __set_active_player(self):
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
    
        #update turn tracker
        if not (update_turntracker(self.active_player.character)):
            print("Error") #need to decide what to do here
        
        
    def add_player(self, player_name):
        
        """
        This function should be called when a user decides to join the game.
        """
        if not path.exists(self.tracker_name):
            try:
                self.__user_tracker = open(self.__user_tracker_name, 'r+')
                
            except IOError:
                return false
        
        try:
            np = self.__user_tracker.readline
            if np != "":
                self.__num_players = np + 1
            else:
                np = 1
                    
            self.__user_tracker.write(self.__num_players)
        
        except IOError:
            return false
        
        players.add(player_name)
        
        return true               
        
    
    def get_num_players(self):
        
        try:
            self.__num_players = self.__user_tracker.readline
        
        except IOError:
            return None
        
        return self.__num_players
    
    
    def make_move(self,move_to):
        """
        Movement of player 
        """
        if self.gamerules.is_valid_move(self.game_board,self.active_player,move_to):
            self.game_board.set_player_location(self.active_player, move_to)
            return True
        else:
            return False

    
    def make_suggestion(self,suspect,weapon):
        """
        Player makes a suggestion
        """
        self.suggest_room = self.active_player.get_position
        self.suggest_suspect = suspect
        self.suggest_weapon = weapon
        
        print ("Player %s thinks it was %s in the %s with a %s." %\
               (self.active_player.get_name, self.suggest_suspect, self.suggest_room,self.suggest_weapon))
        
    
    def check_disprove_suggestion(self,player):
        """
        Checks if a player can disprove a suggestion
        """
        if self.suggest_room in player.get_hand.values():
            return True
        elif self.suggest_suspect in player.get_hand.values():
            return True
        elif self.suggest_weapon in player.get_hand.values():
            return True
        else:
            return False
        
        
    def disprove_suggestion(self,player,):
        #I think this will need to be implemented once the interaction
        #once there is a way to interace with the UI
        """
        Player can disprove another's suggestion
        """
        
        pass
                
    
    def make_accusation(self,room,suspect,weapon):
        """
        Player makes accusation
        """
        if (suspect == case["Suspect"]) and (room == case["Room"]) and (weapon == case["Weapon"]):
            print "You are correct. You have won"
            self.__game_status = False
        else:
            self.active_player.inplay = False
            print "Your guess was incorrect"
            return "It was not %s in the %s with the %s" % (suspect,room,weapon)
    