# Better Approach
def setMatrixZero(mat):
    x = [0, 0, 0]
    y = [0, 0, 0]

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if mat[i][j] == 0:
                x[i] = -1
                y[j] = -1

    for i in range(len(x)):
        if x[i] == -1:
            for j in range(len(y)):
                mat[i][j] = 0

    for j in range(len(y)):
        if y[j] == -1:
            for i in range(len(x)):
                mat[i][j] = 0

    print(mat)

input_matrix = [[1,1,1],[1,0,1],[1,1,1]]
setMatrixZero(input_matrix) 

# -------------------------------------------------------   

# Brute Force Attack

# def setMatrixZero(mat):
#     x_len = len(mat[0])
#     y_len = len(mat)

#     for i in range(x_len):
#         for j in range(y_len):
#             if mat[i][j] == 0:
                
#                 # Set x column to -1
#                 for x in range(x_len):
#                     if mat[x][j] != 0:
#                         mat[x][j] = -1

#                 for y in range(y_len):
#                     if mat[i][y] != 0:
#                         mat[i][y] = -1

#     for i in range(x_len):
#         for j in range(y_len):
#             if mat[i][j] == -1:
#                 mat[i][j] = 0

#     print(mat)

# input_matrix = [[1,1,1],[1,0,1],[1,1,1]]
# setMatrixZero(input_matrix) 