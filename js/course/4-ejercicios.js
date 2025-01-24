arr = ['perro', 'gato', 'pez', 'tortuga', 'loro']
console.log(arr)

arr.push('girafa')
arr.unshift('mono')
console.log(arr)

arr.splice(3, 1) // posicion, numero de elementos
console.log(arr)

console.log('---------------------------------')
// ---------------------------------------------

let cjto = new Set(['a', 'b', 'c', 'd', 'e'])
console.log(cjto)

// cjto.add('c')
// cjto.add('f')

// con operador de propagacion
cjto = new Set([...cjto, ...['c', 'f']])
console.log(cjto)

cjto.add('c')
console.log(cjto)

cjto.delete('c')
console.log(cjto)

console.log('---------------------------------')
// ---------------------------------------------

let mp = new Map([
    [1, 'enero'],
    [2, 'febrero'],
    [3, 'marzo'],
    [4, 'otro']
])

console.log(mp.get(1))
console.log(mp.has(5))


mp.set('verano', ['junio', 'julio', 'agosto'])
console.log(mp)

let a = [1,2,3,4]
console.log(a)
let s = new Set(a)
console.log(s)
let m = new Map([
    ['myset', s]
])
console.log(m)