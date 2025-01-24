let nombre = 'Luisa'
let edad = 15

if (nombre == 'Luisa')
    console.log(nombre)

if (edad >= 18)
    console.log('La persona puede votar')
else {
    console.log(`Le faltan ${18 - edad} años`)
}

let tipo = edad >= 18 ? 'adulto' : 'menor'
console.log(tipo)


let mes = 1
let estacion

if (mes == 12 || mes < 3) {
    estacion = 'invierno'
} else if (mes < 6) {
    estacion = 'primavera'
} else if (mes < 10) {
    estacion = 'verano'
} else {
    estacion = 'otoño'
}

console.log(estacion)

let idioma = 'frances'
let saludo

switch (idioma) {
    case 'español':
        saludo = 'hola'
        break
    case 'frances':
        saludo = 'bonjour'
        break
    case 'ingles':
        saludo = 'hello'
        break
    default:
        saludo = '~#@}]|}|@~}'
}

console.log(saludo)