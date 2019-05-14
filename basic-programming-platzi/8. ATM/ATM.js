class Cash {
    constructor(value, quantity){
        this.value = value;
        this.quantity = quantity;
    }
 }

function giveMoney(){
    for(var cash of box){
        if(money > 0){
            div = Math.floor(money / cash.value);
            if(div > cash.quantity){
                papers = cash.quantity;
            } else {
                papers = div;
            }
            
            given.push(new Cash(cash.value, papers));
            money = money - (cash.value*papers);
        }
    }

    if(money > 0){
        console.log("sorry I cant give you that money");
    } else{
        console.log(given);
    }
}

var box = [];
var given = [];
box.push(new Cash(50, 3));
box.push(new Cash(20, 2));
box.push(new Cash(10, 2));

var money = 1000;
var div = 0;
var papers = 0;

var button = document.getElementById("extract");
button.addEventListener("click", giveMoney)

