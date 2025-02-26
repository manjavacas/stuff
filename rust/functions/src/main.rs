fn main() {
    println!("This is main");

    // ----- BASIC FUNCTIONS -----
    another_function();
    param_function(5, 'a');

    // ----- STATEMENTS -----
    let x = 1;
    // statements do not evaluate to a value
    // function definitions are also statements
    // statements do not return alues

    // ----- EXPRESSIONS -----
    // expressions evaluate to a value
    // expressions can be part of statements
    // let x = 1 is an expression that evaluates to 1
    // calling a function is an expression
    // calling a macro is an expression
    // a new scope block created with {} is an expression...

    let y = {
        let w = 3;
        x + w // note how the ; is not included at the end
    }; // everything inside the braces is a block which evaluates to x + w
       // adding a semicolon at the end of an expression turns it into a statement
    println!("{y}");

    // ----- FUNCTIONS WITH RETURN VALUES -----
    let z = return_function(1, 2);
    println!("Return function output: {z}");

    let w = return2_function(1, 1);
    println!("Return function (2) output: {w}");

    println!("Return function (3) output: {}", return3_function());

    // function + expression
    println!(
        "{}",
        increment({
            let y = 1;

            y + 1
        })
    );

    /* Code block */
}

// snake_case convention; declaration place is not important
fn another_function() {
    println!("This is not main");
}

// type anotations are required for each parameter
fn param_function(x: u8, y: char) {
    println!("Parameters: {x}, {y}");
}

// return value of the funcion is the value of its final expression
// return type is mandatory, and indicated with '->'
// the 'return' keyword can equally be used (i.e., for early returning a value)
fn return_function(x: i32, y: i32) -> i32 {
    x + y
    // x + y; would lead to an error!
}

fn return2_function(x: i32, y: i32) -> i32 {
    return x + y;
    // also: return x + y
}

fn return3_function() -> i32 {
    3
    // 3; would lead to an error!
}

fn increment(x: i32) -> i32 {
    x + 1
}

// a curlly-brace block like { /* ... */ } is
// an expression and a syntactic scope
