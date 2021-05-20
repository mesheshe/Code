var submit = document.getElementById("textAreaSubmit");
submit.addEventListener("click", function(event){
    var node = document.getElementById("textArea");
    var req = new XMLHttpRequest();
    var payload = {comment:null};
    payload.comment = node.value;
    req.open("POST","/third-page",true);
    req.setRequestHeader("Content-Type","application/json")
    req.addEventListener("load", function(){
        document.getElementById("textArea").value = null;
        if (req.status >= 200 && req.status < 400){
            var response = JSON.parse(req.responseText);
            addComment(response);
        }else{
            alert("Error: Invalid Submission")
        }
    })
    req.send(JSON.stringify(payload));
    event.preventDefault();
})

function addComment(str){
    var commentbox = document.createElement("div");
    var profilepic = document.createElement("span");
    var image = document.createElement("img");
    var username  = document.createElement("span");
    var commentContainer = document.createElement("div");

    commentbox.setAttribute("class", "commentbox");
    profilepic.setAttribute("class","profilepic");
    username.setAttribute("class", "username");
    commentContainer.setAttribute("class","commentContainer");
    
    image.src = "/other/Profilepic.png";
    profilepic.appendChild(image);
    username.textContent = (str.name || "Anon") + ":";

    commentContainer.textContent = str.comment;

    commentbox.appendChild(commentContainer);
    commentbox.insertBefore(username, commentbox.firstChild)
    commentbox.insertBefore(profilepic, commentbox.firstChild);
    
    var h = document.getElementById("putCommentsHere");
    if (h.children.length > 1){
        h.insertBefore(commentbox, h.firstChild);
    }else{
        document.getElementById("putCommentsHere").appendChild(commentbox);
    }
}


    
    
    
    
    
    /*
    var t = document.createElement("span");
    t.textContent = node.value;
    node.value = null;
    console.log(t.textContent);
    document.getElementById("putCommentsHere").appendChild(t);
    event.preventDefault();
    */



/*
function button(){
    var apiKey = 'fa7d80c48643dfadde2cced1b1be6ca1';
    var cityZipInput = document.getElementById("cityOrZipInput");
    var countryInput = document.getElementById("countryInput");    
    var button1 = document.getElementById("form1Submit");
    var button2 = document.getElementById("form2Submit");
    button2.addEventListener("click", function(event){
        var req = new XMLHttpRequest();
        var payload = {value:null};
        payload.value = document.getElementById("textArea").value;
        req.open("POST","http://httpbin.org/post",true);
        req.setRequestHeader("Content-Type","application/json")
        req.addEventListener("load", function(){
            document.getElementById("textArea").value = null;
            document.getElementById("textArea").setAttribute("placeholder", "Enter Text Here...");
            if (req.status >= 200 && req.status < 400){
                var response = JSON.parse(req.responseText);
                var newResponse = JSON.parse(response["data"]);
                document.getElementById("textOutput").textContent = newResponse["value"];
            }else{
                alert("Error: Invalid Submission - Form 2")
            }
        })
        req.send(JSON.stringify(payload));
        event.preventDefault();
    })
*/