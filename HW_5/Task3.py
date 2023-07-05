# Создайте функцию генератор чисел Фибоначчи
def fib():
    f_0, f_1 = 0, 1
    while True:
        yield f_0
        f_0, f_1 = f_1, f_0 + f_1

fibonacci = iter(fib())
print(fibonacci)
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))