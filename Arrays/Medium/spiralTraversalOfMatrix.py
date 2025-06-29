def spiralTraversal(mat):
    n = len(mat)-1 # Row
    m = len(mat[0])-1 # Column

    left = 0
    right = n
    top = 0
    bottom = m

    while top <= bottom and left <= right:
        # Left to Right
        for i in range(left, right+1):
           print(mat[top][i])

        top += 1

        # Top to Bottom
        for i in range(top, bottom+1):
           print(mat[i][right])

        right -= 1

        # Bottom to Left
        if top <= bottom:
            for i in range(right, left-1, -1):
                print(mat[bottom][i])

            bottom -= 1

        if left <= right:

            for i in range(bottom, top, -1):
                print(mat[i][left])

            left += 1

    print(mat)


input_matrix = [[ 1, 2, 3, 4 ],
		      [ 5, 6, 7, 8 ],
		      [ 9, 10, 11, 12 ],
	              [ 13, 14, 15, 16 ]]
spiralTraversal(input_matrix)