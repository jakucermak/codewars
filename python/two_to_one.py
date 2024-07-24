def longest(a1, a2):
    return "".join(sorted(list(set(a1+a2))))

def test_longest():
    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"
