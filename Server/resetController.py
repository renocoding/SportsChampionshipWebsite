import cherrypy
import re, json
from champ_library import champ_database

class ResetController(object):

    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = champ_database()
        else:
            self.cdb = cdb


    def PUT_INDEX(self):
        '''when PUT request comes in to /reset/ endpoint, then the cities and years database is reloaded'''
        output = {'result':'success'}

        self.cdb.__init__()
        self.cdb.load_year_data("data_by_year_start1940.json")
        self.cdb.load_city_data("data_by_year_start1940.json")

        return json.dumps(output)
