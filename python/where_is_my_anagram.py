def anagrams(word, words):
    sorted_word = sorted(word)
    result = []
    for w in words:
        sorted_w = sorted(w)
        if list(sorted_word) == sorted_w:
            result.append(w)
    return result



print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])