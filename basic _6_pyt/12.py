def find_columns_with_h(matrix, H):
    columns_with_h = []  # Список для столбцов с H
    columns_without_h = []  # Список для столбцов без H

    # Получаем количество столбцов
    num_columns = len(matrix[0]) if matrix else 0

    for j in range(num_columns):
        has_h = False  # Флаг для проверки наличия H в столбце
        
        for i in range(len(matrix)):
            if matrix[i][j] == H:
                has_h = True
                break  # Если нашли H, выходим из внутреннего цикла
        
        if has_h:
            columns_with_h.append(j)  # Добавляем индекс столбца с H
        else:
            columns_without_h.append(j)  # Добавляем индекс столбца без H

    return columns_with_h, columns_without_h

# Пример использования
matrix = [
    [3, 5, 1],
    [7, 2, 8],
    [4, 6, 1]
]

H = 1
columns_with_h, columns_without_h = find_columns_with_h(matrix, H)

print(f"Столбцы с числом {H}: {columns_with_h}")
print(f"Столбцы без числа {H}: {columns_without_h}")
