#! /usr/local/bin/python

class Player(object):
    
    def __init__(self,name):
        self.character = None
        self.position = "Start"
        self.inplay = True
        self.hand = {}
        self.name = name
    
    @property
    def get_name(self):
        """
        Returns the player's name
        """
        return self.name

    @property
    def get_character(self):
        """
        Returns the player's character
        """
        return self.character
    
    @property
    def get_position(self):
        """
        Returns the player's position
        """
        return self.position
    
    def update_position(self,new_position):
        """
        Updates the player's position
        """
        self.position = new_position
    

    @property
    def get_hand(self):
        """
        Returns the cards in the player's hand
        """
        return self.hand
    
    def make_accusation(self,suspect,room,weapon,case):
        """
        Checks if accusation is within case file
        """
        if (suspect == case["Suspect"]) and (room == case["Room"]) and (weapon == case["Weapon"]):
            print "You are correct. You have won"
            return True #Should most likley make a game object that will change the game variable instead of this method
        else:
            self.inplay = False
            print "Your guess was incorrect"
            return "It was not %s in the %s with the %s" % (suspect,room,weapon)
    
    @property
    def get_player_status(self):
        """
        Returns if the player is still in play and hasn't made an incorrect accusation
        """
        return self.inplay
    
    def make_suggestion(self,suspect,case):
        """
        User makes a suggestion that others can disprove
        """
        pass
    
    def reveal_card(self,card_name):
        """
        Player reveals a particular card to disprove some suggestion
        """
        return self.hand[card_name]
        
        
