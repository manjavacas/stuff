fn main() {
    
    // how Rust "follows" a pointer to its data?
    // dereference operator -> *

    let mut x: Box<i32> = Box::new(1); // x= heap[2]
    let a: i32 = *x; // a = 1 (stack)
    *x += 1; // content in x += 1

    println!("{x}, {a}");

    let r1 : &Box<i32> = &x; // r1 points to x (stack)
    let b: i32 = **r1;  // b value = deref(r1(deref(x)) -> value of x

    let r2 : &i32 = &*x; // r2 points to heap value directly (heap)
    let c: i32 = *r2; // only one dereference needed to read it

    println!("{r1}, {b}");
    println!("{r2}, {c}");

    // explicit dereference
    let x_abs1 = i32::abs(*x);
    // implicit dereference
    let x_abs2 = x.abs(); // syntactic sugar (works for multiple layers of pointers)
    assert_eq!(x_abs1, x_abs2);

    // it also works in the opposite direction
    let s = String::from("Hello");
    let s_len1 = str::len(&s); // explicit
    let s_len2 = s.len();
    assert_eq!(s_len1, s_len2);

}
