fn main() {
    let mut items = [
        "twelve drummers drumming",
        "eleven pipers piping",
        "ten lords-a-leaping",
        "nine ladies dancing",
        "eight maids-a-milking",
        "seven swans-a-swimming",
        "six geese-a-laying",
        "five golden rings",
        "four calling birds",
        "three French hens",
        "two turtle doves",
        "a partridge in a pear tree",
    ];

    items.reverse();

    for i in 0..items.len() {
        heading();
        println!("{}", items[i]);
        for j in (0..i).rev() {
            println!("{}", items[j]);
        }
        println!();
    }
}

fn heading() {
    let heading_lines = ["on the first day of Christmas", "my true love gave to me"];
    for line in heading_lines {
        println!("{line}");
    }
}
