var newLobbyButton = document.getElementById("newLobbyButton");
var joinButton = document.getElementById("joinButton");
var lobbyNumber = document.getElementById("lobbyNumber");
var changeClass = function(){
    // Get the HTML element using its id
    var para = document.getElementById("exampleText");

    // Toggle turns the class off if it's there, and
    // turns it on if it's not.''
    para.classList.toggle("isGreen");
    para.classList.toggle("normal");

    // innerText gets the text inside the element
    para.innerText = "Switched!";
}


// Make changeClass run every time the button with id="test" is clicked
var button = document.getElementById("test");
button.addEventListener("click", changeClass);