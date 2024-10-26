import math

def calculate_y(x):
    # Вычисляем каждую часть формулы
    text1 = math.pow(math.cos(x ** 2), 2/3)  # Кубический корень от cos^2(x^2)
    text2 = math.sin(2 * x - 1) ** 2         # sin^2(2x - 1)

    # Суммируем части
    y = text1 + text2
    return y

# Пример использования
x = float(input("Введите значение x: "))
result = calculate_y(x)
print(f"Значение y: {result}")
