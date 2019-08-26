class Pakiman {
    constructor(name, hp, attack){
        this.name = name;
        this.hp = hp;
        this.attack = attack;
        this.image = new Image();
        this.image.src = images[this.name];
    }

    talk(){
        alert(this.name);
    }

    show(){
        document.write("<p>");
        document.body.appendChild(this.image);
        document.write("<strong>"+ this.name + "</strong><br />");
        document.write("Hp: " + this.hp + "<br />");
        document.write("Attack: " + this.attack + "<br />");
        document.write("</p><hr />");
    }
}