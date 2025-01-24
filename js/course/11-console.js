/****** CONSOLE METHODS *****/

// log

console.log('¡Hola, mundo!')

// error

console.error('¡Error, mundo!', new Error('Conexión fallida'))

// warn

console.warn('¡Advertencia, mundo!')

// info

console.info('¡Info, mundo!')

// table

let data = [
    { name: 'Antonio', age: 26 },
    { name: 'Martha', age: 26 },
    { name: 'John', age: 26 },
]

console.table(data)

// group

console.group('Usuarios')
console.log('Nombre: Antonio')
console.log('Edad: 26')

console.group('Mails')
console.log('mail.mail@mail.net')
console.log('mail2.mail2.@mail.net')

console.groupEnd()

// time

console.time('Tiempo1')

for (let i = 0; i < 1000000; i++);

console.timeEnd('Tiempo1')


console.time('Tiempo2')

for (let i = 0; i < 100000000; i++);

console.time('Tiempo3')

for (let i = 0; i < 10000000; i++);

console.timeEnd('Tiempo2')
console.timeEnd('Tiempo3')

// assert

let age = 17

console.assert(age >= 18, 'No es mayor de edad')

// count

console.count('Click')
console.count('Click')
console.countReset('Click')
console.count('Click')

// trace

function funcA() {
    funcB()
}

function funcB() {
    console.trace('Seguimiento de la ejecucion')
}

funcA()

// clear

// console.clear() --> LIMPIA LOS OUTPUTS ANTERIORES