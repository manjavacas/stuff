use std::io;

fn main() {
    loop {
        println!("\nEnter a ºF temperature:  (E for exit)");

        let mut f_temp = String::new();

        io::stdin()
            .read_line(&mut f_temp)
            .expect("Error reading ºF");

        let f_temp = f_temp.trim();

        if f_temp == "E" {
            break;
        }

        let f_temp_val: f32 = f_temp.parse().expect("Error parsing ºF");
        let c_temp_val: f32 = ((f_temp_val - 32.0) * 5.0) / 9.0;

        println!("{f_temp_val}ºF = {c_temp_val}ºC");
    }
}
