
def even_column(matrix):
    # Создаем новый столбец на основе количества единиц в строках
    new_column = []
    
    for row in matrix:
        count_of_ones = row.count(1)  # Считаем количество единиц в строке
        if count_of_ones % 2 == 0:  # Если четное
            new_column.append(0)
        else:  # Если нечетное
            new_column.append(1)

    # Добавляем новый столбец к матрице
    for i in range(len(matrix)):
        matrix[i].append(new_column[i])
    
    return matrix

# Пример использования функции
matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

new_matrix = even_column(matrix)
for row in new_matrix:
    print(row)
