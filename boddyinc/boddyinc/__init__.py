from pyramid.config import Configurator
from boddyinc.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)    
    config.add_view('boddyinc.views.join_game',
                    context='boddyinc:resources.Root',
                    renderer='boddyinc:templates/welcome.mako')
    config.add_route('playgame', '/{one}')
    config.add_view('boddyinc.views.main_game',
                    context='boddyinc:resources.Root',
                    renderer='boddyinc:templates/clueless.mako',
                    route_name='playgame')
    '''config.add_view('boddyinc.views.quit_game',
                    context='boddyinc:resources.Root,
                    renderer='boddyinc:templates/welcome.mako')'''
    config.add_static_view('static', 'boddyinc:static', cache_max_age=3600)
    return config.make_wsgi_app()
