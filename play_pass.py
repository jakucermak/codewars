import pytest
import string
def play_pass(s, n):
    alpha = string.ascii_uppercase
    result = ""
    i,j = 0,0
    for _ in range(len(s)):
        if s[i].isalpha():
            l = len(alpha)
            if len(alpha) <= n + alpha.index(s[i]):
                i = alpha.index(s[i]) - len(alpha)
            if i % 2 != 0:
                result += alpha[alpha.index(s[i])+n].lower()
            else:
                sub = alpha[alpha.index(s[i])+n].upper()
                result += alpha[alpha.index(s[i])+n].upper()
        elif s[i].isdigit():
            result += f"{9-int(s[i])}"
        else:
            result += s[i]
        i,j = j+1,j+1


    return result[::-1]
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == "!4897 Oj oSpC")

def test_play_pass():
    assert play_pass("BORN IN 2015!", 1) == "!4897 Oj oSpC"
    assert play_pass("I LOVE YOU!!!", 1) ==  "!!!vPz fWpM J"
    assert play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"