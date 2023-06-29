# Напишите однострочный генератор словаря, который принимает на вход
# три списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии

def make_salary(names, salaries, premiums):
    return {name: salary * float(premium[:-1]) / 100 for name, salary, premium in zip(names, salaries, premiums)}


name = ['Ваня', 'Саша', 'Миша']
salary = [100_000, 150_000, 200_000]
premium = ['5.25%', '7.5%', '10%']

print(make_salary(name, salary, premium))