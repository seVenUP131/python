def calculate_monthly_payment(s, r, n):
    """Расчет ежемесячной выплаты по кредиту."""
    m = s * r * (1 + r) ** n / ((1 + r) ** n - 1)
    return m

def main():
    print("Добро пожаловать в калькулятор кредита!")

    # Ввод данных от пользователя
    s = float(input("Введите сумму займа (в рублях): "))
    i = float(input("Введите годовую процентную ставку (в %): "))
    n = int(input("Введите количество месяцев, на которые взят кредит: "))

    # Преобразование годовой процентной ставки в месячную
    r = (i / 100) / 12

    # Расчет ежемесячной выплаты
    monthly_payment = calculate_monthly_payment(s, r, n)

    # Расчет общей суммы выплат и переплаты
    total_payment = monthly_payment * n
    overpayment = total_payment - s

    # Вывод результатов
    print("\n Результаты:")
    print(f"Ежемесячная выплата: {monthly_payment:.2f} рублей")
    print(f"Общая сумма выплат: {total_payment:.2f} рублей")
    print(f"Переплата: {overpayment:.2f} рублей")

if __name__ == "__main__":
    main()