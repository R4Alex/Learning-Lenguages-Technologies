for(var i=0; i <= 100; i++){
    if(isDivisible(i, 3)){
        document.write("Fizz ");
    }

    if(isDivisible(i, 5)){
        document.write("Buzz");
    }

    if(!isDivisible(i, 3) && !isDivisible(i, 5)){
        document.write(i);
    }

    document.write("<br/>");    
}

function isDivisible(num, divisor){
    if(num % divisor ==0){
        return true;
    } else {
        return false;
    }
}
