def two_sum(numbers, target):
    l = len(numbers)
    for i in range(0,l):
        for j in range(0,l):
            if (i != j) and (numbers[i] + numbers[j] == target):
                return [i,j]

def test_two_sum():

    assert sorted(two_sum([1,2,3], 4)) == [0,2]
    assert sorted(two_sum([1234,5678,9012], 14690)) == [1,2]
    assert sorted(two_sum([2,2,3], 4)) == [0,1]