# Transposing a Matrix using zip
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using zip to transpose the matrix
transposed_matrix = list(zip(*matrix))

# Displaying the transposed matrix
for row in transposed_matrix:
    print(row)
