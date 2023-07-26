# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 0
UPPER_LIMIT = 100000

while True:
    number = int(input('Введите число: '))
    if LOWER_LIMIT < number <= UPPER_LIMIT:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print('Вы ввели составное число')
                break
        else:
            print('Вы ввели простое число')
        break
    else:
        print('Ошибка! Вы ввели число меньше чем', LOWER_LIMIT, 'и больше чем', UPPER_LIMIT, 'Попробуйте еще раз')