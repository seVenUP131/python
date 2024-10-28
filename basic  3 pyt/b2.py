cat_a = float(input("Введите длину первого катета (cat_a): "))
cat_b = float(input("Введите длину второго катета (cat_b): "))

area = 0.5 * cat_a * cat_b

hypotenuse = math.sqrt(cat_a**2 + cat_b**2)

print("Площадь прямоугольного треугольника:", area)
print("Гипотенуза треугольника:", hypotenuse)