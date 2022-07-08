def sum_two_smallest_numbers(numbers):
    sorted_arr = sorted(numbers)

    return sorted_arr[0] + sorted_arr[1]

def test_sum_two_smallest():
    assert sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13
    assert sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19
    assert sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30