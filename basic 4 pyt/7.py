import random


m = int(input("Введите количество строк (M): "))
n = int(input("Введите количество столбцов (N): "))


matrix = []


for i in range(m):
    row = []  
    for j in range(n):
        row.append(random.randint(0, 100))  
    matrix.append(row)  


print("Сгенерированная матрица:")
for row in matrix:
    print(row)
