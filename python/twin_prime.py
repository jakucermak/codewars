def is_prime(n):
    result  = False
    if n > 1:
        for i in range(2,n):
            if(n%i) == 0:
                result = False
                break
            else:
                result = True
    return result

def is_twinprime(n):
    x = is_prime(n)
    y = is_prime(n+2)
    z = is_prime(n-2)
    if x and (y or z):
        return True
    return False

def test_is_twin_prime():
    assert is_twinprime(9) == False
    assert is_twinprime(7) == True