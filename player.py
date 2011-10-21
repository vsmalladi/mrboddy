#! /usr/local/bin/python

class Player(object):
    
    def __init__(self):
        self.character = None
        self.position = 'Start'
        self.inplay = True
        self.hand = {}
    
    def return_character(self):
        """
        Returns the players character
        """
        return self.character
    
    def return_position(self):
        """
        Returns the players position
        """
        return self.position
    
    def update_position(self,new_position):
        """
        Updates the players position
        """
        self.position = new_position
    
    def return_hand(self):
        """
        Returns the cards in the players hand
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
            print "You're guess was incorrect"
            return "It was not %s in the %s with the %s" % (suspect,room,weapon)
    
    def make_suggestion(self,suspect,case):
        """
        User makes a suggestion that other's can disprove
        """
        pass
    
    def reveal_card(self,card_name):
        """
        Player reveals a particular card to disprove some's suggestion
        """
        return self.hand[card_name]
        
        