var button = document.getElementById("butt");
var div = document.getElementById("scrollboxCont");

button.addEventListener("click", function(){
    div.style.display = "block";
    button.style.display = "none";
    div.scrollIntoView({behavior: "smooth"});
})