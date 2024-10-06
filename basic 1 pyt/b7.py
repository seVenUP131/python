numbers = [123, 978]


for number in numbers:
    
    if 100 <= number <= 999:
        tens = (number // 10) % 10  
        print(f"Число: {number}, количество десятков: {tens}")
    else:
        print(f"Число: {number} не является трехзначным.")