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
    
    
    @property
    def get_player_status(self):
        """
        Returns if the player is still in play and hasn't made an incorrect accusation
        """
        return self.inplay
    
    
    def reveal_card(self,card_name):
        """
        Player reveals a particular card to disprove some suggestion
        """
        return self.hand[card_name]
        
        
