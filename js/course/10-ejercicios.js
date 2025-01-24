class NumError extends Error {
    constructor(message, x) {
        super(message)
        this.x = x
    }
    printError() {
        console.log("ERROR: value ", this.x, this.message)
    }
}

function increment(x) {
    if(!Number.isInteger(x)) {
        throw new NumError('is not a number', x)
    }
    return x + 1
}


let x = 'a'

try {
    increment(x)
} catch(error) {
    error.printError()
}

// ---------------------------------------------------

let attempts = 0

do {
    console.log('attempt ', attempts)
    try {
        increment(x)
    } catch {
        attempts++;
    }
} while(attempts < 10)

console.log('end...')


