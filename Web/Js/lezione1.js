const arr1 = [1,2,3];
console.log(arr1,...arr1);
const arr2 = [...arr1];
arr1.push(4);

arr1.unshift(0);

console.log(arr1);
console.log(arr2);

const prof = {
    "first name":"Godwayne",
    cognome: "Rasalan",
    età: 25,
    indirizzo:{
        citta:"Roma",
        via:"Cesare Pavese"
    }
}

console.log(prof.indirizzo.via)


const prof1=new Object();
prof1.cognome="Rasalan";
prof1.nome="Godwayne";
console.log(prof1);


function persona(){
    this.nome="";
    this.cognome="";
}



const godwayne=new persona();


console.log();

function Array(){
    console.log("pippo");
}

const arr3=new Array(1,2,3);

console.log(arr3)



for (let i=0;i<4;i++){
    console.log(i)
}

//console.log(1)

{
let ab="33";
console.log(ab)
}