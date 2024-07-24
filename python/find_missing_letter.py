import string

def find_missing_letter(chars):
    lower = string.ascii_lowercase
    is_upper = chars[0].isupper()
    lower_chars = [x.lower() for x in chars]
    started = False

    for i in range(len(lower)):
        if lower[i] in lower_chars and started == False:
            started = True
        if lower[i+1] not in lower_chars and started == True:
            if is_upper:
                return lower[i+1].upper()
            return lower[i+1]


print(find_missing_letter(['a','b','c','d','f']), 'e')
print(find_missing_letter(['O','Q','R','S']), 'P')


