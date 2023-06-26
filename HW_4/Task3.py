# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
# операции — функции. Дополнительно сохраняйте все операции поступления и снятия
# средств в список.

BALANCE = 0
OPERATION = 0

def deposit(amount):
    global BALANCE, OPERATION
    BALANCE += amount
    OPERATION += 1
    if OPERATION % 3 == 0:
        BALANCE += BALANCE * 0.03
    if BALANCE > 5000000:
        BALANCE -= BALANCE * 0.1
    return f"Текущий баланс: {BALANCE}"


def withdraw(amount):
    global BALANCE, OPERATION
    if amount > BALANCE:
        print("На счете недостаточно средств")
        return
    commission = amount * 0.015 if amount * 0.015 >= 30 else 30
    if commission > 600:
        commission = 600
    BALANCE -= amount + commission
    OPERATION += 1
    if OPERATION % 3 == 0:
        BALANCE += BALANCE * 0.03
    if BALANCE > 5000000:
        BALANCE -= BALANCE * 0.1
    print(f"Текущий баланс: {BALANCE}")


information_field = """
Действе над счетом
Введите нужное вам действие
1. Пополнение
2. Снятие
0. Выход"""

print(information_field)
choice = int(input("Ваш выбор: "))
match choice:
    case 1:
        amount = int(input("Введите сумму для пополнения: "))
        if amount % 50 != 0:
            print("Сумма должна быть кратной 50 у.е.")
        else:
            deposit(amount)
    case 2:
        amount = int(input("Введите сумму для снятия: "))
        if amount % 50 != 0:
            print("Сумма должна быть кратной 50 у.е.")
        else:
            withdraw(amount)
    case 0:
        print("Выход")