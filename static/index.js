var home = document.getElementById("home")
home.addEventListener("click", function(){
    home.classList.remove("past");
    home.classList.add("current");
})