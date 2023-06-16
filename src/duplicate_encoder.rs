pub fn duplicate_encode(word: &str) -> String{
    let occurance_in_word: Vec<char> = word.to_lowercase().chars().collect();
    let mut result: Vec<char> = Vec::new();

    for c in &occurance_in_word{
        if occurance_in_word.iter().filter(|x| *x == c ).count() > 1 {
            result.push(')')
        }else {
            result.push('(')
        }
    }

    result.into_iter().collect()
}
