/******** OBJETOS ********/

// Sintaxis

let person = {
    name: "Antonio",
    edad: 26,
    job: "Programmer"
}

console.log(person)
console.log(typeof person)

// Accceso a propiedades

console.log(person.name)
console.log(person["name"])

// Modificar objeto

person.name = "Marta"
console.log(person.name)

// Eliminar propiedades

delete person.job
console.log(person)

// Nueva propiedad

person.mail = "sample@mail.com"
person["alias"] = "The best programmer"
console.log(person)

// Metodos y anidacion de objetos

let bot = {
    name: "MyBot",
    walk: function () {
        console.log("Walking")
    },
    stop: function () {
        console.log("Stop")
    },
    owner: person
}

bot.walk()
console.log(bot)
console.log(bot.owner)

// Igualdad de objetos

let person1 = {
    name: "Eva",
    edad: 35,
    job: "Programmer"
}

let person2 = {
    name: "Eva",
    edad: 35,
    job: "Programmer"
}

console.log(person1 == person2)
console.log(person1 === person2)

// Recorrer propiedades de un objeto (for - in)

for (let key in person) {
    console.log(person[key])
}

// for(let val of person) {
//     console.log(val)
// } --> ERROR!

// Acceso interno a propiedades de objetos (this)

let pet = {
    name: "Doggy",
    type: "Dog",
    sound: function () {
        console.log(`${this.name}: wolf, wolf!`)
    }
}

pet.sound()

// Objetos como funciones (MALA PRACTICA, deberia ser una clase)

function Person(name, age) {
    this.name = name
    this.age = age
}

let client1 = new Person('John', 30)
let client2 = new Person('Dana', 31)