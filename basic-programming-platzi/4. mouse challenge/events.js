function drawLine(color, x_start, y_start, x_final, y_final, context) {
  context.beginPath();
  context.strokeStyle = color;
  context.lineWidth = 3;
  context.moveTo(x_start, y_start);
  context.lineTo(x_final, y_final);
  context.stroke();
  context.closePath();
}

function drawBorder(context){
  drawLine("black", 0, 0, 0, canvas_height, context);
  drawLine("black", 0, canvas_height, canvas_height, canvas_height, context);
  drawLine("black", 0, 0, canvas_height, 0, context);
  drawLine("black", canvas_height, 0, canvas_height, canvas_height, context);
}

var canDraw = false;
function mouseDraw(event){
  if(canDraw){
      drawLine("blue", event.offsetX-1, event.offsetY-1, event.offsetX+1, event.offsetY+1, context);
  }
}

var canva = document.getElementById("paint");
var context = canva.getContext("2d");

var canvas_width = canva.width;
var canvas_height = canva.height;

drawBorder(context);


canva.addEventListener("mousemove", mouseDraw);
canva.addEventListener("mousedown", function(){canDraw = true;});
canva.addEventListener("mouseup", function(){canDraw = false;});



