# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

def my_print(k, l):
    for i in range(2, 11):
        for j in range(k, l):
            print(j, 'X', i, '=', j * i, end='\t')
        print()

my_print(2, 6)
print()
my_print(6, 10)