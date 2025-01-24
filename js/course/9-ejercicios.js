class Guitar {
    constructor(brand, year) {
        this.brand = brand
        this.year =  year
    }

    sound() {
        console.log('ring ring!')
    }

    static notes() {
        console.log('E A D G B E')
    }
}

let g = new Guitar('Fender', 1959)
console.log(g.brand, g.year)
g.sound()
Guitar.notes()


class OwnedGuitar extends Guitar{
    
    #owner
    
    constructor(brand, year, owner) {
        super(brand, year)
        this.#owner = owner
    }

    set owner(owner) {
        this.#owner = owner
    }

    get owner() {
        return this.#owner
    }

    sound() {
        console.log('rang rang!')
    }
}

let og = new OwnedGuitar('Fender', 1971, 'Jimmy Hendrix')
console.log(og.owner)
og.owner = 'Jimmy Page'
console.log(og)
console.log(og.owner)
og.sound()