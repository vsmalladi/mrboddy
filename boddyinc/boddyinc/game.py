#! /usr/local/bin/python

#Import statments
from random import randrange
from random import shuffle
from string import *
from player import Player
from board import Board
from gamerules import GameRules
import os
import pickle
import sys
import simplejson as json
from sqlalchemy import *

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
        self.engine = None
        self.game_ins = insert()
        self.player_ins = insert()
        self.board_ins = insert()
        self.conn = None #database connection
        
        
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
        
        try:
            ins = game_ins.values(casefile=case)
            conn.execute(ins)
        except:
            raise
        
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
    
    
    '''    
    def check_turntracker(self, player):
        
        try:
            if path.exists(self.__tracker_name):
                print("A game is already in progress. Please try again later.")
        except IOError:
            return false    
            
        return true
    ''' 
    
    '''
    def cleanup(self):
        """
        Remove tracker flatfiles at end of game
        """
        
        try:
            self.__turn_tracker.close
            remove(self.__turn_tracker)
            self.__user_tracker.close
            remove(self.__user_tracker)
            
            for c in self.__characters:
                if path.exists(c):
                    remove(c)
                    
        except IOError:
            print "Something went wrong cleaning up the game"
            return false
        
        return true
    '''
    
    '''
    def read_truntracker(self):
        """
        Get the current player
        """
        active_player = None
        
        try:
            file = open(self.__tracker_name, 'r')
            active_player = pickle.load(file)
        except IOError:
            print "Something went wrong reading the active player"
        
        return active_player
    '''
        
    def initialize(self):
        """
        Initialize game
        """
        
        engine = create_engine('sqlite:////var/www/mrboddy/boddyinc/boddyinc/database.db', pool_size=6)
        #may need to manage sessions and/or connection pools?
        
        #create list of player objects
        num_players = self.get_num_players
        players = []
        temp_chars = self.__characters
        
        for i in 0..num_players:
            p = Player()
            players.add(temp_chars.pop())
            
        self.players = players
        self.case_file = self.__create_case()
        
        #TODO: this group may need to be written to the database
        self._card_list = self.__make_card_list(self.case_file) 
        self.game_board = Board()
        self.gamerules = GameRules()
        
        self.active_player = self.players[0]
        self.__game_status = True
        
        #update DB
        conn.execute(game_ins, [player_list=players, \
                     active_player = self.active_player.get_character, \
                     game_status = self.__game_status])
        
        #TODO: update this
        check_turntracker #make sure a game isn't already in progress
            
        while len(self._card_list) > 0:
            for player in self.players:
                card = self.__get_remaining_card(self._card_list)
                player.hand[card] = card

                #add each player to DB
                try:
                    conn.execute(player_ins, [character_name=player.get_character,
                                              location=player.location,
                                              cards=player.hand,
                                              inplay=player.inplay])

                except IOError:
                    print "Something went wrong writing game information to database. \
                    Game play can't continue"
                    cleanup
                    sys.exit
                
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
        try:
            active_player_name = conn.execute("SELECT active_player FROM game")
        except:
            raise

        return active_player_name
    
    
    @property
    def get_game_state(self):
        """
        Returns the state of the game
        """
        try:
            self.__game_status = conn.execute("SELECT game_status FROM game")
        except:
            raise
        
        return self.__game_status
    
    
    def __set_active_player(self):
        """
        Set the next active player
        """
        player_inplay = False
        current_active = get_active_player
        
        for p in players:
            if p == current_active:
                self.active_player = p
        
        while player_inplay == False:    
            try:
                self.active_player = self.players[self.players.index(self.active_player) + 1]
                current_player = self.players[self.players.index(self.active_player)]
                player_inplay = current_player.inplay
                
                try:
                    status = conn.execute("UPDATE players SET players.active_player=" + self.active_player)
                except:
                    raise
                
            except IndexError:
                self.active_player = player = self.players[0]
                current_player = self.players[0]
                player_inplay = current_player.inplay
            
            # If loop through all players and no one is active
            if self.active_player.get_name == current_active:
                self.__game_status = False
                status = conn.execute("UPDATE game SET game.status=FALSE")
                
                try:
                    self.case_file = conn.execute("SELECT case_file FROM players")
                except:
                    raise
                
                print "It was %s in the %s with the %s" % (self.case_file["Suspect"],self.case_file["Room"],self.case_file["Weapon"])
                print "The game is over. Everyone guessed incorrectly"
                break
        
        
    #TODO: not updated for DB yet
    def __set_disprove_player_order(self):
        """
        Return a list of players in order for disproving a suggestion
        """
        disprove_player_list = []
        
        if self.players.index(self.active_player) == 0:
            disprove_player_list = disprove_player_list + self.players[:]
            
        else:
            disprove_player_list = disprove_player_list + self.players[self.players.index(self.active_player):]
            disprove_player_list = disprove_player_list + self.players[:self.players.index(self.active_player) - 1]
            
        return disprove_player_list
    
    
    def add_player(self, player_name):
        
        """
        This function should be called when a user decides to join the game.
        """
        try:
            conn.create
            num_players = conn.execute("SELECT num_players FROM players")
            ins = game_ins(players.num_players = num_playes + 1)
            conn.execue(ins)
        except:
            raise
        
        #TODO: update
        players.add(player_name)
        
        return true               
        
    
    def get_num_players(self):
        
        try:
            self.__num_players = conn.execute("SELECT num_players FROM game")                    
        except:
            raise
        
        return self.__num_players
    
    
    #TODO: update for DB
    def make_move(self,move_to):
        """
        Movement of player 
        """
        if self.gamerules.is_valid_move(self.game_board,self.active_player,move_to):
            self.game_board.set_player_location(self.active_player, move_to)
            print "%s has moved to %s" % (self.active_player.get_name,move_to)
            return True
        else:
            print "That is not a valid move."
            return False


    #TODO: update for DB
    def make_suggestion(self,suspect,weapon):
        """
        Player makes a suggestion
        """
        self.suggest_room = self.active_player.get_position
        self.suggest_suspect = suspect
        self.suggest_weapon = weapon
        
        #Move player's character to new room
        for p in self.players:
            if p.get_character == suspect:
                self.game_board.set_player_location(p,self.suggest_room)
                print "%s (%s) is now at %s" % (p.get_name,p.get_character,p.get_position)
        
        print ("%s thinks it was %s in the %s with a %s." %\
               (self.active_player.get_name, self.suggest_suspect, self.suggest_room,self.suggest_weapon))
        
    
    #TODO: update for DB
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
    
    #TODO: update for DB
    def available_cards_disprove(self,player):
        """
        Returns a dict of cards available from a player to
        disprove a suggestion
        """
        can_disprove = {}
        if self.suggest_room in player.get_hand.values():
            can_disprove[self.suggest_room] = self.suggest_room
        
        if self.suggest_suspect in player.get_hand.values():
            can_disprove[self.suggest_suspect] = self.suggest_suspect
        
        if self.suggest_weapon in player.get_hand.values():
            can_disprove[self.suggest_weapon] = self.suggest_weapon
            
        return can_disprove
        
        
    #TODO: update for DB    
    def disprove_suggestion(self,player,card):
        #I think this will need to be implemented once the interaction
        #once there is a way to interace with the UI
        """
        Player can disprove another's suggestion
        """
        print ("Player %s disproved suggestion by revealing %s." %\
               (player.get_name, player.reveal_card(card)))
        
        return True
    
    #TODO: update for DB  
    def make_accusation(self,room,suspect,weapon):
        """
        Player makes accusation
        """
        if (suspect == self.case_file["Suspect"]) and (room == self.case_file["Room"]) and (weapon == self.case_file["Weapon"]):
            print "You are correct. You have won"
            self.__game_status = False
        else:
            self.active_player.inplay = False
            print "Your guess was incorrect"
            print "It was not %s in the %s with the %s" % (suspect,room,weapon)
    
    #TODO: update for DB?
    def game_play(self):
        """
        This is the main game loop that would be
        called by playgame moduel
        """
        while self.__game_status == True:
            print "It is %s turn." % (self.active_player.get_name)
            print "=== Menu ==="
            print "1. Make Movement"
            print "2. Make Suggestion"
            print "3. Make Accusation"
            print "4. End Turn"
            
            user_choice = raw_input("Choose an option from the menu: ")
    
            if user_choice == "1":
                new_room = raw_input("Enter the name of the room you will move to: ")
                self.make_move(new_room)
            
            elif user_choice == "2":
                suspect = raw_input("Enter a suspect: ")
                weapon = raw_input("Enter a weapon: ")
                self.make_suggestion(suspect,weapon)
                
                disprove_player_list = self.__set_disprove_player_order()

                for disprove_player in reversed(disprove_player_list):
                    print disprove_player.get_name
    
                    if disprove_player == self.active_player:
                            print "No one can disprove the suggestion"
                            break
                    else:
                        if self.check_disprove_suggestion(disprove_player) == True:
                            print self.available_cards_disprove(disprove_player)
                            card_choosen = raw_input("Enter card to disprove: ")
                            self.disprove_suggestion(disprove_player,card_choosen)
                            break
 
            elif user_choice == "3":
                suspect = raw_input("Enter a suspect: ")
                weapon = raw_input("Enter a weapon: ")
                room = raw_input("Enter a room: ")
                self.make_accusation(room,suspect,weapon)
                self.__set_active_player()
                
            elif user_choice == "4":
                self.__set_active_player()
    
    '''
    def encode_num_players(self):
        num_players = json.dumps(self.get_num_players)
        
        return num_players
    
    
    def encode_player_info(self):
        
        temp_player_list = []
        
        for p in self.__characters:
            try:
                if path.exists(p):
                    file = open(p, 'r')
                    temp_player = pickle.load(file)
                    temp_player_list.append(json.dumps(temp_player))
            except:
                print "Something went wrong reading file"
                   
        return temp_player_list
    '''