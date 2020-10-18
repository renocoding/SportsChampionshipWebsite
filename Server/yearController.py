import cherrypy
import re, json
from champ_library import champ_database

class YearController(object):

        def __init__(self, cdb=None):
                if cdb is None:
                        self.cdb = champ_database()
                else:
                        self.cdb = cdb

                self.cdb.load_year_data('data_by_year_start1940.json')

        def GET_KEY(self, year):
		'''when GET request for /years/year comes in, then we respond with json string'''
                output = {'result':'success'}

                try:

                        # returns dict of form {'MLB': 'White Sox', 'NBA' : 'Bulls'....}
                        winners_in_year = self.cdb.get_year(year)

                        # year exists in cdb
                        if winners_in_year is not None:
                            output['year'] = year
                            output['championship_data'] = winners_in_year

                        # year does not exist
                        else:
                            output['result'] = 'error'
                            output['message'] = 'movie not found'

                # catch other errors
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def PUT_KEY(self, year):
		'''when PUT request for /years/year comes in, then we change that year in the cdb'''
                output = {'result':'success'}

                # get body from put request
                winners_in_year = json.loads(cherrypy.request.body.read().decode('utf-8'))

                # call helper function to make data of the form {year: {'MLB': 'White Sox', 'NBA' : 'Bulls'....}}
                self.cdb.set_year(year, winners_in_year)

                return json.dumps(output)
