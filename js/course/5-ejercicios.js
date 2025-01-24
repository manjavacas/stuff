let i = 1
while (i <= 20) {
    console.log(i)
    i++
}

let sum = 0
for (i = 1; i <= 100; i++)
    sum += i
console.log(sum)

for (i = 1; i <= 50; i++)
    if (i % 2 == 0)
        console.log(i)

let names = ['a', 'b', 'c']

for (let x of names)
    console.log(x)

let vocales = 0
for (let x of 'antonio')
    if (['a', 'e', 'i', 'o', 'u'].includes(x))
        vocales++
console.log(vocales)

for(let i = 0; i < 10; i++)
    console.log(`5 x ${i} = ${5*i}`)


// LAS CADENAS EN JS CON INMUTABLES!
// let cadena = 'antonio'
// for(let i = 0; i < cadena.length / 2; i++) {
//     let aux = cadena[i]
//     cadena[i] = cadena[cadena.length - i]
//     cadena[cadena.length - i] = aux
// }
// console.log(cadena)

let cadena = 'antonio'
let invertida = ''

for(i = cadena.length - 1; i >= 0; i--)
    invertida += cadena[i]
console.log(invertida)
