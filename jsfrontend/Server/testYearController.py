import unittest
import requests
import json

class TestYearController(unittest.TestCase):

    SITE_URL = 'http://localhost:51081' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    YEARS_URL = SITE_URL + '/years/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_years_key_get(self):
        self.reset_data()

        # year and the exepcted
        year = '2005'
        expected = {'NCAA Football (M)': 'USC Trojans', 'NFL': 'New England Patriots', 'NCAA Basketball (M)': 'North Carolina Tar Heels',
            'NBA': 'San Antonio Spurs', 'NCAA Basketball (W)': 'Baylor Bears', 'MLB': 'Chicago White Sox'}

        # make request
        r = requests.get(self.YEARS_URL + year)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # see if request matches expected
        self.assertEqual(resp['championship_data'], expected)

    def test_years_put_key(self):
        self.reset_data()

        # make initial get request
        year = "2005"
        r = requests.get(self.YEARS_URL + year)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # make sure get request works
        self.assertTrue(resp['championship_data'], {'NCAA Football (M)': 'USC Trojans', 'NFL': 'New England Patriots', 'NCAA Basketball (M)': 'North Carolina Tar Heels', 'NBA': 'San Antonio Spurs', 'NCAA Basketball (W)': 'Baylor Bears', 'MLB': 'Chicago White Sox'})

        # make put request
        data_to_enter = {'MLB': "Chicago White Sox", "NBA" : "Houston  Rockets"}
        r = requests.put(self.YEARS_URL + year, data = json.dumps(data_to_enter))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # make get request to make sure put worked
        year = "2005"
        r = requests.get(self.YEARS_URL + year)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['championship_data'], data_to_enter)


    def test_years_index_post(self):
        self.reset_data()

        # year and data to be entered
        data_to_enter = {'2040' : {'MLB': "Mars Aliens", "NBA" : "Chicago Bulls"}}

        # make request
        r = requests.post(self.YEARS_URL, data = json.dumps(data_to_enter))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))

        # see if request matches expected
        self.assertEqual(resp['result'], 'success')

        # make get request to make sure post worked
        r = requests.get(self.YEARS_URL + "2040")
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['championship_data'], data_to_enter['2040'])

    def test_years_delete_key(self):
        self.reset_data()

        year = '2005'

        # make sure delete works
        r = requests.delete(self.YEARS_URL + year)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        # make sure get on the same year actually works
        r = requests.get(self.YEARS_URL + year)
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')





if __name__ == "__main__":
    unittest.main()
