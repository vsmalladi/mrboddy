from pyramid.config import Configurator
from boddyinc.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('boddyinc.views.my_view',
                    context='boddyinc:resources.Root',
                    renderer='boddyinc:templates/clueless.mako')
    config.add_static_view('static', 'boddyinc:static', cache_max_age=3600)
    return config.make_wsgi_app()
