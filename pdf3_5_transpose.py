def transpose_matrix(matrix):
    ans = []
    row_in = len(matrix)
    col_in = len(matrix[0])
    for i in range(row_in):
        tmp = []
        for j in range(col_in):
            tmp.append(matrix[j][i])
        ans.append(tmp)
    return(ans)

    assert transpose_matrix([[1,2,3], [4,5,6], [7,8,9]]) == [[1,4,7], [2,5,8], [3,6,9]]