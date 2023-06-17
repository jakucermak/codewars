use std::f64::consts::PI;

use either::Either;

pub fn sort_by_area(seq: &[Either<(f64, f64), f64>]) -> Vec<Either<(f64, f64), f64>> {
    let mut temp: Vec<(f64, Either<(f64,f64), f64>)> = Vec::new();

    for iter in seq {
        match iter {
            Either::Left(sq) => {
                temp.push((sq.0 * sq.1,Either::Left(sq.clone())));
            },
            Either::Right(r) => {
                temp.push(((r.powf(2.0)* PI), Either::Right(r.clone())));
            },
        }
    }

    temp.sort_by(|a,b| a.0.partial_cmp(&b.0).unwrap());

    temp.iter().map(|x| x.1).collect()
}