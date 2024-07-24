/// Converts a number to a string representating roman numeral.
use std::collections::BTreeMap;

pub fn num_as_roman(num: i32) -> String {
    let mut dict: BTreeMap<i32, char> = BTreeMap::new();
    dict.insert(1, 'I');
    dict.insert(5, 'V');
    dict.insert(10, 'X');
    dict.insert(50, 'L');
    dict.insert(100, 'C');
    dict.insert(500, 'D');
    dict.insert(1000, 'M');

    let mut iter = dict.iter().rev();

    let mut res: Vec<char> = Vec::new();
    let mut temp: (i32, i32) = (num, *iter.next().unwrap().0);

    while &temp.0 > &0 {
        if &temp.0 >= &temp.1 {
            res.push(dict[&temp.1]);
            temp = (&temp.0 - &temp.1, temp.1);
        } else {
            temp = (temp.0, *iter.next().unwrap().0);
        }
        
    }

    res.iter().collect()
}
