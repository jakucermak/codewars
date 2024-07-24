use std::{option::IterMut, vec};

pub fn unique_in_order<T>(sequence: T) -> Vec<T::Item>
where
    T: std::iter::IntoIterator,
    T::Item: std::cmp::PartialEq + std::fmt::Debug,
{
    let mut res: Vec<T::Item> = Vec::new();

    let mut iter = sequence.into_iter();
    if let Some(iter_first)= iter.next() {
        res.push(iter_first);
    }else{
        return vec![];
    }
    

    for item in iter{
        if  &item != res.last().unwrap(){
            res.push(item)
        }
    }
    res
}
