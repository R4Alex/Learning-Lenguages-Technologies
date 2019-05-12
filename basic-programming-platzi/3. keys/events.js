var keys = {
  LEFT: 37,
  UP: 38,
  RIGHT: 39,
  DOWN: 40,
};

console.log(keys);

document.addEventListener("keydown", keyboardDraw);
var canva = document.getElementById("paint");
var context = canva.getContext("2d");
var x = 150;
var y = 150;
var movement = 10;

drawLine("brown", x-1, y-1, x+1, y+1, context);

function drawLine(color, x_start, y_start, x_final, y_final, context) {
  context.beginPath();
  context.strokeStyle = color;
  context.lineWidth = 3;
  context.moveTo(x_start, y_start);
  context.lineTo(x_final, y_final);
  context.stroke();
  context.closePath();
}

function keyboardDraw(event){
  var littleColor = "blue";
  switch(event.keyCode){
    case keys.LEFT:
      drawLine(littleColor, x, y, x - movement, y, context);
      x -= movement;
    break;

    case keys.UP:
      drawLine(littleColor, x, y, x, y - movement, context);
      y -= movement;
    break;

    case keys.RIGHT:
    drawLine(littleColor, x, y, x + movement, y, context);
    x += movement;
    break;

    case keys.DOWN:
      drawLine(littleColor, x, y, x, y + movement, context);
      y += movement;
    break;

    default:
    break;
  }

}
