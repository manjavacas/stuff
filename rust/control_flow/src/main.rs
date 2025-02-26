fn main() {
    // IF-ELSE

    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    // if number { ... } would lead to an ERROR
    // because, in Rust, non-bool types are not converted to bool

    if number % 2 == 0 {
        println!("divisible by 2");
    } else if number % 3 == 0 {
        println!("divisble by 3");
    } else {
        println!("not divisible by 2 or 3");
    }

    // if within let statement
    let condition = true;
    let value = if condition { 5 } else { -5 };

    println!("{value}");
    // let value = if condition { 5 } else { 'a' }; --> ERROR!

    // if 1 {
    //     println!("1 is similar to true");
    // } --> INTEGER is not casted to BOOL

    // LOOPS

    // loop
    let mut i = 0;
    loop {
        println!("i = {i}");
        i += 1;

        if i >= 3 {
            break;
        }
        // break, continue
    }

    // loops can be used to retry operations that might fail
    // we can add the value to be returned after break

    let mut tries = 0;

    let result = loop {
        tries += 1;

        if tries == 5 {
            println!("Time limit!");
            break (-1, tries); // ; is optional
        }
    };

    println!("Result is {} after {} tries", result.0, result.1);

    // loops can be named with labels (e.g. 'loop_label) -- with a single quote
    let mut c = 0;

    'double_up: loop {
        c *= 2;
        println!("outer: c = {c}");

        'sum_up: loop {
            c += 1;
            println!("\tinner: c = {c}");

            if c % 3 == 0 {
                break 'sum_up; // similar to just break
            }

            if c % 5 == 0 {
                break 'double_up;
            }
        }
    }

    // WHILE loops
    let mut attempts = 4;
    
    while attempts > 0 {
        println!("attempt: {attempts}");
        attempts -= 1;
    }

    // FOR loops
    let arr = [1, 2, 3, 4, 5];
    
    // run throughout an array
    for element in arr {
        println!("the value is {element}");
    }

    // using a range from 4 (not included) to 1
    for number in (1..4).rev() { 
        println!("{number}");
    }
}
