from pyramid.config import Configurator
from boddyinc.resources import Root
from sqlalchemy import engine_from_config
from boddyinc.models import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(root_factory=Root, settings=settings)
    config.add_route('join_game', '/')
    config.add_view('boddyinc.views.join_game',
                    context='boddyinc:resources.Root',
                    renderer='boddyinc:templates/welcome.mako',
                    route_name='join_game')
    config.commit()
    config.add_route('submit', 'submit/')
    config.add_view('boddyinc.views.submit',
                    renderer='boddyinc:templates/new_player.mako',route_name='submit')
    config.add_route('play_game', '/{name}')
    config.add_view('boddyinc.views.main_game',
                    context='boddyinc:resources.Root',
                    renderer='boddyinc:templates/clueless.mako',
                    route_name='play_game')
    '''config.add_view('boddyinc.views.quit_game',
                    context='boddyinc:resources.Root,
                    renderer='boddyinc:templates/welcome.mako')'''
    config.add_static_view('static', 'boddyinc:static', cache_max_age=3600)
    return config.make_wsgi_app()
