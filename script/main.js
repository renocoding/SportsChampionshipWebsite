console.log('page load - entered main.js for js-other api');

var sendButton1 = document.getElementById('send-button1');
//sendButton1.onmouseup = getYearInfo;

var sendButton2 = document.getElementById('send-button2');
//sendButton2.onmouseup = getCityInfo;



// Update Year Select -> info on adding opts from stackoverflow
var yearSelect = document.getElementById("select-year");

for (i = 1941; i < 2019; i++)
{
    // add year to select
    var option = document.createElement("option");
    option.value = i - 1940;
    option.innerHTML = i;
    yearSelect.appendChild(option)
}

// Update City Select
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://localhost/cities/", true);
xhr.send(null)

// set up onload
xhr.onload = function(e) { // triggered when response is received
    // must be written before send
    console.log(xhr.responseText);

    // update city select
    var citySelect = document.getElementById("select-city");

    responseJson = JSON.parse(responseText);

    // info on json iteration from https://stackoverflow.com/questions/684672/how-do-i-loop-through-or-enumerate-a-javascript-object
    var i = 0
    for (var key of Object.keys(responseJson))
    {
        // add metro area to select
        var option = document.createElement("option");
        option.value = i;
        option.innerHTML = key;
        yearSelect.appendChild(option)
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
