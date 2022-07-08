def digital_root(n):
    string_num = str(n)
    result = 0
    for i in string_num:
        result += int(i)
    if len(str(result)) > 1:
       return digital_root(result)
    return result

print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)
print(digital_root(493193), 2)