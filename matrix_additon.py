def matrix_addition(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]

m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
print(matrix_addition(m1, m2))