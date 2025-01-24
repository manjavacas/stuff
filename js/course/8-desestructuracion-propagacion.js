let arr = [1, 2, 3, 4]

let person = {
    alias: 'John',
    surname: 'Doe',
    age: 27,
    job: {
        role: 'IT guy',
        salary: 30000
    }
}

/****** DESESTRUCTURACION ******/

// Arrays

let [val0, val1, val2, val3, val4] = arr
console.log(val0, val1, val2, val3, val4)

// Sintaxis arrays con valores por defecto

let [val5, val6, val7, val8, val9 = 0] = arr
console.log(val5, val6, val7, val8, val9)

// Ignorar elementos

let [val10, , , val13] = arr
console.log(val10, val13)


// Objetos

let { alias, surname, age, gender = 'Man' } = person
console.log(alias, surname, age, gender)

let { alias2, surname2, age2, gender2 = 'Man' } = person
console.log(alias2, surname2, age2, gender) // no existen! (NECESARIO NOMBRE REAL)

let { alias: alias3, surname: surname3, age: age3, gender3 = 'Man' } = person
console.log(alias3, surname3, age3, gender3)

// Desestructurar en diferentes niveles

let { alias: alias4, job: { role: role } } = person
console.log(alias4, role)

/****** PROPAGACION (...) ******/

// Sintaxis arrays

let arr2 = [...arr]
console.log(arr2)

let arr3 = [...arr, 5, 6]
console.log(arr3)

let arr4 = [...arr, ...arr2, ...[0, 0, 0], ...arr3]
console.log(arr4)

// Sintaxis objetos

let person2 = { ...person, email: 'mymail@mail.com' }
console.log(person2)
