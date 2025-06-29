def setMatrixZero(mat):
    x_len = len(mat[0])
    y_len = len(mat)

    for i in range(x_len):
        for j in range(y_len):
            if mat[i][j] == 0:
                
                # Set x column to -1
                for x in range(x_len):
                    if mat[x][j] != 0:
                        mat[x][j] = -1

                for y in range(y_len):
                    if mat[i][y] != 0:
                        mat[i][y] = -1

    for i in range(x_len):
        for j in range(y_len):
            if mat[i][j] == -1:
                mat[i][j] = 0

    print(mat)

input_matrix = [[1,1,1],[1,0,1],[1,1,1]]
setMatrixZero(input_matrix)