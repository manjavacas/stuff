/***** MODULOS *****/

// Usamos 'export' y empleamos la extension 'mjs'

// otra opcion: añadir un fichero package.json y emplear la extension 'js'
// package.json => { "type":"module" }

export function add(a, b) {
    return a + b
}

// export para variables

export const PI = 3.1416

// export por defecto

export default function substract(a, b) {
    return a - b
}

// la exportacion por defecto tiene que ser unica

// export default function substract2(a, b) {
//     return a - b
// } => ERROR

// exportacion de clases

export class Circle {
    constructor(radius) {
        this.radius = radius
    }
    area() {
        return Math.PI * Math.pow(this.radius,2)
    }
    perim() {
        return 2 * Math.PI * this.radius
    }
}

// export default class Circle {
//     constructor(radius) {
//         this.radius = radius
//     }
//     area() {
//         return Math.PI * Math.pow(this.radius,2)
//     }
//     perim() {
//         return 2 * Math.PI * this.radius
//     }
// }