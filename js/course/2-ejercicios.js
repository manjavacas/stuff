
let a = 'Bizz'
let b = 'Buzz'

let c = a + b

console.log(c)
console.log(c.length)
console.log(c.toLocaleUpperCase())

const d = `${a}
and ${b} is 
${c}`
console.log(d)

let e = "this is a sample string"
console.log(e.replace(/ /g, '-')) // expresion regular

e.includes('this') ? console.log('contiene this') : console.log('no contiene this')
e.includes('thus') ? console.log('contiene thus') : console.log('no contiene thus')

console.log(a == b)
console.log(a === b)

let i = 'prueba'
let j = 'prueba'
let h = 'prueb'

console.log(i == j)
console.log(i === j)
console.log(i > j)
console.log(i > h) // length

console.log(i.length == h.lenght)