from random import randint

N = 10  # количество элементов в списке
arr = [randint(1, 35) for _ in range(N)]
print(arr)

# Проверяем уникальность элементов с помощью преобразования в множество
if len(arr) != len(set(arr)):
    print("Есть одинаковые")
else:
    print("Все элементы уникальны")
