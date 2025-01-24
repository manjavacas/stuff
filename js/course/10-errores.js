/****** MANEJO DE ERRORES *****/

// try-catch

let user

try {
    console.log(user.name)
} catch (error) {
    console.log('[ERROR] Name is not defined.')
}

// catch error

try {
    console.log(user.name)
} catch (error) {
    console.log('[ERROR]', error.message)
}

// try-catch-finally

try {
    console.log(user.name)
} catch (error) {
    console.log('[ERROR]', error.message)
} finally {
    console.log('Anyways...')
}

// Lanzar errores y capturarlos

function sumInts(a, b) {

    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new Error('sum is only available for numbers')
    }


    if (!Number.isInteger(a) || !Number.isInteger(b)) {
        throw new Error('sum is only available for integers')
    }
    return a + b
}

try {
    console.log(sumInts(5, 4))
    console.log(sumInts('5', 4))
} catch (error) {
    console.log('Catched error: ', error.message)
}

// Capturar varios tipos de errores

function diffInts(a, b) {

    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('diff is only available for numbers')
    }


    if (!Number.isInteger(a) || !Number.isInteger(b)) {
        throw new Error('diff is only available for integers')
    }
    return a - b
}

try {
    console.log(diffInts('5', 4))
} catch (error) {
    if (error instanceof TypeError) {
        console.log('Type error: ', error.message)
    } else {
        console.log('Error: ', error.message)
    }
}

try {
    console.log(diffInts(6.4, 4))
} catch (error) {
    if (error instanceof TypeError) {
        console.log('Type error: ', error.message)
    } else {
        console.log('Error: ', error.message)
    }
}

// Crear errores personalizados

class CustomError extends Error {
    constructor(message, a, b) {
        super(message)
        this.a = a
        this.b = b
    }

    printNumbers() {
        console.log('Cannot divide: ', this.a, '/', this.b)
    }
}


function DivInts(a, b) {
    if (b == 0) {
        throw new CustomError('div cannot divide by zero', a, b)
    }
    return a / b
}

try {
    DivInts(5, 0)
} catch (error) {
    if (error instanceof CustomError) {
        error.printNumbers()
    }
}
