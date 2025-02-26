use std::io;

fn main() {
    let n = read_input_num();

    println!("Fibonacci series: ");
    
    let (mut x0, mut x1) = (0, 1);

    for _ in 1..n {
        println!("{}", x0);
        let sum = x0 + x1;
        x0 = x1;
        x1 = sum;
    }
}

fn read_input_num() -> u64 {
    println!("Enter limit number: ");
    let mut limit = String::new();
    io::stdin()
        .read_line(&mut limit)
        .expect("Error reading value");
    let limit: u64 = limit.trim().parse().expect("Error parsing value");
    limit
}
