'''
solve("((1)23(45))(aB)", 0) = 10 -- the opening brace at index 0 matches the closing brace at index 10
solve("((1)23(45))(aB)", 1) = 3 
solve("((1)23(45))(aB)", 2) = -1 -- there is no opening bracket at index 2, so return -1
solve("((1)23(45))(aB)", 6) = 9
solve("((1)23(45))(aB)", 11) = 14
solve("((>)|?(*'))(yZ)", 11) = 14
'''


def solve(st, idx):
    inner_blocks = 0
    if st[idx] != '(': return -1
    for i in range(idx+1, len(st)):
        if st[i] == '(':
            inner_blocks += 1
        elif st[i] == ')' and inner_blocks > 0:
            inner_blocks -= 1
        elif st[i] == ')':
            return i


print((solve("((1)23(45))(aB)",0),10))
print((solve("((1)23(45))(aB)",1),3))
print((solve("((1)23(45))(aB)",2),-1))
print((solve("((1)23(45))(aB)",6),9))
print((solve("((1)23(45))(aB)",11),14))
print((solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",11),28))
print((solve("(g(At)IO(f)(tM(qk)YF(n)Nr(E)))",0),29))
print((solve("(>_(va)`?(h)C(as)(x(hD)P|(fg)))",19),22))