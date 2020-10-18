import unittest
import requests
import json

class TestReset(unittest.TestCase):

    SITE_URL = 'http://localhost:51081' # replace with your port id
    print("Testing for server: " + SITE_URL)
    CITIES_URL = SITE_URL + '/cities/'
    YEARS_URL = SITE_URL + '/years/'
    RESET_URL = SITE_URL + '/reset/'

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_put_reset_cities(self):
        city = 'Houston, TX'
        expected = {'championships':3}
        altered = {'championships':100}

        # change houston to 100
        r = requests.put(self.CITIES_URL + city, data = json.dumps(altered))  
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # resets the data so houston is 3 again
        r = requests.put(self.RESET_URL)                           
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        # gets houston data after rest
        r2 = requests.get(self.CITIES_URL + city)                   
        self.assertTrue(self.is_json(r2.content.decode('utf-8')))
        resp2 = json.loads(r2.content.decode())

        # check that houston is  3  again
        self.assertEqual(resp2['championships'], expected['championships']) 

    def test_put_reset_years(self):
        year = '2005'
        expected = {'NCAA Football (M)': 'USC Trojans', 'NFL': 'New England Patriots', 'NCAA Basketball (M)': 'North Carolina Tar Heels',
            'NBA': 'San Antonio Spurs', 'NCAA Basketball (W)': 'Baylor Bears', 'MLB': 'Chicago White Sox'}
        altered = {'NCAA Football (M)': 'Notre Dame', 'NFL': 'Notre Dame', 'NCAA Basketball (M)': 'Notre Dame',
            'NBA': 'Notre Dame', 'NCAA Basketball (W)': 'Notre Dame', 'MLB': 'Notre Dame'}

        #  changes 2005 so that its all notre dame
        r = requests.put(self.YEARS_URL + year, data = json.dumps(altered)) 
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # resets  2005 to correct data
        r = requests.put(self.RESET_URL)                           
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        # gets data after correction
        r = requests.get(self.YEARS_URL + year)                     
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # see if request matches expected
        self.assertEqual(resp['championship_data'], expected)


if __name__ == "__main__":
    unittest.main()
