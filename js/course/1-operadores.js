/***** OPERADORES ARITMETICOS ****/

let a = 5
let b = 10

console.log(a + b)
console.log(a - b)
console.log(a * b)
console.log(a / b)
console.log(a % b)
console.log(a ** b)

a++
console.log(a)

b--
console.log(b)

/***** OPERADORES DE ASIGNACION ****/

let variable = 2
console.log(variable)
variable += 1
console.log(variable)

console.log('-----------------')

/***** OPERADORES DE COMPARACION ****/

let x = 1
let y = 2

console.log(x > y)
console.log(x <= y)
console.log(x == y)

// Igualdad por valor
console.log(x == 1) // true
console.log(x == '1') // true

// Igualdad por identidad (tipo + valor)
console.log(x === 1) // true
console.log(x === '1') // false

// Similar para desigualdad...
console.log(x != '1') // false
console.log(x !== '1') // true

// Truthy y falsy values
console.log(0 == false)
console.log(1 == true)
console.log(2 == false)
console.log(1 === true)
console.log(0 == '')
console.log(0 == ' ')
console.log(0 == 'Hola')
console.log(0 === '')
console.log(undefined == null)
console.log(undefined === null)

/* Truthy values:
    1. numeros positivos y negativos (excepto 0)
    2. cadenas de texto no vacias
    3. boolean true
*/

/* Falsy values:
    1. numero 0
    2. numero 0n
    2. null
    3. undefined
    4. boolean false
    5. cadenas vacias
    6. NaN
*/

console.log('-----------------')

/***** OPERADORES LOGICOS ****/

let p = true
let q = false

console.log(p && q)
console.log(p || q)
console.log(!p)

console.log(p && 0)
console.log(p || 0)

console.log('-----------------')

/***** OPERADORES TERNARIOS ****/

const isRaining = true
const soleado = false

isRaining ? console.log('Llueve') : console.log('No llueve')

soleado ? console.log('Soleado') : console.log('Nublado')