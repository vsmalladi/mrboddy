#! /usr/local/bin/python

#Import statments

class GameRules(object):
   
        def __init__(self):
            self.rooms = []
            self.player_list = {}
 
        def is_valid_move(self, board, player, room_to):
            
            room_from = board.get_player_location(player)
            self.rooms = board.get_rooms
            self.player_list = board.get_player_list;
            
            #if the room is empty and doesn't have someone in it, the move is valid
            if self.is_adjacent_to(room_to, room_from) and  self.is_empty_room(room_to, conn):
                return True
            else:
                return False
                
            
        def is_adjacent_to(self, room_to, room_from):
            
            #from study to study-hall, study-library, or kitchen
            if room_from == self.rooms[0]:
                if room_to == self.rooms[1] or room_to == self.rooms[2] or room_to == self.rooms[3] or room_to == self.rooms[20]:
                    return True
            
            #from study-hall to study or hall
            elif room_from == self.rooms[1]:
                if room_to == self.rooms[3] or room_to == self.rooms[0]:
                    return True
            
            #from hall to study-hall, hall-lounge, or hall-billiard    
            elif room_from == self.rooms[3]:
                if room_to == self.rooms[1] or room_to == self.rooms[4] or room_to == self.rooms[5]:
                    return True
            
            #from hall-lounge to hall or lounge
            elif room_from == self.rooms[4]:
                if room_to == self.rooms[3] or room_to == self.rooms[6]:
                    return True
            
            #from hall-billiard to hall or billiard
            elif room_from == self.rooms[5]:
                if room_to == self.rooms[3] or room_to == self.rooms[11]:
                    return True
                
            #from lounge to hall-lounge, lounge-dining, or conservatory
            elif room_from == self.rooms[6]:
                if room_to == self.rooms[7] or room_to == self.rooms[4] or room_to == self.rooms[16]:
                    return True
            
            #from lounge-dining to lounge or dining room
            elif room_from == self.rooms[7]:
                if room_to == self.rooms[6] or room_to == self.rooms[8]:
                    return True
                
            #from dining room to lounge-dining, dining-billiard, or dining-kitchen
            elif room_from == self.rooms[8]:
                if room_to == self.rooms[7] or room_to == self.rooms[9] or room_to == self.rooms[20]:
                    return True
            
            #from dining-billiard to billiard room or dining room
            elif room_from == self.rooms[9]:
                if room_to == self.rooms[11] or room_to == self.rooms[8]:
                    return True
            
            #from dining-kitchen to dining room or kitchen
            elif room_from == self.rooms[10]:
                if room_to == self.rooms[8] or room_to == self.rooms[20]:
                    return True
                
            #from billiard room to hall-billiard, billiard-library, dining-billiard, or billiard-ball
            elif room_from == self.rooms[11]:
                if room_to == self.rooms[5] or room_to == self.rooms[9] \
                or room_to == self.rooms[12] or room_to == self.rooms[13]:
                    return True 
            
            #from billiard-library to library or billiard room
            elif room_from == self.rooms[12]:
                if room_to == self.rooms[14] or room_to == self.rooms[11]:
                    return True
            
            #from billiard-ball to billiard or ballroom
            elif room_from == self.rooms[13]:
                if room_to == self.rooms[11] or room_to == self.rooms[18]:
                    return True
                
            #from library to study-library or library-conservatory
            elif room_from == self.rooms[14]:
                if room_to == self.rooms[2] or room_to == self.rooms[15]:
                    return True
            
            #from library-conservatory to library or conservatory
            elif room_from == self.rooms[15]:
                if room_to == self.rooms[14] or room_to == self.rooms[16]:
                    return True
            
            #from conservatory to library-conservatory, conservatory-ball, or lounge
            elif room_from == self.rooms[16]:
                if room_to == self.rooms[15] or room_to == self.rooms[17] or room_to == self.rooms[6]:
                    return True
                
            #from conservatory-ball to conservatory or ballroom
            elif room_from == self.rooms[17]:
                if room_to == self.rooms[16] or room_to ==self.rooms[18]:
                    return True
            
            #from ballroom to conservatory-ball, billiard-ball, or ball-kitchen
            elif room_from == self.rooms[18]:
                if room_to == self.rooms[17] or room_to == self.rooms[19] or room_to == self.rooms[13]:
                    return True
            
            #from ball-kitchen to ballroom or kitchen
            elif room_from == self.rooms[19]:
                if room_to == self.rooms[18] or room_to == self.rooms[20]:
                    return True
            
            #from kitchen to ball-kitchen, dining-kitchen, or study
            elif room_from == self.rooms[20]:
                if room_to == self.rooms[19] or room_to == self.rooms[10] or room_to == self.rooms[0]:
                    return True
            
            else:
                return False
                
                
        def has_secret_passage(self, room):
            
            if room == self.rooms[0] \
            or room == self.rooms[6] \
            or room == self.rooms[16] \
            or room == self.rooms[20]:
                return True
            
            else:
                return False
        
        
        def is_hallway(self, room):
            
            if room == self.rooms[1] \
            or room == self.rooms[4] \
            or room == self.rooms[2] \
            or room == self.rooms[5] \
            or room == self.rooms[7] \
            or room == self.rooms[15] \
            or room == self.rooms[13] \
            or room == self.rooms[10] \
            or room == self.rooms[17] \
            or room == self.rooms[18] \
            or room == self.rooms[19]:
                return True
            
            else:
                return False
            
            
        def is_empty_room(self, room_to):
            
            empty = True
            
            #if the room to be moved to is not a hallway, then
            #it's ok to move there even if it's already occupied
            if self.is_hallway(room_to) == False:
                return empty
            
            else:
                if room_to in self.player_list.values():
                        empty = False
                        
            return empty