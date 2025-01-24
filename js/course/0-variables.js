/******** HOLA MUNDO ********/

console.log("Hola mundo!")
// console.log('Hola mundo!')
// console.log(`Hola mundo!`)

/******** VARIABLES ********/

// var (no utilizar)
var x = 5
console.log('Variable x =', x)
x++
console.log('Variable x =', x)

// let
let y = 6
console.log('Variable y =', y)
y++;
console.log('Variable y =', y)

// const
const z = 7
// z++; --> ERROR
console.log('Constante z =', z)

/******** TIPOS DE DATOS ********/

// String
let nombre = 'Antonio'

// Enteros, decimales
let edad = 26
let altura = 1.75

// Booleanos
let hombre = true
console.log(hombre)

// Undefined (valor no inicializado)
let undefinedValue
console.log(undefinedValue)

// Null (valor nulo)
let nullValue = null
console.log(nullValue)

// Symbol (valores unicos)
let mySymbol = Symbol("symbol")
console.log(mySymbol)

// BigInt
let myBigInt = BigInt(328238238923832938928322)
let myBigInt2 = 38389238293829382983293298329n
console.log(myBigInt)
console.log(myBigInt2)

// Mostrar tipo de dato
console.log(typeof nombre)
console.log(typeof edad)

let h = typeof nombre
console.log(h + '!')

console.log(typeof nullValue)