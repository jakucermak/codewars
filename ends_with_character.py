def end_with_character(str,char):
    set_words = set(str.split())
    count = 0
    for word in set_words:
        if word[len(word)-1] == char:
            count += 1
    return count

print(end_with_character("all is well that ends well","l"))