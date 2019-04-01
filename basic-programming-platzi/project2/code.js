/*var route = window.location;
console.log(console)
document.write("hello student</br>")
document.write("You are on: " + route)
*/

var element = document.getElementById("paint");
var context = element.getContext("2d")


function drawLine(color, x_start, y_start, x_final, y_final) {
    context.beginPath();
    context.strokeStyle = color;
    context.moveTo(x_start, y_start);
    context.lineTo(x_final, y_final);
    context.stroke();
    context.closePath()    
}

drawLine("blue", 10, 300, 220, 10)
drawLine("yellow", 310, 10, 10, 220)