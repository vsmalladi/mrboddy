#! /usr/local/bin/python
import sqlalchemy
from sqlalchemy import *

metadata = MetaData()

players = Table('players', metadata,
    Column('character_name', Integer, primary_key = True), \
    Column('inplay', Boolean, nullable = False), \
    Column('location', String(60), nullable = True), \
    Column('cards', PickleType(), nullable = False), \
    Column('name', String, nullable = False))

game = Table('game', metadata, \
    Column('num_players', Integer, primary_key = True), \
    Column('case_file', PickleType(), nullable = False), \
    Column('active_player', ForeignKey("players.character_name"), nullable=False), \
    Column('game_status', Boolean, nullable = False), \
    Column('player_list', PickleType(), nullable = False))
)

board = Table('board', metadata, \
              Column('weapon', String(40), nullable = False), \
              Column('weapon_location', String(40), nullable = False), \
              Column('player', ForeignKey("players.character_name"), nullable = False), \
              Column('player_location', String(40), nullable = False))

engine = create_engine('sqlite:////var/www/mrboddy/boddyinc/boddyinc/database.db')

metadata.create_all(engine)
