// This is a JS comment. I'll discuss what I did in these.'
var changeClass = function(){
    // Get the HTML element using its id
    var para = document.getElementById("exampleText");

    // Toggle turns the class off if it's there, and
    // turns it on if it's not.''
    para.classList.toggle("isGreen");

    // innerText gets the text inside the element
    para.innerText = "Switched!";
}

// Make changeClass run every time the button with id="test" is clicked
var button = document.getElementById("test");
button.addEventListener("click", changeClass);