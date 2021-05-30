var names = document.getElementById("name");
var reps = document.getElementById("reps");
var weight = document.getElementById("weight");
var unit = document.getElementById("lbs" );
var date = document.getElementById("date");
var id = document.getElementById('id');
var update = document.getElementById('submit1');
update.addEventListener('click', function(event){
    var req = new XMLHttpRequest();
    var payload = {}
    payload.content = 'update';
    payload.name = names.value;
    payload.reps = reps.value;
    payload.weight = weight.value;
    payload.unit =  unit.checked;
    payload.date = date.value;
    payload.id = id.value;
    req.open('POST', '/', true);
    req.setRequestHeader('Content-Type', 'application/json');
    req.addEventListener('load', function(){
        if (req.status >= 200 && req.status < 400){
            console.log('Updated')
        }else{
            console.log('Error')
        }
    })
    req.send(JSON.stringify(payload));
});