#! /usr/local/bin/python

class Player(object):
    
    def __init__(self):
        self.character = None
        self.position = 'Start'
        self.inplay = True
        self.hand = {}
    
    def get_character(self):
        """
        Returns the player's character
        """
        return self.character
    
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
    
    def get_hand(self):
        """
        Returns the cards in the player's hand
        """
        return self.hand
    
    def move(self):
        """
        Function that allows player to move
        """
        pass
    
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
        
        
