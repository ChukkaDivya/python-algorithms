# Problem Statement
# Given an m × n matrix, if an element is 0, set its entire row and entire column to 0.
# You must do it in-place.

def set_zeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows=[0]*m
    columns=[0]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows[i]=1
                columns[j]=1
    for i in range(m):
        for j in range(n):
            if rows[i] or columns[j]:
                matrix[i][j]=0
    return matrix
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
print(set_zeroes(matrix))