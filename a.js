console.log("Fibonacci numbers");

let a = 1;
let b = 1;
let aux = 0;
for(let i = 0; i < 50; i++) {
  console.log(a+b);
  aux = a;
  a = b;
  b = aux + b;
}
