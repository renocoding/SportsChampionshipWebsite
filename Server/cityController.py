import cherrypy
import re, json
from champ_library import champ_database

class CityController(object):

    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = champ_base()
        else:
            self.cdb = cdb

        self.cdb.load_city_data('data_by_year_start1940.json')

    def GET_KEY(self, city_id):
    '''when GET request for /cities/city_id comes in, then we respond with json string'''
            output = {'result':'success'}

        try:
            championships = self.cdb.get_city(city_id)
            if movie is not None:
                output['id'] = movie_id
                output['championships'] = championships
            else:
                output['result'] = 'error'
                output['message'] = 'city not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def PUT_KEY(self, city_id):
    '''when PUT request for /movies/movie_id comes in, then we change that movie in the cdb'''
        output = {'result':'success'}

        try:
            data = json.loads(cherrypy.request.body.read().decode('utf-8'))
            champs = int(data['championshps'])
            self.cdb.set_city(city_id, champs)
        except Exception as ex:
            output['result'] = 'error'
            outout['message'] = str(ex)

        return json.dumps(output)


    def POST_INDEX(self):
    '''when POST for /movies/ comes in, we take title and genres from body of request, and respond with the new movie_id and more'''
        output = {'result' : 'success'}
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))

        # perform main operation
        try:
            self.cdb.city_data[data.keys()[0]] = data['champioships']
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

    def DELETE_KEY(self, city_id):
    '''when DELETE for /movies/ comes in, we remove each existing movie from cdb object'''
        output = {'result' : 'success'}
        # main operation
        try:
            self.cdb.delete_city(city_id)

        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
