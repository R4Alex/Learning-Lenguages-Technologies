
function random(max, min) {
	return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function paint(){
	if(background.isLoaded){
		context.drawImage(background.image, 0, 0);
	}
	if(cow.isLoaded){
		for(var i=0; i < cow.positionsX.length; i++){
			var x = cow.positionsX[i];
			var y = cow.positionsY[i];
			context.drawImage(cow.image, x, y);
		}
	}
	if(rooster.isLoaded){
		for(var i=0; i < rooster.positionsX.length; i++){
			var x = rooster.positionsX[i];
			var y = rooster.positionsY[i];
			context.drawImage(rooster.image, x, y);
		}
	}
	if(pig.isLoaded){
		for(var i=0; i < pig.positionsX.length; i++){
			var x = pig.positionsX[i];
			var y = pig.positionsY[i];
			context.drawImage(pig.image, x, y);
		}
	}

	if(wolf.isLoaded){
		context.drawImage(wolf.image, wolf.positionX, wolf.positionY);
	}
}

function loadBackground(){
	background.isLoaded = true;
	paint();
}

function loadCows(){
	cow.isLoaded = true;
	paint();
}

function loadRoosters(){
	rooster.isLoaded = true;
	paint();
}

function loadPigs(){
	pig.isLoaded = true;
	paint();
}

function loadWolf(){
	wolf.isLoaded = true
	paint();
}

var keys = {
	LEFT: 37,
	UP: 38,
	RIGHT: 39,
	DOWN: 40,
};

document.addEventListener("keyup", keyboardDraw);
var vp = document.getElementById("platzivillage");
var context = vp.getContext("2d");



var background = {
	url: "tile.png",
	isLoaded: false
};

var cow = {
	url: "cow.png",
	isLoaded: false,
	quantity: random(3, 7),
	positionsX: [],
	positionsY: [],
}

var rooster = {
	url: "rooster.png",
	isLoaded: false,
	quantity: random(3, 7),
	positionsX: [],
	positionsY: [],
}

var pig = {
	url: "pig.png",
	isLoaded: false,
	quantity: random(3, 7),
	positionsX: [],
	positionsY: [],
}

var wolf = {
	url: "wolf.png",
	isLoaded: false,
	positionX: 0,
	positionY: 0,
	movement: 50
}

for (var i=0; i < cow.quantity; i++){
	var x = random(0, 420);
	cow.positionsX.push(x);
	var y = random(0, 420);
	cow.positionsY.push(y);
}

for (var i=0; i < rooster.quantity; i++){
	var x = random(0, 420);
	rooster.positionsX.push(x);
	var y = random(0, 420);
	rooster.positionsY.push(y);
}

for (var i=0; i < pig.quantity; i++){
	var x = random(0, 420);
	pig.positionsX.push(x);
	var y = random(0, 420);
	pig.positionsY.push(y);
}

background.image = new Image();
background.image.src = background.url;
background.image.addEventListener("load", loadBackground);

cow.image = new Image();
cow.image.src = cow.url;
cow.image.addEventListener("load", loadCows);


rooster.image = new Image();
rooster.image.src = rooster.url;
rooster.image.addEventListener("load", loadRoosters);


pig.image = new Image();
pig.image.src = pig.url;
pig.image.addEventListener("load", loadPigs);


wolf.image = new Image();
wolf.image.src = wolf.url;
wolf.image.addEventListener("load", loadWolf);


function keyboardDraw(event){
	switch(event.keyCode){
		case keys.LEFT:
			wolf.positionX -= wolf.movement;
			paint();
		break;

	  	case keys.UP:
			wolf.positionY -= wolf.movement;
			paint();
	  	break;
  
		case keys.RIGHT:
			wolf.positionX += wolf.movement;
			paint();  
		break;
  
		case keys.DOWN:	
	  		wolf.positionY += wolf.movement;
			paint();
		break;

		default:
		break;
	}
}
