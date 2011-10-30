#! /usr/local/bin/python

import player

class Board(object):
    	
    rooms = {0 :"Study", 1:"Study-Hall", 2:"Study-Library", 3:"Hall", 4:"Hall-Lounge", 5:"Hall-Billiard", 6:"Lounge", 7:"Lounge-Dining", 8:"Dining Room", 9:"Dining-Billiard",10:"Dining-Kitchen", 11:"Billiard Room", 12:"Billiard-Library", 13:"Billiard-Ball", 14:"Library", 15:"Library-Conservatory", 16:"Conservatory", 17:"Conservatory-Ball", 18:"Ballroom", 19:"Ballroom-Kitchen", 20:"Kitchen"}

    def __init__(self):
        
    	self.player_locations = None
	self.weapon_locations = None

    def get_player_location(self, player):
        """
        Returns the player's location on the board
        """
        
    
    def set_player_location(self, player, room):
        """
        Moves a player to a room based on another player's suggestion
        """
        
    def get_weapon_location(self, weapon):
        """
        Returns the location of a weapon
        """
        

    def set_weapon_location(self, weapon, room):
        """
        Moves a weapon to the given room
        """
        
    
    def displayPlayerLocation(self, player):
        """
        Prints out the location of a given player
        """
        
    
    def display_weapon_location(self, weapon):
        """
        Prints out the location of a given weapon
        """
   
