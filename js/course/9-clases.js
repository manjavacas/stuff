/****** CLASES ******/

class Person {
    constructor(name, age, alias) {
        this.name = name
        this.age = age
        this.alias = alias
    }
}

let p1 = new Person('Antonio', 26, 'The programmer')
console.log(p1)

let p2 = new Person('Martha', 21, 'The best')
console.log(p2)
console.log(typeof p2)

// Valores por defecto

class User {
    constructor(name = 'user_?', age, alias = 'default') {
        this.name = name
        this.age = age
        this.alias = alias
    }
}

let user = new User('user_1')
console.log(user)

// Acceso a propiedades

console.log(user.name)
console.log(user['name'])

console.log(user.alias)
user.alias = 'Sample user'
console.log(user.alias)

// Funciones en clases

class Dog {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    bark() {
        console.log(`${this.name}: wolf, wolf!`)
    }
}

let dog = new Dog('Doggy', 10)
dog.bark()

// Atributos privados (#)

class Account {

    #password // no accesible, no modificable

    constructor(mail, password) {
        this.mail = mail
        this.#password = password
    }
}

let acc = new Account('mail@mail.com', '1234ABC')
console.log(acc)

console.log(acc.password) // no accesible
acc.password = '6789DEF' // crea una propiedad publica nueva
console.log(acc)

// Get y set

class Car {

    #id
    #year
    #serial

    constructor(id, year, serial) {
        this.#id = id
        this.#year = year
        this.#serial = serial
    }

    get year() {
        return this.#year
    }

    set year(new_year) {
        this.#year = new_year
    }
}

let car = new Car('02818-W', 2004, '1210B90WC01')
console.log(car)
console.log(car.year)

car.year = 2005
console.log(car)
console.log(car.year)

// Metodos estaticos

class MathOperations {

    static numOps = 0

    static sum(a, b) {
        this.numOps++
        return a + b
    }

    static diff(a, b) {
        this.numOps++
        return a - b
    }

}

let result = MathOperations.sum(5, 4)
console.log(result)
result = MathOperations.diff(1, 3)
console.log(result)

console.log('Operations done: ', MathOperations.numOps)

/******** HERENCIA ********/

class Animal {
    constructor(name) {
        this.name = name
    }

    eat() {
        console.log(`${this.name} eating...`)
    }
}

class Cat extends Animal {

    jump() {
        console.log(`${this.name} jumps!`)
    }
}

class Fish extends Animal {

    constructor(name, color) {
        super(name)
        this.color = color
    }

    swim() {
        console.log(`${this.name} (${this.color}) swims!`)
    }

    eat() {
        console.log(`${this.name} (${this.color}) eating...`)
    }
}

let catty = new Cat('Catty')
catty.eat()
catty.jump()

let fishy = new Fish('Fishy', 'black')
fishy.swim()
fishy.eat()