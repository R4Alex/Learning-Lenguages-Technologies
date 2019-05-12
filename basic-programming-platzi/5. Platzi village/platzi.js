
function random(max, min){
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}


for (var i = 0; i < 10; i++) {
  document.write(random(-5, 10) + ", ");
}

for (var i = 0; i < 10; i++) {
  document.write(random(0, 10) + ", ");

}
