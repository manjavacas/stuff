/***** STRINGS ****/

// Concatenacion
let nombre = 'Antonio'
let greeting = '¡Hola, soy ' + nombre + '!'
console.log(greeting)
console.log(typeof greeting)

// Longitud
console.log(nombre.length)

// Indexar
console.log(nombre[0])
console.log(nombre[nombre.length - 1])
console.log(nombre[nombre.length])

// Metodos comunes
console.log(greeting.toUpperCase())
console.log(greeting.toLowerCase())
console.log(greeting.indexOf('Antonio'))
console.log(greeting.indexOf('o'))
console.log(greeting.indexOf('w'))
console.log(greeting.includes('Antonio'))
console.log(greeting.includes('Pedro'))

let hola = greeting.slice(1, 5)
console.log(hola)

let saludos = greeting.replace('Hola', 'Saludos')
console.log(saludos)

// Template literals
let mensaje = `Hola, este es un
mensaje en multiples lineas`
console.log(mensaje)

// Interpolar variables
let year = 1998
console.log(`Ey, soy ${nombre}, y soy del ${year}`)