///////////////////////////
///////INITIAL TASKS///////
///////////////////////////

console.log('page load - entered main.js for js-other api');

var sendButton1 = document.getElementById('send-button1');
sendButton1.onmouseup = getEnteredYear;

var sendButton2 = document.getElementById('send-button2');
sendButton2.onmouseup = getEnteredCities;

url = "http://localhost:51081"


// UPDATE YEAR SELECT
// info on adding optionss from stackoverflow
var yearSelect = document.getElementById("select-year");

for (i = 1941; i < 2019; i++)
{
    // add year to select
    var option = document.createElement("option");
    option.value = i;
    option.innerHTML = i;
    yearSelect.appendChild(option)
}

updateYearData("1940");

// UPDATE CITY SELECT
// make reqeust to get_index of cities endpoint
var xhr = new XMLHttpRequest();
xhr.open("GET", url + "/cities/", true);
xhr.send(null)

// set up onload
xhr.onload = function(e) { // triggered when response is received

    // must be written before send
    console.log(xhr.responseText);

    // update city select
    var citySelect = document.getElementById("select-city1");
    var citySelect2 = document.getElementById("select-city2");

    responseJson = JSON.parse(xhr.responseText);
    console.log(responseJson["cities"][1])

    // print cities using get
    var i = 0
    for (city in responseJson["cities"])
    {
        // add metro area to select
        var option1 = document.createElement("option");
        var option2 = document.createElement("option");
        option1.value = responseJson["cities"][i];
        option2.value = responseJson["cities"][i];
        option1.innerHTML = responseJson["cities"][i];
        option2.innerHTML = responseJson["cities"][i];
        citySelect.appendChild(option1)
        citySelect2.appendChild(option2)
        i++;
    }
}

// set up onerror
xhr.onerror = function(e) { // triggered when error response is received and must be before send
    console.error(xhr.statusText);
}

updateCityData("College Station, TX", "College Station, TX");

///////////////////////
///////Functions///////
///////////////////////
function getEnteredYear(){
    var selindex = document.getElementById('select-year').selectedIndex; 
    var year = document.getElementById('select-year').options[selindex].value; 
    updateYearData(year);
}

function getEnteredCities(){
    var city1 = document.getElementById("select-city1").value;
    var city2 = document.getElementById("select-city2").value;
    updateCityData(city1, city2);
}

function updateCityData(city1, city2){
    // one request for each inputted city
    var xhr1 = new XMLHttpRequest();
    xhr1.open("GET", url + "/cities/" + city1, true);

    var xhr2 = new XMLHttpRequest();
    xhr2.open("GET", url + "/cities/" + city2, true);

    xhr1.onload = function(e) { // triggered when response is received
        console.log(xhr1.responseText);
        responseJson = JSON.parse(xhr1.responseText);
        champs = responseJson['championships'];

        // updating caption of circle
        var label = document.getElementById("city1-label");
        label.innerHTML = "Number of Championships: " + champs;

        // changing size of circle given number of championships
        var circle = document.getElementById("city1-circle");
        circle.style.width = champs + "0px";
        circle.style.height = champs + "0px";
    }
    xhr2.onload = function(e) { // triggered when response is received
        console.log(xhr2.responseText);
        responseJson = JSON.parse(xhr2.responseText);
        champs = responseJson['championships'];

        // updating caption of circle
        var label = document.getElementById("city2-label");
        label.innerHTML = "Number of Championships: " + champs;

        // changing size of circle given number of championships
        var circle = document.getElementById("city2-circle");
        circle.style.width = champs + "0px";
        circle.style.height = champs + "0px";
    }

    xhr1.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr1.statusText);
    }
    xhr2.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr2.statusText);
    }

    xhr1.send(null)
    xhr2.send(null)
}

function updateYearData(year){
    // make reqeust to get_index of cities endpoint
    var xhr = new XMLHttpRequest();
    console.log(year, "this is whats wrong")
    xhr.open("GET", url + "/years/" + year, true);

    // set up onload
    xhr.onload = function(e) { // triggered when response is received

        // must be written before send
        console.log(xhr.responseText);

        // update year champ data
        responseJson = JSON.parse(xhr.responseText);
        yearData = responseJson["championship_data"]

        if ("NCAA Football (M)" in yearData) {
            var ncaaf = document.getElementById("ncaaf")
            ncaaf.innerHTML = "NCAA Football (M): " + yearData["NCAA Football (M)"]
        }
        else {
            var ncaaf = document.getElementById("ncaaf")
            ncaaf.innerHTML = "NCAA Football (M): " + "None"
        }

        if ("NCAA Basketball (W)" in yearData) {
            var ncaabw = document.getElementById("ncaabw")
            ncaabw.innerHTML = "NCAA Basketball (W): " + yearData["NCAA Basketball (W)"]
        }
        else {
            var ncaabw = document.getElementById("ncaabw")
            ncaabw.innerHTML = "NCAA Basketball (W): " + "None"
        }

        if ("NCAA Basketball (M)" in yearData) {
            var ncaabm = document.getElementById("ncaabm")
            ncaabm.innerHTML = "NCAA Basketball (M): " + yearData["NCAA Basketball (M)"]
        }
        else {
            var ncaabm = document.getElementById("ncaabm")
            ncaabm.innerHTML = "NCAA Basketball (M): " + "None"
        }

        if ("MLB" in yearData) {
            var mlb = document.getElementById("mlb-list")
            mlb.innerHTML = "MLB: " + yearData["MLB"]
        }
        else {
            var mlb = document.getElementById("mlb-list")
            mlb.innerHTML = "MLB: " + "None"
        }

        if ("NFL" in yearData) {
            var nfl = document.getElementById("nfl-list")
            nfl.innerHTML = "NFL: " + yearData["NFL"]
        }
        else {
            var nfl = document.getElementById("nfl-list")
            nfl.innerHTML = "NFL: " + "None"
        }

        if ("NBA" in yearData) {
            var nba = document.getElementById("nba-list")
            nba.innerHTML = "NBA: " + yearData["NBA"]
        }
        else {
            var nba = document.getElementById("nba-list")
            nba.innerHTML = "NBA: " + "None"
        }

        if ("NHL" in yearData) {
            var nhl = document.getElementById("nhl-list")
            nhl.innerHTML = "NHL: " + yearData["NHL"]
        }
        else {
            var nhl = document.getElementById("nhl-list")
            nhl.innerHTML = "NHL: " + "None"
        }

    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }

    xhr.send(null)
}
