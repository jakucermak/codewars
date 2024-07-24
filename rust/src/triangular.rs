pub fn triangular(n: i32) -> i32 {
    let mut res: i32 = 0;

    for i in 1..n+1 {
        res += i;
    }
    res
}
