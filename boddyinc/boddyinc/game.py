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
        self.game_ins = game.insert()
        self.player_ins = players.insert()
        self.board_ins = board.insert()
        self.conn = None #database connection
        self.game_board = None
        self.metadata = None
        
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
            self.conn.execute(ins)
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
    
       
    def check_game_status(self):
        
        try:
            s = game.select(game_status)
            
            if self.conn.execute(s):
                print("A game is already in progress. Please try again later.")
                return true
        except:
            raise   
            
        return false
     
    
    def cleanup(self):
        """
        Remove game info from database
        """
        
        try:
            d = self.conn.begin()

            for table in reversed(meta.sorted_tables):
                print table.delete()
                self.conn.execute(table.delete())

            d.commit() 
                    
        except:
            print "Something went wrong cleaning up the game"
            return false
        
        return true
        
    def initialize(self):
        """
        Initialize game
        """
        
        initialize_db #may need to manage sessions and/or connection pools?
        
        #create list of player objects
        num_players = self.get_num_players
        players = []
        temp_chars = self.__characters
        
        #if a game isn't already in progress, continue
        if not check_game_status: 
        
            for i in 0..num_players:
                p = Player()
                players.add(temp_chars.pop())
                
            self.players = players
            self.case_file = self.__create_case()
            
            self._card_list = self.__make_card_list(self.case_file) 
            self.game_board = Board()
            self.gamerules = GameRules()
            
            #initialize board & write to DB
            for p in players:
                for r in self.__room_dict:
                    if self.gamerules.is_empty_room(r):
                        self.game_board.set_player_location(p, r, self.conn)
                        
                        try:
                            self.game_board.set_player_location(p, self.conn)
                        except:
                            raise
            
            for w in self.__weapon_dict:
                for r in self.__room_dict:
                    self.game_board.set_weapon_location(w, r, self.conn)
                    
                
            self.active_player = self.players[0]
            self.__game_status = True
            
            #update DB
            try:
                ins = game_ins(player_list=self.players)
                self.conn.execute(ins)
                ins = game_ins(active_player = self.active_player.get_character(self.conn))
                self.conn.execute(ins)
                ins = game_ins(game_status = self.__game_status)
                self.conn.execute(ins)
                
            except:
                raise
                
            while len(self._card_list) > 0:
                for player in self.players:
                    card = self.__get_remaining_card(self._card_list)
                    player.hand[card] = card
    
                    #add each player to DB
                    try:
                        ins = player_ins(character_name=player.get_character)
                        self.conn.execute(ins)
                        ins = player_ins(location=player.location)
                        self.conn.execute(ins)
                        ins = player_ins(cards=player.hand)
                        self.conn.execute(ins)
                        ins = player_ins(inplay=player.inplay)
                        self.conn.execute(ins) 
    
                    except:
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
    def get_active_player_name(self):
        """
        Returns the active player's name
        """
        try:
            active_player_name = self.conn.execute("SELECT active_player FROM game")
        except:
            raise

        return active_player_name
    
    def get_active_player(self):
        """
        Returns the active player's name
        """
        
        name = get_active_player_name
        
        for p in players:
            if p.get_character == name:
                return p
    
    @property
    def get_game_state(self):
        """
        Returns the state of the game
        """
        try:
            self.__game_status = self.conn.execute("SELECT game_status FROM game")
        except:
            raise
        
        return self.__game_status
    
    
    def __set_active_player(self):
        """
        Set the next active player
        """
        player_inplay = False
        self.active_player = get_active_player
        
        while player_inplay == False:    
            try:
                self.active_player = self.players[self.players.index(self.active_player) + 1]
                current_player = self.players[self.players.index(self.active_player)]
                player_inplay = current_player.inplay
                
                try:
                    status = self.conn.execute("UPDATE players SET players.active_player=" + self.active_player)
                except:
                    raise
                
            except IndexError:
                self.active_player = player = self.players[0]
                current_player = self.players[0]
                player_inplay = current_player.inplay
            
            # If loop through all players and no one is active
            if self.active_player.get_name == current_active:
                self.__game_status = False
                status = self.conn.execute("UPDATE game SET game.status=FALSE")
                
                try:
                    self.case_file = self.conn.execute("SELECT case_file FROM players")
                except:
                    raise
                
                print "It was %s in the %s with the %s" % (self.case_file["Suspect"],self.case_file["Room"],self.case_file["Weapon"])
                print "The game is over. Everyone guessed incorrectly"
                break
        
        
    def __set_disprove_player_order(self):
        """
        Return a list of players in order for disproving a suggestion
        """
        disprove_player_list = []
        
        self.active_player = get_active_player
        
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
            self.conn.create
            num_players = self.conn.execute("SELECT num_players FROM players")
            num_players += 1
            ins = player_ins(num_players = num_players)
            self.conn.execue(ins)
        except:
            raise
        
        players.add(player_name)
        
        try:
            ins = game_ins(name = player_name)
            self.conn.execute(ins)
        except:
            return false
        
        return true               
        
    
    def get_num_players(self):
        
        try:
            self.__num_players = self.conn.execute("SELECT num_players FROM game")                    
        except:
            raise
        
        return self.__num_players
    
    
    def make_move(self,move_to):
        """
        Movement of player 
        """
        
        if self.gamerules.is_valid_move(self.game_board, self.active_player, move_to):
            self.game_board.set_player_location(self.active_player, move_to, self.conn)
            print "%s has moved to %s" % (self.active_player.get_name, move_to)
            return True
        else:
            print "That is not a valid move."
            return False


    def make_suggestion(self,suspect,weapon):
        """
        Player makes a suggestion
        """
        self.active_player = get_active_player
                
        self.suggest_room = self.active_player.get_position
        self.suggest_suspect = suspect
        self.suggest_weapon = weapon
        
        #Move player's character to new room
        for p in self.players:
            if p.get_character == suspect:
                self.game_board.set_player_location(p, self.suggest_room, self.conn)
                print "%s (%s) is now at %s" % (p.get_name, p.get_character, p.get_position)
        
        print ("%s thinks it was %s in the %s with a %s." %\
               (self.active_player.get_name, self.suggest_suspect, self.suggest_room, self.suggest_weapon))
        
    
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
        
           
    def disprove_suggestion(self,player,card):
        #I think this will need to be implemented once the interaction
        #once there is a way to interace with the UI
        """
        Player can disprove another's suggestion
        """
        print ("Player %s disproved suggestion by revealing %s." %\
               (player.get_name, player.reveal_card(card)))
        
        return True
    
    def make_accusation(self,room,suspect,weapon):
        """
        Player makes accusation
        """
        try:
            self.case_file = self.conn.executet("SELECT case_file FROM game")
            self.active_player = get_active_player
                    
        except:
            raise
        
        if (suspect == self.case_file["Suspect"]) and (room == self.case_file["Room"]) and (weapon == self.case_file["Weapon"]):
            print "You are correct. You have won"
            self.__game_status = False
            
            try:
                self.conn.execute("UPDATE game SET case_file=" + self.__game_status)
            except:
                raise
            
        else:
            self.active_player.inplay = False
            print "Your guess was incorrect"
            print "It was not %s in the %s with the %s" % (suspect,room,weapon)
            
            try:
                self.conn.execute("UPDATE players SET inplay=" + self.activeplayer.inplay \
                                  + " WHERE players.character_name=" + self.active_player.get_character)
            except:
                raise
    
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
    
    def initialize_db(self):
        metadata = MetaData()

        players = Table('players', metadata,
            Column('character_name', Integer, primary_key = True), \
            Column('inplay', Boolean, nullable = False), \
            Column('location', String(60), nullable = True), \
            Column('cards', PickleType(), nullable = False))

        game = Table('game', metadata, \
            Column('num_players', Integer, primary_key = True), \
            Column('case_file', PickleType(), nullable = False), \
            Column('active_player', ForeignKey("players.character_name"), nullable=False), \
            Column('game_status', Boolean, nullable = False), \
            Column('player_list', PickleType(), nullable = False))

        board = Table('board', metadata, \
                      Column('weapon', String(40), nullable = False), \
                      Column('weapon_location', String(40), nullable = False), \
                      Column('player', ForeignKey("players.character_name"), nullable = False), \
                      Column('player_location', String(40), nullable = False))
        
        engine = create_engine('sqlite:////var/www/mrboddy/boddyinc/boddyinc/database.db')
        
        metadata.create_all(engine)
