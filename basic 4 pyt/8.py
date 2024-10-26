def min_max(matrix):
    if not matrix or not matrix[0]:
        return None, None  #матрица пустая

    min_value = float('inf')
    max_value = float('-inf')
    min_index = (-1, -1)
    max_index = (-1, -1)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value < min_value:
                min_value = value
                min_index = (i, j)
            if value > max_value:
                max_value = value
                max_index = (i, j)

    return min_index, max_index


matrix = [
    [3, 5, 1],
    [7, 2, 8],
    [4, 6, 0]
]

min_index, max_index = min_max(matrix)
print(f"Индексы минимального элемента: {min_index}")
print(f"Индексы максимального элемента: {max_index}")
