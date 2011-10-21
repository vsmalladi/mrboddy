#! /usr/local/bin/python

#Import statments
from random import randrange
from random import shuffle
from string import *
from player import Player

#Dictionaries
character_dict = {0 :"Colonel Mustard", 1:"Miss Scarlet", 2:"Prof. Plum", 3:"Mr. Green", 4:"Mrs. White", 5:"Mrs. Peacock"}
weapon_dict = {0 :"Rope", 1:"Lead Pipe", 2:"Knife", 3:"Wrench", 4:"Candlestick", 5:"Pistol"}
room_dict = {0 :"Hall", 1:"Lounge", 2:"Dining Room", 3:"Kitchen", 4:"Ballroom", 5:"Conservatory", 6:"Billiard Room", 7:"Library", 8:"Study"}

#Define a random card picker
def get_card(card_dict):
    """
    Returns a random card from the card dictionary
    """
    card = card_dict[randrange(0,len(card_dict))]
    return card

#Define case file
def get_case():
    """
    Returns case dictionary including the suspect, weapon, and room
    """
    case = {}
    case['Suspect'] = get_card(character_dict)
    case['Weapon'] = get_card(weapon_dict)
    case['Room'] = get_card(room_dict)
    return case

#Make leftover card list that doesn't include cards in case
def make_card_list(case):
    """
    Returns suffled list of cards not in case file
    """
    cards = []
    for value in character_dict.values():
        if value != case['Suspect']:
            cards.append(value)
    
    for value in weapon_dict.values():
        if value != case['Weapon']:
            cards.append(value)  
    
    for value in room_dict.values():
        if value != case['Room']:
            cards.append(value)
            
    shuffle(cards)
    return cards

#Randomly get a card from a list
def get_remaining_card(card_list):
    """
    Returns a random card from the remaing card list and removes
    it from the list
    """
    card = card_list.pop(randrange(0,len(card_list)))
    return card

