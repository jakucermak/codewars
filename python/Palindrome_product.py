def is_palindrome(n):
    if f"{n}" == f"{n}"[::-1]: return True
    else: return False

def palindrome_product():
    result = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if is_palindrome(i*j):
                result.append(j*i)
    return max(result)


def some():
    str = "  hello my little pony "

    rev = "".join([str[i] for i in range(len(str)-1,-1, -1)])
    print(rev)


some()
