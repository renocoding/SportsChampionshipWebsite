import cherrypy
import re, json
import sys
sys.path.insert(1, "../OOAPI")
from _champ_library import champ_database

class CityController(object):

    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = champ_base()
        else:
            self.cdb = cdb

        self.cdb.load_city_data('data_by_year_start1940.json')

    def GET_KEY(self, city):
        '''when GET request for /cities/city comes in, then we respond with json string'''
        output = {'result':'success'}

        try:

            # get num championships for city if possible
            championships = self.cdb.get_city(city)
            if championships is not None:
                output['city'] = city
                output['championships'] = championships

            # city not in cdb
            else:
                output['result'] = 'error'
                output['message'] = 'city not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def GET_INDEX(self):
        '''when GET request for /cities/ comes in, we respond with all the cities'''
        output = {'result':'success'}
        output['cities'] = []

        try:
            for city in self.cdb.get_cities():
                output['cities'].append(city)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)


    def PUT_KEY(self, city):
        '''when PUT request for /cities/city comes in, then we change that city in the cdb'''
        output = {'result':'success'}

        try:

            # get body
            data = json.loads(cherrypy.request.body.read().decode('utf-8'))

            # call helper function to change data of existing city
            champs = int(data['championships'])
            self.cdb.set_city(city, champs)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)


    def POST_INDEX(self):
        '''when POST for /cities/ comes in, we add data of the form {'Chicago, IL' : 20} and add it to the cdb'''
        output = {'result' : 'success'}
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))

        # create new city in database and assign it the corresponding number of 'ships
        try:
            self.cdb.city_data[list(data.keys())[0]] = data[list(data.keys())[0]]
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)


    def DELETE_KEY(self, city):
        '''when DELETE for /cities/ comes in, we remove that city from cdb object'''
        output = {'result' : 'success'}
        # main operation
        try:
            self.cdb.delete_city(city)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
