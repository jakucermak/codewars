def create_phone_number(n):
    prefix = "".join([str(n[i]) for i in range(0,3)])

    return f"({prefix}) " + "".join([str(n[i]) for i in range(3,6)])+"-"+"".join([str(n[i]) for i in range(6,10)])

    return prefix
def test_phone_number():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"