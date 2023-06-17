
pub fn find_outlier(values: &[i32]) -> i32 {
    let mut evens: Vec<i32> = Vec::new();
    let mut odds: Vec<i32> = Vec::new();


    for i in values {
        if i % 2 == 0 {
            evens.push(*i);
        }else{
            odds.push(*i);
        }
    }

    if evens.len() == 1 {
        evens[0]
    }else{
        odds[0]
    }
}