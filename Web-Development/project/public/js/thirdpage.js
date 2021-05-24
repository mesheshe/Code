var submit = document.getElementById("textAreaSubmit");
submit.addEventListener("click", function(event){
    var node = document.getElementById("textArea");
    var nameNode = document.getElementById("name")
    var req = new XMLHttpRequest();
    var payload = {comment:null, name:null};
    if (node.value != null){
        payload.comment = node.value;
    }
    if (nameNode.value != null){
        payload.name = nameNode.value;
    }
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
    commentContainer.textContent = str.comment || "I <3 Space.";

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


    
    
    
 