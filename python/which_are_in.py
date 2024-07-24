def in_array(array1, array2):
    result = []

    for word_1 in array1:
        for word_2 in array2:
            if str(word_2).__contains__(word_1):
                result.append(word_1)


    return list(sorted(set(result)))


a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1,a2))