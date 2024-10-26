def gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return a  


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    
    
    result = gcd(num1, num2)
    
    
    print(f"Наибольший общий делитель {num1} и {num2} равен {result}.")
except ValueError:
    print("Ошибка: Пожалуйста, введите целые числа.")