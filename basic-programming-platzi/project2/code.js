var element = document.getElementById("paint");
var context = element.getContext("2d")
var lines = 60;
var l = 0;
var mycolor = "blue";

function drawLine(color, x_start, y_start, x_final, y_final) {
    context.beginPath();
    context.strokeStyle = color;
    context.lineWidth = 0.5;
    context.moveTo(x_start, y_start);
    context.lineTo(x_final, y_final);
    context.stroke();
    context.closePath();
}

for (l = 0; l < lines; l++) {
    y_start = 10 * l;
    x_final = 10 * (l + 1);
    drawLine(mycolor, 0, y_start, x_final, 600);
}

for (l = 0; l < lines; l++) {
    y_start = 10 * l;
    x_final = 10 * (l + 1);
    drawLine(mycolor, 600, y_start, x_final, 0);
}

for (l = 0; l < lines; l++) {
    y_start = 10 * l;
    x_final = 600 - (10 * (l + 1));
    drawLine(mycolor, 600, y_start, x_final, 600);
}

for (l = 0; l < lines; l++) {
    y_start = 600- (10 * l);
    x_final = 10 * (l + 1);
    drawLine(mycolor, 0, y_start, x_final, 0);
}


// Border
drawLine("black", 1, 1, 1, 600);
drawLine("black", 1, 600, 600, 600);
drawLine("black", 1, 1, 600, 1);
drawLine("black", 600, 1, 600, 600);
