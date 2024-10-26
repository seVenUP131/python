def diagonal_sums(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(matrix)  # Предполагаем, что матрица квадратная (M x M)

    for i in range(n):
        main_diagonal_sum += matrix[i][i]  # Элементы главной диагонали
        secondary_diagonal_sum += matrix[i][n - 1 - i]  # Элементы побочной диагонали

    return main_diagonal_sum, secondary_diagonal_sum

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_sum, secondary_sum = diagonal_sums(matrix)

print("Сумма главной диагонали:", main_sum)
print("Сумма побочной диагонали:", secondary_sum)