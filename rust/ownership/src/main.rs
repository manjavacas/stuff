fn main() {

    // esto hace que tenga en memoria:
    // s = 5 y _s2 = 5
    // funciona
    let s = 5;
    let _s2 = s;
    println!("{s}");

    // esto hace que tenga en memoria:
    // s = heap[5]
    // despues _s2 = heap[5] y desaparece la referencia a s
    let s = Box::new(5);
    let _s2 = s;
    // println!("{s}"); // falla porque intento acceder a s que apunta a la nada

    // esto es similar, porque String por debajo actua como una coleccion / vector / box
    // fallaria porque desaparece la referencia a s
    let s = String::from("hello");
    let _s2 = s;
    // println!("{s}"); // falla

    // esto es una prueba
    let x = 1;
    increment(x);
    println!("{x}");
}

fn increment(mut a : i32) -> i32 {
    a += 1;
    a
}

