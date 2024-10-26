import math

def calculate_y(x):
    # Вычисляем значение y по формуле
    y = 5 * x + 3 * (x ** 2) * math.sqrt(1 + (math.sin(x) ** 2))
    return y

# Пример использования функции
x_value = float(input("Введите значение x: "))
result = calculate_y(x_value)
print(f"Значение y при x = {x_value}: {result}")
