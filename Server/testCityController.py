import unittest
import requests
import json

class TestCitiesController(unittest.TestCase):

    SITE_URL = 'http://localhost:51081' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    CITIES_URL = SITE_URL + '/cities/'
    RESET_URL = SITE_URL +'/reset/'

    def reset_data(self):
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_cities_key_get(self):
        self.reset_data()

        city = 'Houston, TX'

        # make sure get request returns 3, which is number of championships in houston
        r = requests.get(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['championships'], 3)

    def test_cities_put_key(self):
        self.reset_data()

        city = 'Houston, TX'

        # get request
        r = requests.get(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['championships'], 3)          # checks that total champs is correct ie: 3

        # put request to change value
        c = {}
        c['championships'] = 15
        r = requests.put(self.CITIES_URL + city, data = json.dumps(c))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')         # checks that we update city to 10

        # make sure value has changed
        r = requests.get(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['championships'], 15)         # checks using a get that the put was correct

    def test_cities_post(self):
        self.reset_data()

        # make put request for new city
        c = {}
        c['Steubenville, OH'] = 50
        r = requests.post(self.CITIES_URL, data = json.dumps(c))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        # make sure database reflects change using get request
        r = requests.get(self.CITIES_URL + list(c.keys())[0])
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['championships'], 50)

    def test_cities_delete_key(self):
        self.reset_data()

        city = 'Houston, TX'

        # delete data associatd with Houston
        r = requests.delete(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # make sure following get request fails
        r = requests.get(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')



if __name__ == "__main__":
    unittest.main()
