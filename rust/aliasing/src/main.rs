fn main() {
    let mut v: Vec<i32> = vec![1,2,3];
    
    let num : &i32 = &v[2];
    println!("{num}");

    v.push(4);
    // println!("{num}"); -> ERROR, ya que al actualizar v su direccion de memoria cambia

    // v is aliased by the reference num, and mutated by v.push(4)

    // Pointer Safety Principle: data should never be aliased and mutated at the same time
}
