def maze_runner(arr, directions):
    n = len(arr)
    x,y = 0,0
    for i in range(0,n):
        for j in range(0,n):
            if arr[i][j] == 2:
                x = i
                y = j

    for s in directions:
        if s == 'N' and arr[x - 1][y] != 1:
            arr[x][y]=0
            x,y = x-1,y
            arr[x][y]=2
        if s == 'S' and arr[x + 1][y] != 1:
            arr[x][y] = 0
            x,y = x+1,y
            arr[x][y] = 2
        if s == 'E' and arr[x][y + 1] != 1:
            arr[x][y] = 0
            x,y = x,y+1
            arr[x][y] = 2
        if s == 'W' and arr[x][y - 1] != 1:
            arr[x][y]=0
            x,y = x,y-1
            arr[x][y]=2

    for i in range(n):
        print(arr[i])


maze = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,3],
        [1,0,1,0,1,0,1],
        [0,0,1,0,0,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1],
        [1,2,1,0,1,0,1]]

#print(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
print(maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
#print(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")

#print(maze_runner(maze, ["N", "N", "N", "W", "W"]), "Dead")
#print(maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]), "Dead")