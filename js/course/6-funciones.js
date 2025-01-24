/***** FUNCIONES *****/

// Funcion simple

myFunc()

function myFunc() {
    console.log('Hola desde funcion!')
}

myFunc()

// Funcion con parametros

function myFuncWithParams(name) {
    console.log(`Hola ${name}!`)
}

myFuncWithParams('Antonio')

// Funcion anonima

const myAnonymousFunc = function (name) {
    console.log(`Hola ${name}!`)
}

myAnonymousFunc('Anonimo')

// Funcion arrow (sintaxis simplificada, para una sola linea)

const myArrowFunc = (name) => {
    console.log(`Hola ${name}!`)
}

myArrowFunc('Arrow')

// Parametros por defecto

function sum(a, b) {
    return a + b
}

function sum(a = 0, b = 0) {
    console.log(a + b)
}

sum(5, 10)
sum(5)
sum()
sum(b = 3)

// Retorno de valores

function mult(a = 1, b = 1) {
    return a * b
}

console.log(mult(2, 3))
console.log(mult(b = 2))
console.log(mult(a = 7))

// Funciones anidadas

function extern() {
    console.log('Funcion externa')
    intern()
    function intern() {
        console.log('Funcion interna')
    }
}

extern()
// intern() ERROR! --> fuera de scope

// Funciones de orden superior (reciben funciones como args)

function applyFunc(func, param) {
    func(param)
}

applyFunc(myArrowFunc, 'orden superior')

// Funcion para iterar: forEach

myArray = [1, 2, 3, 4]

myArray.forEach((value) => console.log(value))

myArray.forEach(function (value) {
    console.log(value + 10)
})

myMap = new Map([
    ['a', 1],
    ['b', 2],
    ['c', 3]
])

myMap.forEach((value, key) => console.log(key, value))
