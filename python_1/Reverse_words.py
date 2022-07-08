def reverse_words(str):
    str_arr = str.split(" ")
    temp_w = ""
    result = ""
    for w in str_arr:
        for c in range(len(w)-1,-1, -1):
            temp_w += w[c]
        result += temp_w + " "
        temp_w = ""
    return result.strip()


print(reverse_words('The quick brown fox jumps over the lazy dog.'),'ehT kciuq nworb xof spmuj revo eht yzal .god')
print(reverse_words('apple'), 'elppa')
print(reverse_words('a b c d'), 'a b c d')
print(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')