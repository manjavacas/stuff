import { add, PI, Circle } from "./12-export-modulos.mjs"

import foo from "./12-export-modulos.mjs"

console.log(add(5, 10))

console.log(add(PI, 1))

// Default
// console.log(substract(10,8))
console.log(foo(10, 8))

let circ = new Circle(3)
console.log(circ.area().toFixed(4))
console.log(circ.perim().toFixed(4))

// Proyecto modular
// import { Whatever } from "./classes/wtf.js"