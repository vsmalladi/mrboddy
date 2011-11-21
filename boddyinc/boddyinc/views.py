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

'''formatter = formatters.HtmlFormatter(linenos=True, cssclass="source")
style_defs = formatter.get_style_defs()
all_lexers = list(lexers.get_all_lexers())
all_lexers.sort()
lexer_info = []
for name, aliases, filetypes, mimetypes_ in all_lexers:
    lexer_info.append({'alias':aliases[0], 'name':name})'''
    
#views

@view_config(renderer='clueless.mako')
def main_game(request):
    return {'project':'my project'}
    

#@view_config(context=Forbidden, renderer='templates/login.pt')
@view_config(renderer='templates/welcome.mako')
def join_game(request):
    #login_url = request.resource_url(request.context, 'join')
    '''referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)'''
    ''' message = ''
    login = ''
    
    if 'form.submitted' in request.params:
        login = request.params['login']
        return HTTPFound(location = came_from, headers = headers)'''
    return {'content':'Join Game Test'}
    
@view_config(name='quit_game', context='''PasteBin''', permission='view')
def quit_game(request):
    ''' headers = forget(request)
    return HTTPFound(location = request.resource_url(request.context),
                     headers = headers)'''
    return {'content':'exit'}
    



