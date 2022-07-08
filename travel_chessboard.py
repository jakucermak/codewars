def travel_chessboard(s):
    a_x = int(list(s)[1])
    a_y = int(list(s)[3])
    b_x = int(list(s)[6])
    b_y = int(list(s)[8])

    if a_y == b_y or a_x == b_x:

        return 1
    return 0 + travel_chessboard(f"({a_x+1} {a_y})({b_x} {b_y})") + travel_chessboard(f"({a_x} {a_y+1})({b_x} {b_y})")
    + travel_chessboard(f"({a_x+1} {a_y+1})({b_x} {b_y})")


tests = ["(1 1)(3 3)", "(2 3)(4 8)", "(1 8)(4 8)", "(8 1)(8 6)", "(1 2)(8 7)", "(3 6)(8 7)", "(3 1)(7 8)"]
results = [6, 21, 1, 1, 792, 6, 330]

for i in range(len(tests)):
    print(travel_chessboard(tests[i]), results[i])