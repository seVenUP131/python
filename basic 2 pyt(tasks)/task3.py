
import math

def calculate_length_of_year(R, v):
    L = (2 * R * math.pi) / v
    return L

def main():
    print("Добро пожаловать в программу для вычисления длины года на планетах!")
    
    # Ввод данных для первой планеты
    print("\nВведите данные для первой планеты:")
    R1 = float(input("Введите радиус орбиты (в миллионах км): "))
    v1 = float(input("Введите орбитальную скорость (в км/ч): "))
    
    # Ввод данных для второй планеты
    print("\nВведите данные для второй планеты:")
    R2 = float(input("Введите радиус орбиты (в миллионах км): "))
    v2 = float(input("Введите орбитальную скорость (в км/ч): "))
    
    # Вычисление длины года
    length_of_year1 = calculate_length_of_year(R1, v1)
    length_of_year2 = calculate_length_of_year(R2, v2)
    
    # Вывод результатов
    print("\nРезультаты:")
    print(f"Длина года на первой планете: {length_of_year1:.2f} часов")
    print(f"Длина года на второй планете: {length_of_year2:.2f} часов")
    
    # Сравнение длины года
    if length_of_year1 > length_of_year2:
        print("На первой планете год длиннее, чем на второй.")
    elif length_of_year1 < length_of_year2:
        print("На второй планете год длиннее, чем на первой.")
    else:
        print("На обеих планетах год имеет одинаковую длину.")

if __name__ == "__main__":
    main()
