def second_largest_perimeter(arr):
    sums_of_elements = []
    index_of_max = 0
    index_of_second = 0
    if len(arr) == 0: return -1
    for i in range(0,len(arr)):
        if sum(arr[i]) > sum(arr[index_of_max]):
            index_of_second = index_of_max
            index_of_max = i
    return index_of_second


tests_array_1 = [[2, 3, 4],[4, 5, 6],[7, 8, 9],[10, 11, 12]]
tests_array_2 = [[2, 3, 4],[4, 5, 6]]

print(second_largest_perimeter(tests_array_1))
print(second_largest_perimeter(tests_array_2))
print(second_largest_perimeter([]))