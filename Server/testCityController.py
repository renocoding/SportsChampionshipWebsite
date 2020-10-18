import unittest
import requests
import json

class TestMoviesIndex(unittest.TestCase):

    SITE_URL = 'localhost' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    CITIES_URL = SITE_URL + '/cities/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_cities_key_get(self):

        city = 'Houston, TX'
        r = requests.get(self.CITIES_URL + city)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['championships'], 3)

if __name__ == "__main__":
    unittest.main()