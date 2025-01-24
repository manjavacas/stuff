let arr = ['a', 'b', 'c', 'd']

let [c0, c1, c2, c3, c4 = 'e'] = arr
console.log(c0, c1, c2, c3, c4)

let circulo = {
    radio: 1,
    diametro: 2,
    color: 'azul',
    centro: {
        x: 1.0,
        y: -1.0
    }
}

let { id = 'circ01', radio: r, diametro: d, color: c, centro: { x: cX, y: cY } } = circulo
console.log(id, r, d, c, cX, cY)

let a1 = [1,2,3]
let a2 = [4,5,6]
console.log([...a1, ...a2])

let a3 = [...a1]
console.log(a3)

let circulo2 = {...circulo, dibujar: true}
console.log(circulo2)

let circulo3 = {...circulo2}
console.log(circulo2)

let {radio: rad, ...circ} = circulo3
console.log(rad, circ)