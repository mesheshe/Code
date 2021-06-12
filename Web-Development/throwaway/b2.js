document.addEventListener('DOMContentLoaded', bindButton());
function bindButton(){
    // piggy back of this function to do work on elements
    var zipInput = document.getElementById("zip");
    var cityInput = document.getElementById("city");
    var stateInput = document.getElementById("state");
    var apiKey = 'fa7d80c48643dfadde2cced1b1be6ca1';
    zipInput.addEventListener("input", function(){
        if (zipInput.value != "" && stateInput.value == ""){
            stateInput.setAttribute("readonly", "readonly");
            cityInput.setAttribute("readonly", "readonly");
        }else{
            stateInput.removeAttribute("readonly")
            cityInput.removeAttribute("readonly")
        }
    })
    stateInput.addEventListener("input", function(){
        if (stateInput.value != "" && zipInput.value == ""){
            zipInput.setAttribute("readonly", "readonly");
        }else{
            zipInput.value = "";
        }
    })
    cityInput.addEventListener("input", function(){
        if (cityInput.value != "" && zipInput == ""){
            zipInput.setAttribute("readonly", "readonly");
        }else{
            zipInput.value = "";
        }
    })
    document.addEventListener("submit", function(event){ 
        event.preventDefault();
        var req = new XMLHttpRequest();
        if (zipInput.value == "" && stateInput.value != ""){
            req.open("GET",`http://api.openweathermap.org/data/2.5/weather?q=${cityInput.value},${stateInput.value},us&units=metric,&appid=${apiKey}`,true);
        }else if (zipInput.value != ""){
            req.open("GET",`http://api.openweathermap.org/data/2.5/weather?q=${zipInput.value},us&units=metric&appid=${apiKey}`,true);
        }else{
            req.open("GET",`http://api.openweathermap.org/data/2.5/weather?q=Error404&appid=${apiKey}`,true);
            // intentionally doing this so it parses 404 and the code below can still execute
        }
        req.addEventListener("load", function(){
            var returnResponse = JSON.parse(req.responseText);
            var cityOutput = document.getElementById("outputCity");
            var tempOutput = document.getElementById("outputTemp");
            var humidOutput = document.getElementById("outputHumid");
            if (returnResponse["cod"] < 400){
                cityOutput.textContent = returnResponse["name"];
                if (returnResponse["main"]["temp"] > 273.15){
                    returnResponse["main"]["temp"] -= 273.15 
                }
                tempOutput.textContent = Math.round(returnResponse["main"]["temp"]);
                humidOutput.textContent = returnResponse["main"]["humidity"];
            }else{
                cityOutput.textContent = "";
                tempOutput.textContent = "";
                humidOutput.textContent = "";
            }
            event.preventDefault();
            zipInput.value = "";
            cityInput.value = "";
            stateInput.value = "";
            zipInput.removeAttribute("readonly");
            cityInput.removeAttribute("readonly");
            stateInput.removeAttribute("readonly");
        });
        req.send(null);
    })
}

 
function aaa(){
    return 
    {
        test:1
    };
}

alert(typeof aaa());