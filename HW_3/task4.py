#  Создайте вручную список с повторяющимися элементами.
#  Удалите из него все элементы, которые встречаются дважды.

my_list = [2, 2, 5, 6, 7, 8, 3, 4, 5, 6, 1, 3, 4, 9, 8, 7, 6, 5]

for _ in range(len(my_list)):
    for item in my_list:
        if my_list.count(item) == 2:
            for j in range(2):
                my_list.remove(item)

print(my_list)