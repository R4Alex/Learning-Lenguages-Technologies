var images = [];
images["Cauchin"] = "cow.png";
images["Pokacho"] = "rooster.png";
images["Baconauro"] = "pig.png";

/*
var cauchin = new Pakiman("Cauchin", 100, 30);
var pokacho = new Pakiman("Pokacho", 80, 50);
var baconauro = new Pakiman("Baconauro", 120, 40);


var collection = [];
collection.push(cauchin);
collection.push(pokacho);
collection.push(baconauro);
*/

var collection = [];
collection.push(new Pakiman("Cauchin", 100, 30));
collection.push(new Pakiman("Pokacho", 80, 50));
collection.push(new Pakiman("Baconauro", 120, 40));

/*
for (var i = 0; i <= collection.length; i++){
    collection[i].show();
}
*/

/*
for (var pakiman in collection){
    collection[pakiman].show();
}
*/

for (var pakiman of collection){
    pakiman.show();
}
