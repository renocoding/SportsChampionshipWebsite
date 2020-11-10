# SportsChampsWebsite

INTRODUCTION:
This API loads data from 1940 to present about the major sports in America. The API loads this
sprorts information into 2 dictionaries, one that is accesed by a year, and another that is
accessed by a city or metro area. The main functionality is to use 'get' requests to load the data.
The post requests are reserved for future seasons when a new winner in a new season. The put
requests are there to edit any descrepcincies in the data. The put reset will change the data back
to what the original file stores. The function that you should run are 'gets' because this is
historical data dn ther is very little need to changeit.

TESTING SERVER/API:
In order to  run the server run the file 'server.py found in the 'Server' directory on a different
window.  The server is currently set to run on 'localhost'. Then while in the 'Server' directory, run 'python test_requests.py' to run our test that make sure the controllers and handlers are wokring correctly. To just test the OO API, go into the 'OOAPI' directory and run 'python3 test_OOAPI.py'. The server does not need to be running to test this.

TESTING WEB CLIENT:
Testing the webclient was relatively simple for our website. To test feature one, we tested a bunch of sample years and made sure the champions listed for the year matched up with what we expected when compared to our database values, our own memory, and wikipedia answers. To test feature two, we simply compared a bunch of different cities and checked against our own knowledge as well as checking that it reflected the database's data to make sure that the number of championships shown made sense.

USER INTERACTION:
Our website has two features - 1) championships in a year, 2) comparing the championships of two cities since 1940
1) To interact with the first feature, click on the dropdown to select a year and then hit "Go". It will then populate the webpage with the winners in several major sports in the chosen year.
2) To interact with the second feature, click on both dropdowns to select to different cities and then hit "Go". It will then show you (graphically and in text) the comparison of the number of championships in each city since 1940 (comprised only of the sports shown in Feature 1)

RUNNING SERVER:
UOur server is run on port 51081 and is by default set to localhost. In order to sun the server, enter the Server directory and run the file named 'server.py'  This can be done in a terminal by running the command 'python server.py' form the "Server" directory. Once you have done this the server should be running. At this point you can go to the following link: https://rdomel.gitlab.io/SportsChampsWebsite/jsfrontend/mainPage.html (DO NOT USE SAFARI)
Now, to use the front end, see the 'USER INTERACTION' for how to use the front end.

JSON SPECIFICATION:
To see json specification, click on the following link: https://docs.google.com/document/d/1TDIrrV_5wHV8K28aR1vJk4iekL0Xt5zJkR2hsd3nV2c/edit

SCALE AND COMPLEXITY:
We assessed the complexity of our project as being about medium complexity. It was not easy setting up the server, being that there are three resource endpoints, and furthermore, there was a lot of data too manage (JSON specification was "heavy"). However, it was not overwhelmingly complex because we mostly parse GET requests. As for the scale, we think the scale of the project is slightly greater than average. This is simply because we had so much data to parse and think about (So much sports data!). Similarly, it was still managable because our use and analysis of the data wasn't too overly complicated.
