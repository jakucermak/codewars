def swap(matrix):
    length = len(matrix[0])
    result = matrix

    for i in range(0, length):
        if i > 0:
            for j in range(0, length):
                if i == j:
                    result[i-1][j], result[i][j-1] = result[i][j-1], result[i-1][j]
                    if i != length-1:
                        result[i+1][j-1], result[i-1][j+1] = result[i-1][j+1], result[i+1][j-1]

    return result

def test_swap_1():

    matrix_1 = [[ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15, 16]]

    matrix_1_r = [[1,  5,  9, 13],
                 [ 2,  6, 10, 14],
                 [ 3,  7, 11, 15],
                 [ 4,  8, 12, 16]]

    matrix_2 = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]

    matrix_2_r = [[1, 4, 7],
                  [2, 5, 8],
                  [3, 6, 9]]

    assert swap(matrix_1) == matrix_1_r
    assert swap(matrix_2) == matrix_2_r

