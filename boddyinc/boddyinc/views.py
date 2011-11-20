from pyramid.renderers import render
from pyramid.view import view_config

@view_config(renderer='clueless.mako')
def my_view(request):
    return {'project':'my project'}

