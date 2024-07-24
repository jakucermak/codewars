pub fn contamination(text: &str, character: &str) -> String {
    text.chars().map(| x| character).collect()
}
