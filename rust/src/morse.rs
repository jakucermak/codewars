// MORSE_CODE is `HashMap<String, String>`. e.g. ".-" -> "A".
use std::collections::HashMap;

pub fn decode_morse(encoded: &str) -> String {
    // Will delete this line
    let MORSE_CODE: HashMap<String, String> =
        HashMap::from([(String::from(".-"), String::from("A"))]);

    let mut res: Vec<char> = Vec::new();
    for word in encoded.split("  ") {
        for sign in word.split(" ") {
            if sign != " " {
                if let Some(letter) = MORSE_CODE
                    .get(sign)
                    .unwrap()
                    .chars()
                    .next(){
                        res.push(letter)
                    }
            }

        }
        res.push(' ')
    }
    res.iter().collect()
}
