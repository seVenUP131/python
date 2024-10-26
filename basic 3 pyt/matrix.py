def create_square_matrix(size):
    
    numbers = list(range(100, 100 + size * size * 2, 2))
    
    matrix = np.array(numbers).reshape(size, size)
    return matrix

size = int(input("Введите размер квадратной матрицы: "))

matrix = create_square_matrix(size)

print(matrix)