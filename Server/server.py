import cherrypy
from yearController import YearController
from cityController import CityController
from resetController import ResetController

import sys
sys.path.insert(1, "../OOAPI")
from _champ_library import champ_database

class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    # create database object and pass it to both controllers
    cdb = champ_database()
    yearController     = YearController(cdb=cdb)
    cityController     = CityController(cdb=cdb)
    resetController     = ResetController(cdb=cdb)

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

    # connect reset handler
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))


    # cors handlers
    dispatcher.connect('years_key_options', '/years/:year', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('years_options', '/years/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('reset_key_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('rating_options', '/cities/:city', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('rating_options', '/cities/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))


    conf = {
	'global': {
            'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'localhost', #
	    'server.socket_port': 51081, #change port number to your assigned
	    },
	'/': {
	    'request.dispatch': dispatcher,
        'tools.CORS.on': True,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
