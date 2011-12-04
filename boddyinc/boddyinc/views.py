from pyramid.renderers import render
from pyramid.view import view_config
import sys
import urlparse

import webob
#import formencode
from webob.exc import HTTPFound

'''import pygments
from pygments import lexers
from pygments import formatters
from pygments import util'''

from pyramid.traversal import find_interface
from pyramid.security import authenticated_userid
from pyramid.security import has_permission
from pyramid.security import remember
from pyramid.security import forget
from pyramid.exceptions import Forbidden


from game import Game

current_game = Game()

#views

@view_config(route_name='game', renderer='clueless.mako')
def main_game(request):
    return {'project':'my project'}
    

@view_config(route_name='welcome',renderer='welcome.mako')
def join_game(request):
    game_status = current_game.get_game_state
    num_players = current_game.get_num_players()
    return {'state':game_status,'players':num_players}
    
@view_config(route_name='submit',renderer='clueless.mako')
def submit(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            current_game.add_player(request.POST.get('name'))
            return HTTPFound(location=request.route_url('join_game'))
    return {}


    
    
@view_config(name='quit_game', context='''PasteBin''', permission='view')
def quit_game(request):
    ''' headers = forget(request)
    return HTTPFound(location = request.resource_url(request.context),
                     headers = headers)'''
    return {'content':'exit'}
    



