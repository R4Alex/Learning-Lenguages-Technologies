
var element = document.getElementById("paint");
var context = element.getContext("2d")
var lines = 30;
var l = 0;

function drawLine(color, x_start, y_start, x_final, y_final) {
    context.beginPath();
    context.strokeStyle = color;
    context.moveTo(x_start, y_start);
    context.lineTo(x_final, y_final);
    context.stroke();
    context.closePath();
}

//while (l < lines) {
for (l = 0; l < lines; l++) {
    y_start = 10 * l;
    x_final = 10 * (l + 1);
    drawLine("#AAF", 0, y_start, x_final, 300);
}

drawLine("black", 1, 1, 1, 299);
drawLine("black", 1, 299, 299, 299);
