def move_zeros(array:list):
    idx = []
    for i in range(0,len(array)):
        if array[i] == 0:
            idx.append(i)
            array.append(0)
    for i in range(len(idx)-1,-1,-1):
        array.pop(idx[i])
    return array

print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])