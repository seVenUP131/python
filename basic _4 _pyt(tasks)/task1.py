import math

def calculate_y(a, b):
    text1 = (a ** 2) / 3
    text2 = (a ** 2 + 4) / b
    text3 = math.sqrt(a ** 2 + 4) / 4
    text4 = (a ** 2 + 4) ** (1/3) / 4
    
    y = text1 + text2 + text3 + text4
    return y


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

if b == 0:
    print("Ошибка: деление на ноль!")
else:
    result = calculate_y(a, b)
    print(f"Значение y: {result}")
