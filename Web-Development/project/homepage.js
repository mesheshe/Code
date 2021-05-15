function showCarousel(num = 0){
    var caro = document.getElementsByClassName("carouselContent");
    caro = Array.from(caro);
    var dots = document.getElementsByClassName("carouselTracker");
    dots = Array.from(dots);
    caro.forEach(x => x.style.display = "None");
    dots.forEach(x => x.style.color = "lightgrey");
    caro[num].style.display = "block";
    dots[num].style.color = "grey";
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
var left = document.getElementsByClassName("left");
var right = document.getElementsByClassName("right");
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

left[0].addEventListener("click", function(){
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
right[0].addEventListener("click", function(){
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
    if (document.visibilityState !== 'visible'){
        var id = window.setTimeout(function() {}, 0);
        while (id--){  // not all browswer see if(0) as false 
            window.clearTimeout(id); 
        }
    }else{
        showCarousel(num);
    }
});
var s = true
if (s){
    showCarousel();
    s = false;
}