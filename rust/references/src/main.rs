fn main() {
    let m1 = String::from("Hello");
    let m2 = String::from("world");
    
    // greet(m1, m2); // cuando se llama a la funcion, m1 y m2 ya no apuntan a a nada
    // son g1 y g2 quienes apuntan a esas cadenas
    // let s = format!("{} {}", m1, m2); -> ERROR

    // podemos usar una version alternativa que devuelva otra vez esas cadenas
    // let (m1b, m2b) = greet_return(m1, m2); // demasiado verbose -> MEJORABLE
    // let s = format!("{} {}", m1b, m2b);

    // solucion -> referencias
    // g1 y g2 son referencias a m1 y m2, que apuntan a heap["hello"] y heap["world"]
    greet_ref(&m1, &m2);
    // "hello" pertence a m1, mientras que g1 "lo pide prestado" -> borrowing
    // como "hello" no pertence a g1, este no es capaz de eliminarlo del heap
    // references are non-owning pointers

    let s = format!("{} {}", m1, m2);
    
    println!("{s}");
}

// fn greet(g1: String, g2: String) {
//     println!("{} {}!", g1, g2);
// }

// fn greet_return(g1: String, g2: String) -> (String, String) {
//     println!("{} {}", g1, g2);
//     (g1, g2)
// }

fn greet_ref(g1: &String, g2: &String) {
    println!("{} {}", g1, g2);
}