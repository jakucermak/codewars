def find_even_index(arr):
    length = len(arr)
    result = -1
    for i in range(length):
        left_sum = 0
        right_sum = 0

        for j in range(i,length):
            right_sum += arr[j]

        for k in range(i,-1,-1):
            left_sum += arr[k]

        if left_sum == right_sum:
            result = i
            break
    return result

def test_find_index():
    assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
    assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
    assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
    assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
    assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
    assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
    assert find_even_index(list(range(1, 100))) == -1
    assert find_even_index([0, 0, 0, 0, 0]) == 0
    assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
    assert find_even_index(list(range(-100, -1))) == -1
