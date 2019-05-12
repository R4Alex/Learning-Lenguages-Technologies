
function random(max, min) {
	return Math.floor(Math.random() * (max - min + 1) ) + min;
}

function paint(){
	if(background.isLoaded){
		context.drawImage(background.image, 0, 0);
	}
	if(cow.isLoaded){
		var quantity = random(5, 10);
		for(var i=0; i < quantity; i++){
			var x = random(0, 420);
			var y = random(0, 420);
			context.drawImage(cow.image, x, y);
		}
	}
	if(rooster.isLoaded){
		var quantity = random(5, 10);
		for(var i=0; i < quantity; i++){
			var x = random(0, 420);
			var y = random(0, 420);
			context.drawImage(rooster.image, x, y);
		}
	}
	if(pig.isLoaded){
		var quantity = random(5, 10);
		for(var i=0; i < quantity; i++){
			var x = random(0, 420);
			var y = random(0, 420);
			context.drawImage(pig.image, x, y);
		}
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

var vp = document.getElementById("platzivillage");
var context = vp.getContext("2d");


var background = {
	url: "tile.png",
	isLoaded: false
};

var cow = {
	url: "cow.png",
	isLoaded: false
}

var rooster = {
	url: "rooster.png",
	isLoaded: false
}

var pig = {
	url: "pig.png",
	isLoaded: false
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
