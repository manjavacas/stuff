
let sumar = (x, y) => x + y

let suma = sumar(1, 2)
console.log(suma)

/************************************************/

function mayor(arr) {
    let mayor = arr[0]
    for (let i = 0; i < arr.length; i++)
        if (arr[i] > mayor)
            mayor = arr[i]
    return mayor
}

console.log(mayor([1, 2, 3, 4, 5, 4, 3, 2, 1]))

/************************************************/

const vocalsum = (cadena) => {
    vocales = ['a', 'e', 'i', 'o', 'u']
    let sum = 0
    for (let i = 0; i < cadena.length; i++) {
        if (vocales.includes(cadena[i]))
            sum++;
    }
    return sum
}

console.log(vocalsum('murcielago'))

/************************************************/

function mayus(arr) {
    let mayus_arr = []
    arr.forEach((cad) => mayus_arr.push(cad.toUpperCase()))
    return mayus_arr
}

let mapyus = (arr) => arr.map(cad => cad.toUpperCase())

let arr_cads = ['hola', 'que', 'tal']

console.log(mayus(arr_cads))
console.log(mapyus(arr_cads))
