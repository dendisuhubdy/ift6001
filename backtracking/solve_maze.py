def solveMaze( Maze , position , N ):
    # returns a list of the paths taken
    if position == ( N - 1 , N - 1 ):
        return [ ( N - 1 , N - 1 ) ]
    x , y = position
    if x + 1 < N and Maze[x+1][y] == 1:
        a = solveMaze( Maze , ( x + 1 , y ) , N )
        if a != None:
            return [ (x , y ) ] + a

    if y + 1 < N and Maze[x][y+1] == 1:
        b = solveMaze( Maze , (x , y + 1) , N )
        if  b != None:
            return [ ( x , y ) ] + b


Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]
        ]

print(solveMaze(Maze,(0,0),5))
