#! /usr/local/bin/python

from gamerules import GameRules

class Phase(object):
    """
    A phase of the game
    """
    
    def __init__(self,game):
        self.game = game
        self.gamerules = GameRules()
    
    def enter(self):
        """
        Called when in phase
        """
        raise NotImplementedError

class MovePhase(Phase):
    """
    Player Movement Phase
    """
    
    name = "Move Phase"
    key = P_MOVE
    
    def enter(self, move_to):
        self.player = self.game.active_player
        self.move_to = move_to
        if self.gamerules.is_valid_move(self.game.game_board,self.player,self.move_to):
            player.update_position(self.move_to)
            return True
        else:
            return False
        

class MakeSuggestionPhase(Phase):
    """
    Player Makes Suggestion
    """
    
    name = "Suggestion Phase"
    key = P_SUGGEST
    
    def enter(self,suspect,weapon):
        self.player = self.game.active_player
        self.position = self.game.get_position
        self.suspect = suspect
        self.weapon = weapon
        for p in self.game.players:
            if p.get_character == self.suspect:
                self.game.game_board.set_player_location(p,self.position)

class MakeAccusation(Phase):
    """
    Player Makes Accusation
    """
    
    name = "Accusation Phase"
    key = P_ACCUSE
    
    def enter(self,suspect,room,weapon):
        player = self.game.active_player
        case = self.game.get_case
        self.suspect = suspect
        self.room = room
        self.weapn = weapon
        
        if (self.suspect == case["Suspect"]) and (self.room == case["Room"]) and (self.weapon == case["Weapon"]):
            print "You are correct. You have won"
            self.game.status = False
        else:
            player.inplay = False
            print "Your guess was incorrect"
            return "It was not %s in the %s with the %s" % (self.suspect,self.room,self.weapon)