/***** FOR *****/

let x = 0
const n = 5

for (let i = 0; i < n; i++) {
    console.log(x)
    x++
}

console.log('------------------')

const nums = [1, 2, 3, 4]

for (let i = 0; i < nums.length; i++) {
    console.log(nums[i])
}

console.log('------------------')

/***** WHILE *****/

let y = 4

while (y > 0) {
    console.log(y)
    y--
}

console.log('------------------')

/***** DO-WHILE *****/

let z = 10

do {
    console.log(z)
    z++
} while (z < 10)

console.log(z)

console.log('------------------')

/***** FOR-OF *****/

let arr = [1, 2, 3]
let cjt = new Set(['a', 'b', 'c'])
let dic = new Map([[1, 'a'], [2, 'b'], [3, 'c']])

for (let x of arr)
    console.log(x)

for (let x of cjt)
    console.log(x)

for (let x of dic)
    console.log(x)

for (let x of 'Hola que tal')
    console.log(x + ',')

console.log('------------------')

/***** BREAK, CONTINUE *****/

for (let x of 'Hoooooola')
    if (x == 'l')
        break
    else if (x == 'o')
        continue
    else
        console.log(x + ' ')

