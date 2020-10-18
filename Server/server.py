import cherrypy
from yearController import YearController
from cityController import CityController
from champ_library import champ_database


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # create database object and pass it to both controllers
    cdb = champ_database()
    yearController     = YearController(cdb=cdb)
    cityController     = CityController(cdb=cdb)

    # connect year handlers
    dispatcher.connect('year_get', '/years/:year', controller=yearController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('year_put', '/years/:year', controller=yearController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('year_delete', '/years/:year', controller=yearController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('year_index_post', '/years/', controller=yearController, action = 'POST_INDEX', conditions=dict(method=['POST']))

    # connect city handlers
    dispatcher.connect('city_get', '/cities/:city', controller=cityController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('city_put', '/cities/:city', controller=cityController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('city_delete', '/cities/:city', controller=cityController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('city_index_post', '/cities/', controller=cityController, action = 'POST_INDEX', conditions=dict(method=['POST']))



    conf = {
	'global': {
            'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'localhost', #
	    'server.socket_port': 51081, #change port number to your assigned
	    },
	'/': {
	    'request.dispatch': dispatcher,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    start_service()
