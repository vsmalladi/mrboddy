#! /usr/local/bin/python

class Board(object):
    
    def __init__(self):
        
        self.player_locations = {}
        self.weapon_locations = {"Rope":None, "Lead Pipe":None, "Knife":None, "Wrench":None, 
                                 "CandleStick":None,"Pistol":None}
        self.rooms = ["Study", "Study-Hall", "Study-Library", "Hall", "Hall-Lounge", 
                      "Hall-Billiard", "Lounge", "Lounge-Dining", "Dining Room", "Dining-Billiard",
                      "Dining-Kitchen", "Billiard Room", "Billiard-Library", "Billiard-Ball", "Library", 
                      "Library-Conservatory", "Conservatory", "Conservatory-Ball", "Ballroom", 
                      "Ballroom-Kitchen", "Kitchen"]
        
    def get_player_location(self, player):
        
        return player.get_position
        
    
    def set_player_location(self, player, room):
        
        player.update_position(room)
        self.player_locations[player]=player.get_position
    
    @property
    def get_player_list(self):
        
        return self.player_locations    
    
                
    def get_weapon_location(self, weapon):
        
        return self.weapon_locations.get(weapon)
        
        
    def set_weapon_location(self, weapon, room):
        
        self.weapon_locations[weapon] = room
    
    
    def display_player_location(self, player):
        
        print("%s is in the %s" % (player.get_character, player.get_position))
        
    
    def display_weapon_location(self, weapon):
        
        if self.weapon_locations[weapon] != None:
            print("The %s is in the %s " % (weapon,self.get_weapon_location(weapon)))
        else:
            print("The %s is not in a room yet." % (weapon))
    
    @property
    def get_rooms(self):
        return self.rooms
    
    
    def get_board(self):        
        return self        
