use std::io;

fn main() {
    // Scalar values:

    // ----- INTEGERS -----

    // (8 to 128 bits, isize, usize, signed/unsigned)
    let _a = 1_000; // decimal
    let _b = 0xff; // hexadecimal
    let _c = 0o77; // octal
    let _d = 0b1111_0000; // binary
    let _e = b'A'; // byte
                   // integers are i32 by default

    // Integer overflow
    // let _f : u8 = 256; --> ERROR!

    // If cargo build --release, integer overflow is not checked
    // values are "wrapped around"
    // let mut _g : u8 = 255;
    // _g = _g + 1;
    // println!("{_g}"); --> ERROR with RUN, but not when RELEASED

    // ----- FLOATING POINT NUMBERS -----
    // f32 and f64 (by default -> same speed, more precission)

    let x = 1.0 / 3.0;
    let y: f32 = 1.0 / 3.0;

    println!("Float 64: {x}, Float 32: {y}");

    // Math operations...
    // +, -, *
    let quotient = 56.7 / 32.2;
    println!("{quotient}");
    let trunc = -5 / 2;
    println!("{trunc}");
    let rem = 43 % 5;
    println!("{rem}");

    // ----- BOOLEANS -----
    // true/false, 1 byte size

    let _t = true;
    let _f: bool = false;

    // ----- CHARACTERS -----
    // 4 bytes size
    let p = 'p';
    let q: char = 'ℤ';
    let r = '😻';

    println!("{p}");
    println!("{q}");
    println!("{r}");

    // Compound types
    // can group multiple values into one type

    // ----- TUPLES -----
    // fixed length, different types inside

    let tup: (f64, u8, char) = (12.1212, 97, 'a');

    let (u, _v, _w) = tup; // destructing
    println!("{u}");
    println!("{}", tup.1); // indexing

    // tuple without values is named as 'unit'
    let _un = ();
    // expressions implicitly return it if they do not return
    // any other value

    // tuples can be mutable
    let mut tup2 = ('a', 5);
    tup2.0 = 'c';
    tup2.1 += 5;
    println!("{}, {}", tup2.0, tup2.1);

    // ----- ARRAYS -----
    // a single chunk of memory of a known, fixed size that can be allocated on the stack
    // elements of the SAME TYPE, fixed length
    // indexed with []

    let arr = [1, 2, 3, 4];
    println!("{}", arr[0]);

    // useful for allocate data on the stack
    // rathen than the heap

    // array type: type of each element + number of elements
    let months: [&str; 12] = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];

    println!("{}", months[3]);

    // another way...
    let arr2 = [2; 3]; // has 3 2's, similar to [2,2,2]
    println!("{},{},{}", arr2[0], arr2[1], arr2[2]);

    // runtime errors can happen if indexing beyond array length
    println!("Enter month number: ");
    
    let mut index = String::new();
    io::stdin().read_line(&mut index).expect("Failed to read line");

    let index: usize = index.trim().parse().expect("Failed to cast number");

    println!("The month is {}", months[index - 1]);

}
