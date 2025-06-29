def rotateMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i, n, 1):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n):
        mat[i].reverse()

    print(mat)

input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix(input_matrix)

# Brute Force Approach
# def rotateMatrix(mat):
#     n = len(mat)
#     new_mat = [[0 for _ in range(n)] for _ in range(n)]

#     # Transpose the matrix
#     for i in range(n):
#         for j in range(n):
#             new_mat[j][n-i-1] = mat[i][j]

#     print(new_mat)

# input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotateMatrix(input_matrix)