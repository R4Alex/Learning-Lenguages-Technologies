/*var route = window.location;
console.log(console)
document.write("hello student</br>")
document.write("You are on: " + route)
*/

var element = document.getElementById("paint");
var context = element.getContext("2d")

context.beginPath();
context.strokeStyle = "red";
context.moveTo(100, 100);
context.lineTo(200, 200);
context.stroke();
context.closePath()

context.beginPath();
context.strokeStyle = "blue";
context.moveTo(180, 10);
context.lineTo(290, 200);
context.stroke();
context.closePath()
