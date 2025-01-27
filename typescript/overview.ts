// create project config json file with
// $ npx tsc --init

let x = 4
let y = 5

// let x: number = 4
// let y: number = 5

console.log(x)
console.log(typeof x)

let undef: undefined
console.log(undef)

const z = 10

if (z > 0) {
    console.log("Value of z = ", z)
}

function add(x: number, y: number): number {
    return x + y
}

console.log("x + y = " + add(x, y))

function showSum(x: number, y: number) {
    console.log(x + y)
}

showSum(x, y)

let l: Array<string> = ["A", "B", "C"]
l.push("D")
console.log(l)

let s: Set<string> = new Set(["A", "A", "B", "C"])
s.add("D")
console.log(s)

let m: Map<number, string> = new Map([
    [1, "A"],
    [2, "B"],
    [3, "C"]
])
m.set(4, "D")
console.log(m)

for (const value of l) {
    console.log(value)
}

while (x > 0) {
    console.log(x)
    x--
}

do {
    y--
    console.log(y)
} while (y > 0)

class User {
    name: string
    age: number

    constructor(name: string, age: number) {
        this.name = name
        this.age = age
    }
}

let u = new User("John", 30)
console.log(u)

enum Enumeration {
    PYTHON = "python",
    JAVA = "java",
    CPP = "c++",
    JS = "javascript"
}

const e = Enumeration.CPP
console.log(e)