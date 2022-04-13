console.log("Fibonacci numbers");

let a = 0;
let b = 1;
let aux = 0;

for(let i = 0; i < 30; i++) {
  console.log(b);
  aux = a;
  a = b;
  b = aux + b;
}
