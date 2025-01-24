let circulo = {
    id: 'circ_01',
    color: 'azul',
    radio: 3.5,
    area: function() {
        console.log(`Area: ${Math.PI * this.radio ** 2}`)
    },
    centro: {
        x: 1.0,
        y: 2.0
    }
}

console.log(circulo)

circulo.sombreado = false
delete circulo.id

console.log(circulo)
circulo.area()

for(let key in circulo)
    console.log(circulo[key])

console.log(circulo.centro)

for(let key in circulo.centro)
    console.log(circulo.centro[key])

console.log(circulo == circulo.centro)
console.log(circulo.radio == circulo.color)