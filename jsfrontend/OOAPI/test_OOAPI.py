import unittest
import requests
import json
from _champ_library import champ_database

class TestOOAPI(unittest.TestCase):

    SITE_URL = 'http://localhost:51081' # replace with your assigned port id
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_get_year(self):

        # initalize database
        cdb = champ_database()
        cdb.load_year_data("data_by_year_start1940.json")
        expected = {'NCAA Football (M)': 'USC Trojans', 'NFL': 'New England Patriots', 'NCAA Basketball (M)': 'North Carolina Tar Heels',
            'NBA': 'San Antonio Spurs', 'NCAA Basketball (W)': 'Baylor Bears', 'MLB': 'Chicago White Sox'}

        # call get year
        result_get_year = cdb.get_year("2005")

        # see if get_year matches expected
        self.assertEqual(result_get_year, expected)

    def test_set_year(self):
        # initalize database
        cdb = champ_database()
        #cdb.load_year_data("data_by_year_start1940.json")

        # change cdb using set
        year = "2040"
        expected = {"MLB": "Mars Aliens"}
        cdb.set_year(year, expected)

        # see if get_year matches expected
        result_get_year = cdb.get_year(year)
        self.assertEqual(result_get_year, expected)

    def test_delete_year(self):
        #initalize database
        cdb = champ_database()
        cdb.load_year_data("data_by_year_start1940.json")
        year = "2005"

        # change cdb using delete
        cdb.delete_year(year)

        # see if get_year matches None type
        result_get_year = cdb.get_year(year)
        self.assertEqual(result_get_year, None)

    def test_get_city(self):

        # initalize database
        cdb = champ_database()
        cdb.load_city_data("data_by_year_start1940.json")
        city = 'Houston, TX'
        expected = 3

        # call get city
        result_get_city = cdb.get_city(city)

        # see if get_city matches expected
        self.assertEqual(result_get_city, expected)

    def test_get_cities(self):

        # initalize database
        cdb = champ_database()
        cdb.load_city_data("data_by_year_start1940.json")
        expected = ['College Station, TX', 'Bloomington, IN', 'New York Metro Area', 'Cincinnati, OH', 'Chicago, IL', 'Twin Cities, MN', 'Madison, WI', 'Greater Boston, MA', 'San Francisco Bay Area, CA', 'Toronto, ON', 'St. Louis, MO', 'Washington, DC Metro Area', 'Columbus, OH', 'Cheyenne, WY', 'Metro Detroit, MI', 'Notre Dame, IN', 'Salt Lake City, UT', 'Montreal, QC', 'Green Bay, WI', 'West Point, NY', 'Stillwater, OK', 'Cleveland, OH', 'Worcester, MA', 'Greater Philadelphia, PA', 'Lexington-Fayette, KY', 'Baltimore, MD', 'Ann Arbor, MI', 'Oklahoma City, OK', 'Rochester, NY', 'Greater Los Angeles, CA', 'Knoxville, TN', 'Lawrence, KS', 'East Lansing, MI', 'Syracuse, NY', 'Greater Raleigh, NC', 'Milwaukee, WI', 'Auburn, AL', 'Iowa City, IA', 'Baton Rouge, LA', 'Pittsburgh, PA', 'Oxford, MS', 'Tuscaloosa, AL', 'Austin, TX', 'Northwest Arkansas, AR', 'El Paso, TX', 'Kansas City, MO', 'Lincoln, NE', 'Dallas-Fort Worth, TX', 'Greater Miami Area, FL', 'Portland Metro Area, OR', 'Tallahassee, FL', 'Seattle,WA', 'Richmond, KY', 'Louisville, KY', 'Athens, GA', 'Boise City, ID', 'Greenville, SC', 'Pocatello, ID', 'Monroe, LA', 'State College, PA', 'Columbia, SC', 'Carbondale, IL', 'Edmonton, AB', 'Provo, UT', 'Bozeman, MT', 'Norfolk, VA', 'Statesboro, GA', 'Calgary, AB', 'Las Vegas, NV', 'Atlanta, GA', 'Boulder, CO', 'Youngstown, OH', 'Huntington, WV', 'Lubbock, TX', 'Houston, TX', 'Hartford, CT', 'Missoula, MT', 'Denver, CO', 'Gainesville, FL', 'Tucson, AZ', 'Springfield, MA', 'San Antonio, TX', 'West Lafayette, IN', 'Metro Phoenix, AZ', 'Bowling Green, KY', 'Tampa Bay Area, FL', 'Newark, DE', 'Harrisonburg, VA', 'Waco, TX', 'Boone, NC', 'Indianapolis Metro Area, IN', 'Richmond, VA', 'New Orleans, LA', 'Spokane, WA', 'Fargo, ND']

        # call get cities
        result_get_cities = list(cdb.get_cities())

        # see if get_city matches expected
        self.assertEqual(result_get_cities,expected)

    def test_set_city(self):
        # initalize database
        cdb = champ_database()
        #cdb.load_city_data("data_by_year_start1940.json")

        # change cdb using set
        city = "Steubenville, OH"
        expected = 100
        cdb.set_city(city, expected)

        # see if get_city matches expected
        result_get_city = cdb.get_city(city)
        self.assertEqual(result_get_city, expected)

    def test_delete_city(self):
        #initalize database
        cdb = champ_database()
        cdb.load_city_data("data_by_year_start1940.json")
        city = "Houston, TX"

        # change cdb using delete
        cdb.delete_city(city)

        # see if get_city matches None type
        result_get_city = cdb.get_city(city)
        self.assertEqual(result_get_city, None)



if __name__ == "__main__":
    unittest.main()
