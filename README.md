# SportsChampsWebsite

INTRODUCTION:
This API loads data from 1940 to present about the major sports in America. The API loads this
sprorts information into 2 dictionaries, one that is accesed by a year, and another that is
accessed by a city or metro area. The main functionality is to use 'get' requests to load the data.
The post requests are reserved for future seasons when a new winner in a new season. The put 
requests are there to edit any descrepcincies in the data. The put reset will change the data back 
to what the original file stores. The function that you should run are 'gets' because this is
historical data dn ther is very little need to changeit.

TESTING:
In order to  run the server run the file 'server.py found in the 'Server' directory on a different 
window.  The server is currently set to run on 'localhost'. Then in the 'Server' directory, run 'python test_Requests.py' to run our test that make sure the controllers and handlers are wokring correctly.

To just test the OO API, go into the 'OOAPI' directory and run 'python3 test_OOAPI.py'. The server does not need to be running to test this.
