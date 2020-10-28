import json

class champ_database:

    # constructor
    def __init__(self):
        self.year_data = dict()
        self.city_data = dict()


    def load_city_data(self, filename):

        # json parsing in python, source used - https://www.geeksforgeeks.org/read-json-file-using-python/
        json_file = open("../OOAPI/data_by_year_start1940.json");
        json_data = json.load(json_file)

        # loop through each year
        for year, result in json_data.items():

            # loop through each sport in each year
            for sport in result:

                # get data for each sport and update our city-sorted data
                if sport['sport'] == "NBA" or sport['sport'] == "MLB" or sport['sport'] == "NFL" or sport['sport'] == "NHL":
                   self.city_data[sport['winner_metro']] = 1 + self.city_data.get(sport['winner_metro'], 0)
                elif sport['level'] == "college" and sport['sport'] == "Basketball (M)":
                   self.city_data[sport['winner_metro']] = 1 + self.city_data.get(sport['winner_metro'], 0)
                elif sport['level'] == "college" and sport['sport'] == "Basketball (W)":
                   self.city_data[sport['winner_metro']] = 1 + self.city_data.get(sport['winner_metro'], 0)
                elif sport['level'] == "college" and sport['sport'] == "Football (M)":
                   self.city_data[sport['winner_metro']] = 1 + self.city_data.get(sport['winner_metro'], 0)

        json_file.close()


    def load_year_data(self, filename):

        print("Loading year data...")

        # json parsing in python, source used - https://www.geeksforgeeks.org/read-json-file-using-python/
        json_file = open("../OOAPI/data_by_year_start1940.json");
        json_data = json.load(json_file)

        # loop through each year
        for year, result in json_data.items():
            self.year_data[year] = {}

            # loop through each sport in each year
            for sport in result:

                # get data for each sport and update our year-sorted
                if sport['sport'] == "NBA" or sport['sport'] == "MLB" or sport['sport'] == "NFL" or sport['sport'] == "NHL":
                   self.year_data[year][sport['sport']] = sport['winner']
                elif sport['level'] == "college" and sport['sport'] == "Basketball (M)":
                   self.year_data[year]["NCAA Basketball (M)"] = sport['winner']
                elif sport['level'] == "college" and sport['sport'] == "Basketball (W)":
                   self.year_data[year]["NCAA Basketball (W)"] = sport['winner']
                elif sport['level'] == "college" and sport['sport'] == "Football (M)":
                   self.year_data[year]["NCAA Football (M)"] = sport['winner']
        json_file.close()

    def get_year(self, year):

        # try to get the champions from that given year from dictionary
        try:
            champions = self.year_data[year]
        except Exception as ex:
            champions = None

        return champions

    def get_city(self, city):

        # try go get the championship number from given city from dictionary
        try:
            championships = self.city_data[city]
        except Exception as ex:
            championships = None

        return championships

    def get_cities(self):
        return self.city_data.keys()

    def delete_year(self, year):
        # simply delete key-val pair for given year
        try:
            del(self.year_data[year])
        except Exception as ex:
            print(str(ex))

    def delete_city(self, city):
        # simply delete key-val pair for given city
        del(self.city_data[city])


    def set_year(self, year, data):
        # add data to associated year in database
        self.year_data[year] = data

    def set_city(self, city, data):
        # add data to associated city in database
        self.city_data[city] = data

if __name__ == "__main__":

    # create champ database object
    cdb = champ_database()

    # fill two dictionaries
    cdb.load_year_data("data_by_year_start1940.json")
    cdb.load_city_data("data_by_year_start1940.json")
