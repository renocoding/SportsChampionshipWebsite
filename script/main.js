console.log('page load - entered main.js for js-other api');

var sendButton1 = document.getElementById('send-button1');
//sendButton1.onmouseup = getYearInfo;

var sendButton2 = document.getElementById('send-button2');
//sendButton2.onmouseup = getCityInfo;

url = "http://localhost:51081"


// UPDATE YEAR SELECT
// info on adding optionss from stackoverflow
var yearSelect = document.getElementById("select-year");

for (i = 1941; i < 2019; i++)
{
    // add year to select
    var option = document.createElement("option");
    option.value = i - 1940;
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

    responseJson = JSON.parse(xhr.responseText);
    console.log(responseJson["cities"][1])

    // print cities using get
    var i = 0
    for (city in responseJson["cities"])
    {
        // add metro area to select
        var option = document.createElement("option");
        option.value = i;
        option.innerHTML = responseJson["cities"][i];
        citySelect.appendChild(option)
        i++;
    }


}

// set up onerror
xhr.onerror = function(e) { // triggered when error response is received and must be before send
    console.error(xhr.statusText);
}

function getYearInfo(){
    console.log('entered getYearInfo!');
}

function updateYearData(year){
    // make reqeust to get_index of cities endpoint
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url + "/years/" + year, true);
    xhr.send(null)

    // set up onload
    xhr.onload = function(e) { // triggered when response is received

        // must be written before send
        console.log(xhr.responseText);

        // update year champ data
        responseJson = JSON.parse(xhr.responseText);
        yearData = responseJson["championship_data"]

        if ("NCAA Football (M)" in yearData) {
            var ncaaf = document.getElementById("ncaaf")
            ncaaf.innerHTML += " " + yearData["NCAA Football (M)"]
        }
        if ("NCAA Basketball (W)" in yearData) {
            var ncaabw = document.getElementById("ncaabw")
            ncaaf.innerHTML += " " + yearData["NCAA Basket (W)"]
        }
        else {
            var ncaabw = document.getElementById("ncaabw")
            ncaabw.innerHTML += " " + "None"
        }


    }

    // set up onerror
    xhr.onerror = function(e) { // triggered when error response is received and must be before send
        console.error(xhr.statusText);
    }
}
