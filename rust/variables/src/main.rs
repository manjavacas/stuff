fn main() {
    
    // Variables are immutable by default
    let x = 5;
    println!("The value of immutable x is: {x}");

    // x = 6; --> ERROR!
    
    // A mutable variable may be...
    let mut y = 5;
    println!("The value of mutable y is: {y}");
    y = 7;
    println!("...and the value of mutable y is now: {y}");

    // Constants may be set only to a constant expression
    // ...and always have a type
    const MY_CONSTANT : u32 = 60 * 60 * 3;
    // constants can be used globally (vs. 'let')

    println!("Constant value: {MY_CONSTANT}");

    // Shadowing
    let z = 5;
    let z = z + 1;

    {
        let z = z * 2;
        println!("Inner scope value of z: {z}");
    }

    println!("Outer scope value of z: {z}");

    // shadowing is different from defining a variable as 'mut'
    // we'll get a compile error if we reassing its value without 'let'

    // 'let' allows overwriting

    let _spaces = "   "; // string
    let _spaces = _spaces.len(); // overwritten by number

    let mut _spaces = "   "; // string
    // spaces = spaces.len(); --> ERROR! str to number

}
