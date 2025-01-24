/**** IF-ELSE ****/

let x = 5
let y = 10

if (x > y) {
    console.log('x es mayor que y')
} else if (x < y) {
    console.log('x es menor que y')
} else {
    console.log('x e y son iguales')
}

/**** OPERADOR TERNARIO ****/

x > y ? console.log('x es mayor que y') : console.log('x es menor o igual que y')

let mayor = x > y ? true : false

if (mayor) {
    console.log('x es mayor que y')
} else {
    console.log('x es menor o igual que y')
}

/**** SWITCH ****/

let day = 5
let dayname

switch (day) {
    case 0:
        dayname = 'Lunes'
        break
    case 1:
        dayname = 'Martes'
        break
    case 2:
        dayname = 'Miercoles'
        break
    case 3:
        dayname = 'Jueves'
        break
    case 4:
        dayname = 'Viernes'
        break
    case 5:
        dayname = 'Sabado'
        break
    case 6:
        dayname = 'Domingo'
        break
    default:
        dayname = 'Desconocido'
}

console.log(dayname)