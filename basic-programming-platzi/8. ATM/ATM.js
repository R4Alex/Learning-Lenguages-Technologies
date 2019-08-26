class Cash {
    constructor(value, quantity){
        this.value = value;
        this.quantity = quantity;
    }
 }

function giveMoney(){
    money = document.getElementById("money").value;
    money = parseInt(money);

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
        result.innerHTML = "sorry I cant give you that money";
    } else{
        for(var e of given){
            if(e.quantity > 0){
                result.innerHTML += e.quantity + " of $" + e.value + "<br />"
            }
        }
    }
}

var box = [];
var given = [];
box.push(new Cash(100, 5));
box.push(new Cash(50, 10));
box.push(new Cash(20, 5));
box.push(new Cash(10, 10));
box.push(new Cash(5, 5));

var money = 1000;
var div = 0;
var papers = 0;

var result = document.getElementById("result");
var button = document.getElementById("extract");
button.addEventListener("click", giveMoney)

