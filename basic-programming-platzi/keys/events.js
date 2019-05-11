var keys = {
  LEFT: 37,
  UP: 38,
  RIGHT: 39,
  DOWN: 40,
};

console.log(keys);

document.addEventListener("keydown", keyboardDraw);

function keyboardDraw(event){

  switch(event.keyCode){
    case keys.LEFT:
      console.log("abajo");
    break;

    case keys.UP:
      console.log("abajo");
    break;

    case keys.RIGHT:
      console.log("abajo");
    break;

    case keys.DOWN:
      console.log("abajo");
    break;

  }

}
