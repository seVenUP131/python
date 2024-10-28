matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = []
for j in range(len(matrix[0])):  
    new_row = []
    for i in range(len(matrix)):  
        new_row.append(matrix[i][j])  
    transposed_matrix.append(new_row)  

print(transposed_matrix)