extern crate either;

mod sort_area;
mod triangular;
// mod prime_factors;
mod unique_in_order;
mod parity_outliar;
mod duplicate_encoder;
mod morse;
mod plural;
use either::Either;

fn main() {
    // let str = "recede";
    // plural::plural(1.0);
    // duplicate_encoder::duplicate_encode(&str);
    // print!("{}", morse::decode_morse(""));
    // print!("{:?}", triangular::triangular(4));
    // println!("{:?}", unique_in_order::unique_in_order("AAAABBBCCDAABBB".chars()));
    // println!("{:?}", prime_factors::prime_factors(12));
    // let seq = &[ Either::Left((4.23, 6.43)), Either::Right(1.23), Either::Right(3.444), Either::Left((1.342, 3.212)) ];
    // println!("{:?}", sort_area::sort_by_area(seq));
    let t1 = [2,6,8,-10,3];
    println!("{:?}", parity_outliar::find_outlier(&t1));
}