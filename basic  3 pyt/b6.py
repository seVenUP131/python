numbers = [200, 123, -587]

for number in numbers:
    last_digit = abs(number) % 10  
    print(f"Последняя цифра числа {number}: {last_digit}")