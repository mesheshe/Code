function showCarousel(num = 0){
    var caro = document.getElementsByClassName("carouselContent");
    caro = Array.from(caro);
    var dots = document.getElementsByClassName("carouselTracker");
    dots = Array.from(dots);
    var imgsource = document.getElementsByClassName("imgsource")
    imgsource = Array.from(imgsource)
    caro.forEach(x => x.style.display = "None");
    dots.forEach(x => x.style.color = "lightgrey");
    imgsource.forEach(x => x.style.display = "None")
    caro[num].style.display = "block";
    dots[num].style.color = "grey";
    imgsource[num].style.display = "";
    setTimeout(function(n, len){
        if (n + 1 === len){
            return function(){
                showCarousel()
            }
        }else{
            return function(){
                showCarousel(n+1)}
            }     
        }(num, caro.length), 2000)
}
var left = document.getElementById("left");
var right = document.getElementById("right");
var dots = document.getElementsByClassName("carouselTracker");
for (var i = 0; i < dots.length; i++){
    dots[i].addEventListener("click", function(j){
        return function(){
            var id = window.setTimeout(function() {}, 0);
            while (id--) {
                window.clearTimeout(id); // will do nothing if no timeout with id is present
            }
            showCarousel(j);
        }
    }(i));
}
var leftCont = document.getElementById("leftCont");
left.addEventListener("mouseover", function(){
    leftCont.style.border = "2px solid black";
    leftCont.style.backgroundColor = "black";
});
left.addEventListener("mouseleave", function(){
    leftCont.style.border = "";
    leftCont.style.backgroundColor = "";
});
left.addEventListener("click", function(){
    var caro = document.getElementsByClassName("carouselContent");
    caro = Array.from(caro);
    var num = -1;
    for (var i = 0; i < caro.length; i++){
        if (caro[i].style.display === "block"){
            num = i;
        }
    }
    if (num === -1){
        num = 0;
    }else if (num === 0){
        num = caro.length - 1
    }else{num--;}
    var id = window.setTimeout(function() {}, 0);
    while (id--) {
        window.clearTimeout(id); // will do nothing if no timeout with id is present
    }
    showCarousel(num);
});
var rightCont = document.getElementById("rightCont");
right.addEventListener("mouseover", function(){
    rightCont.style.border = "2px solid black";
    rightCont.style.backgroundColor = "black";
});
right.addEventListener("mouseleave", function(){
    rightCont.style.border = "";
    rightCont.style.backgroundColor = "";
});
right.addEventListener("click", function(){
    var caro = document.getElementsByClassName("carouselContent");
    caro = Array.from(caro);
    var num = -1;
    for (var i = 0; i < caro.length; i++){
        if (caro[i].style.display === "block"){
            num = i;
        }
    }
    if (num === -1 || num === caro.length - 1){
        num = 0;
    }else{num++;}
    var id = window.setTimeout(function() {}, 0);
    while (id--) {
        window.clearTimeout(id); // will do nothing if no timeout with id is present
    }
    showCarousel(num);
});
document.addEventListener("visibilitychange", function(){
    /*
     this function will pause the animation if user is not viewing the page
     In order to do this, it is a two step process. 
     First step is to save the current position, and that is done by
     checking if for all possible screens in carousel, if the current 
     screen is a block, if so, save the index. 
     Second step is to pause the screen and that is done by using the 
     visibiltyState event, and when it is not visible, all timers 
     are cleared, and the screen "pauses". 
     Once user is viewing the screen, the function showCarousel is called
     with the current index
    */
     if (document.visibilityState !== 'visible'){
        var id = window.setTimeout(function() {}, 0);
        while (id--){  // not all browswer see if(0) as false 
            window.clearTimeout(id); 
        }
    }else{
        var caro = document.getElementsByClassName("carouselContent");
        caro = Array.from(caro);
        var num = -1;
        for (var i = 0; i < caro.length; i++){
            if (caro[i].style.display === "block"){
                num = i;
            }
        }
        if (num === -1){
            num = 0;
        }
        showCarousel(num);
    }
});
var s = true
if (s){
    showCarousel();
    s = false;
}
