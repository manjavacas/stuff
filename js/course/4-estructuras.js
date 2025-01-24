/******** ARRAYS ********/

// Declaracion

let arr = []
let arr2 = new Array()

console.log(arr)
console.log(arr2)

// Inicializacion

arr = [1]
arr2 = new Array(3)

console.log(arr)
console.log(arr2)

arr = [1, 2, 3, 4]
arr2 = new Array(1, 2, 3, 4)

console.log(arr)
console.log(arr2)

arr = [1, 'a', 'b', 4]
console.log(arr)

// Manipular valores

arr[0] = 'z'
console.log(arr)

arr2 = new Array(3)
arr2[0] = 'a'
arr2[2] = 'c'
console.log(arr2)

arr = []
arr[1] = 'b'
console.log(arr)

arr2 = new Array(2)
arr2[3] = 'x'
console.log(arr2)

console.log('-----------')

// Metodos comunes

arr = []

arr.push(0)
arr.push(1)

console.log(arr)

let x = arr.pop()
console.log('Extraigo', x)

console.log(arr)

console.log('-----------')

arr = [1, 2, 3, 4]
console.log(arr)

let a = arr.shift()
console.log(`Extraigo ${a} del array...`)
console.log(arr)

console.log('Introduzco un 0 al principio...')
arr.unshift(0)
console.log(arr)

console.log('Introduzco varios elementos...')
arr.unshift('1', '1')
console.log(arr)

console.log(arr.length)

// arr = [] // borrar contenido
arr.length = 0 // borrar contenido
console.log(arr)

console.log('-----------')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(arr)
let subarr = arr.slice(2,) // obtener elementos
console.log(subarr)
console.log(subarr.slice(3, 5))

console.log('-----------')

arr = ['hola', 1, true, 'prueba', 2, false]
console.log(arr)
arr.splice(1, 3) // eliminar elementos
console.log(arr)

console.log('-----------')

arr = ['hola', 1, true, 'prueba', 2, false]
console.log(arr)
arr.splice(1, 2, 'Nuevo1', 'Nuevo2')
console.log(arr)

console.log('-----------')

/******** SET ********/

// Declaracion / inicializacion

let cjto = new Set(['a', 'b', 'b', 'c'])
console.log(cjto)

// Metodos comunes

cjto.add('d')
console.log(cjto)

cjto.delete('b')
console.log(cjto)

console.log(cjto[0])
console.log(cjto.delete(1))
console.log(cjto.delete('a'))

console.log(cjto)

if (cjto.delete(2)) {
    console.log('El set cjto contenia 2 y se ha borrado')
} else {
    console.log('Elemento 2 no encontrado')
}

console.log(cjto.has('c'))
console.log(cjto.size)

// set <--> array

let myArray = Array.from(cjto)
console.log(myArray)

let mySet = new Set(myArray)
console.log(mySet)

console.log('-----------')

/******** MAPS / DICCIONARIOS ********/

// Inicializacion

// let dic = new Map()
let dic = new Map([
    ['nombre', 'Antonio'],
    ['edad', 26],
    ['nacimiento', 1998]
])

let dic2 = { 'key': 'value' }

console.log(dic2['key'])

dic2['key2'] = 'value2'
console.log(dic2['key2'])

// set

console.log(dic)

dic.set('genero', 'hombre')
console.log(dic)

dic.set('nombre', 'antonio')
console.log(dic)

// get

console.log(dic.get('nombre'))

// has

if (!dic.has('id'))
    dic.set('id', 777)

console.log(dic['id'])

// delete

console.log(dic)
dic.delete('id')
console.log(dic)

// otros metodos

console.log(dic.keys())
console.log(dic.values())
console.log(dic.entries())
console.log(dic.size)


