
var mypaint = document.getElementById("paint");
var context = mypaint.getContext("2d");
var text = document.getElementById("text_lines");

var mybutton = document.getElementById("button1");
mybutton.addEventListener("click", drawByClick);

var canvas_width = mypaint.width;
var canvas_height = mypaint.height;

function drawLine(color, x_start, y_start, x_final, y_final) {
    context.beginPath();
    context.strokeStyle = color;
    context.lineWidth = 0.5;
    context.moveTo(x_start, y_start);
    context.lineTo(x_final, y_final);
    context.stroke();
    context.closePath();
}

function drawByClick() {
    var lines = parseInt(text.value);
    var l;
    var mycolor = "blue";
    var space = canvas_width / lines;

    for (l = 0; l < lines; l++) {
        y_start = space * l;
        x_final = space * (l + 1);
        drawLine(mycolor, 0, y_start, x_final, canvas_height);
    }
    
    for (l = 0; l < lines; l++) {
        y_start = space * l;
        x_final = space * (l + 1);
        drawLine(mycolor, canvas_height, y_start, x_final, 0);
    }
    
    for (l = 0; l < lines; l++) {
        y_start = space * l;
        x_final = canvas_height - (space * (l + 1));
        drawLine(mycolor, canvas_height, y_start, x_final, canvas_height);
    }
    
    for (l = 0; l < lines; l++) {
        y_start = canvas_height - (space * l);
        x_final = space * (l + 1);
        drawLine(mycolor, 0, y_start, x_final, 0);
    }
}

// Border
drawLine("black", 0, 0, 0, canvas_height);
drawLine("black", 0, canvas_height, canvas_height, canvas_height);
drawLine("black", 0, 0, canvas_height, 0);
drawLine("black", canvas_height, 0, canvas_height, canvas_height);
