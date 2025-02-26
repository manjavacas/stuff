use std::io;

const MAX_LEN: usize = 100;

fn read_array() -> ([i32; MAX_LEN], usize) {
    let mut arr: [i32; MAX_LEN] = [0; MAX_LEN];
    let length: usize;

    loop {
        let mut length_str = String::new();
        println!("Number of elements (max. {MAX_LEN}): ");

        io::stdin()
            .read_line(&mut length_str)
            .expect("Error reading length");

        match length_str.trim().parse::<usize>() {
            Ok(len) if len > 0 && len <= MAX_LEN => {
                length = len;
                break;
            }
            _ => println!("Invalid input"),
        }
    }

    for i in 0..length {
        loop {
            let mut elem_str = String::new();
            println!("Element in position {i}: ");
            io::stdin()
                .read_line(&mut elem_str)
                .expect("Error reading element");

            match elem_str.trim().parse::<i32>() {
                Ok(val) => {
                    arr[i] = val;
                    break;
                }
                Err(_) => println!("Invalid input. Please enter a valid integer"),
            }
        }
    }

    (arr, length)
}

fn get_max_value(arr: &[i32], length: usize) -> Option<(i32, usize)> {
    if length == 0 {
        return None;
    }

    let (mut max_value, mut max_index): (i32, usize) = (arr[0], 0);

    for (i, &val) in arr.iter().take(length).enumerate() {
        if val > max_value {
            max_value = val;
            max_index = i;
        }
    }

    Some((max_value, max_index))
}

fn main() {
    let (arr, arr_length) = read_array();
    println!(
        "The following array has been read: {:?}",
        &arr[..arr_length]
    );

    match get_max_value(&arr, arr_length) {
        Some((max_value, max_pos)) => println!("Max. value: {max_value}, in position: {max_pos}"),
        None => println!("No elements in the array"),
    }
}
