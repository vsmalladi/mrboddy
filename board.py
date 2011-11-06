#! /usr/local/bin/python

class Board(object):
    
    def __init__(self):
        
        self.player_locations = {"Study":None, "Study-Hall":None, "Study-Library":None, "Hall":None, 
                                 "Hall-Lounge":None, "Hall-Billiard":None, "Lounge":None, 
                                 "Lounge-Dining":None, "Dining Room":None, "Dining-Billiard":None,
                                 "Dining-Kitchen":None, "Billiard Room":None, "Billiard-Library":None, 
                                 "Billiard-Ball":None, "Library":None, "Library-Conservatory":None, 
                                 "Conservatory":None, "Conservatory-Ball":None, "Ballroom":None,
                                 "Ballroom-Kitchen":None, "Kitchen":None}
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
        
        #update the player location list
        for rm, pl in self.player_locations:
            if pl == player:
                self.player_locations[rm].remove(pl)
                
        self.player_locations[room].append(player)
    
    
    def get_player_list(self):
        
        return self.player_locations    
    
                
    def get_weapon_location(self, weapon):
        
        return self.weapon_locations.get(weapon)
        
        
    def set_weapon_location(self, weapon, room):
        
        self.weapon_locations[weapon] = room
    
    
    def display_player_location(self, player):
        
        print(player.get_character() & " is in the " & player.get_position())
        
    
    def display_weapon_location(self, weapon):
        
        if self.weapon_locations[weapon].value() != None:
            print("The " & weapon & " is in the " & self.get_weapon_location(weapon))
        else:
            print("The " & weapon & " is not in a room yet.")
            
    def get_rooms(self):
        return self.rooms
            
            
