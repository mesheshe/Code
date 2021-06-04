document.addEventListener('DOMContentLoaded', function(event){
    var req = new XMLHttpRequest();
    var payload = {};
    payload.content = "loadItAll";
    req.open("POST", '/', true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.addEventListener('load', function(){
        if (req.status >= 200 && req.status < 400){
            var response = JSON.parse(req.responseText);
            response = JSON.parse(response.results);
            for (var i = 0; i < response.length; i++){
                build(response[i]);
            }
        }else{
            console.log("Error in network request: " +req.statusText);
        }
    });
    req.send(JSON.stringify(payload));
});

var clear = document.getElementById("clearButton");
clear.addEventListener("click", function(event){
    var req = new XMLHttpRequest();
    req.open("GET", '/?clear=true', true);
    req.addEventListener('load', function(){
        if (req.status >= 200 && req.status < 400){
            var node = document.getElementById("insertHere");
            var newNode = document.createElement("tbody");
            newNode.setAttribute("id", "insertHere");
            node.parentElement.replaceChild(newNode, node);
        }else{
            console.log("Error: " + req.status);
        }
    })
    req.send(null);
});

var names = document.getElementById("name");
var reps = document.getElementById("reps");
var weight = document.getElementById("weight");
var unit = document.getElementById("lbs" );
var date = document.getElementById("date");
var submit1 = document.getElementById("submit1");

submit1.addEventListener("click", function(event){
    var req = new XMLHttpRequest();
    var payload = {};
    payload.content = "add";
    payload.name = names.value;
    payload.reps = reps.value;
    payload.weight = weight.value;
    payload.unit =  unit.checked;
    payload.date = date.value;
    payload = JSON.stringify(payload)
    req.open("POST", '/', true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.addEventListener('load', function(){
        if (req.status >= 200 && req.status < 400){
            var response = JSON.parse(req.responseText);
            response = JSON.parse(response.results);
            if (response != null){
                names.value = null;
                reps.value = null;
                weight.value = null;
                date.value = null;
                build(response);
            }
        }else{
            console.log("Error in network request: " +req.statusText);
        }
    });
    req.send(payload);
    event.preventDefault();
});

document.addEventListener("submit", function(event){
    var del_or_update = event.submitter.name;
    var id = event.target.children[0].value;
    if (del_or_update == "delete_button"){
        var  request = new XMLHttpRequest();
        var payload = {};
        payload.content = "delete";
        payload.id = id;
        request.open("POST", '/', true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.addEventListener('load', function(){
            if (request.status >= 200 && request.status < 400){
                //event.target = form <parent is> td <parent is> tr <parent is> tbody
                document.getElementById('insertHere').removeChild(event.target.parentElement.parentElement);
            }else{
                console.log("Error: " + request.status);
            }
        });
        request.send(JSON.stringify(payload));
        event.preventDefault();
    }
});

// format below that build is expecting
//{id: 18, name: "Final ", reps: 32, weight: 135, date: "2021-05-27T07:00:00.000Z", …}    
function build(response){
    var tr = document.createElement("tr");
    var hidden1 = document.createElement("input");
    hidden1.setAttribute("type", "hidden");
    hidden1.setAttribute("name", "id");
    hidden1.setAttribute("value", `${response.id}`);
    var hidden2 = hidden1.cloneNode(true);
    var names = document.createElement("td");
    names.textContent = response.name;
    var reps = document.createElement("td");
    reps.textContent = response.reps;
    var weight = document.createElement("td");
    weight.textContent = response.weight;
    var units = document.createElement("td");
    if (weight != null){
        if (response.lbs === 1){
            units.textContent = "lbs";
        }else{
            units.textContent = "kg";
        }
    }else{
        units.textContent  = null;
    }
    var aDate = response.date;
    if (aDate != null){
        aDate = aDate.substring(0,aDate.indexOf("T"));
        var month = aDate.substring(5,7);
        var day = aDate.substring(8,10);
        var year = aDate.substring(0,4);
        aDate = month + '-' + day + '-' + year;
    }
    var date = document.createElement("td");
    date.textContent = aDate;
    var input1 = document.createElement("input");
    input1.setAttribute("type", "submit");
    input1.setAttribute("name", "update_button");
    input1.setAttribute("value", "Update");
    var update = document.createElement("td");
    var form = document.createElement("form");
    form.setAttribute('method', "post")
    form.setAttribute('action', "/update")
    var form2 = form.cloneNode(false);
    form.appendChild(hidden1);
    form.appendChild(input1);
    update.appendChild(form);
    var input2 = document.createElement("input");
    input2.setAttribute("type", "submit");
    input2.setAttribute("name", "delete_button");
    input2.setAttribute("value", "Delete");
    var del = document.createElement("td");
    form2.appendChild(hidden2);
    form2.appendChild(input2);
    del.appendChild(form2);
    tr.appendChild(names);
    tr.appendChild(reps);
    tr.appendChild(weight);
    tr.appendChild(units);
    tr.appendChild(date);
    tr.appendChild(update);
    tr.appendChild(del);
    document.getElementById("insertHere").appendChild(tr);
}