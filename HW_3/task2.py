# В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

LIMIT = 10

text = 'Дизайн языка Python построен вокруг объектно-ориентированной ' \
       'модели программирования. Реализация ООП в Python является хорошо ' \
       'продуманной, но вместе с тем достаточно специфической по сравнению ' \
       'с другими объектно-ориентированными языками. В языке всё является ' \
       'объектами — либо экземплярами классов, либо экземплярами метаклассов. ' \
       'Исключением является базовый встроенный метакласс type. ' \
       'Таким образом, классы на самом деле являются экземплярами метаклассов, ' \
       'а производные метаклассы являются экземплярами метакласса type. ' \
       'Метаклассы являются частью концепции метапрограммирования и предоставляют ' \
       'возможность управления наследованием классов, что позволяет создавать ' \
       'абстрактные классы, регистрировать классы или добавлять в них какой-либо ' \
       'программный интерфейс в рамках библиотеки или фреймворка. ' \
       'Классы по своей сути представляют план или описание того, как создать объект, ' \
       'и хранят в себе описание атрибутов объекта и методов для работы с ним. ' \
       'Парадигма ООП основывается на инкапсуляции, наследовании и полиморфизме. ' \
       'Инкапсуляция в Python представлена возможностью хранения публичных и скрытых ' \
       'атрибутов (полей) в объекте с предоставлением методов для работы с ними, ' \
       'при этом на самом деле все атрибуты являются публичными, но для пометки ' \
       'скрытых атрибутов существует соглашение об именовании. Наследование ' \
       'позволяет создавать производные объекты без необходимости повторного написания ' \
       'кода, а полиморфизм заключается в возможности переопределения любых методов ' \
       'объекта (в Python все методы являются виртуальными), а также в перегрузке ' \
       'методов и операторов. Перегрузка методов в Python реализуется за счёт ' \
       'возможности вызова одного и того же метода с разным набором аргументов. ' \
       'Особенностью Python является возможность модифицировать классы после их объявления, ' \
       'добавляя в них новые атрибуты и методы, также можно модифицировать ' \
       'и сами объекты, в результате чего классы могут использоваться как структуры ' \
       'для хранения произвольных данных. ' \
       'В Python поддерживается множественное наследование. Само по себе множественное ' \
       'наследование является сложным, и его реализации сталкиваются с проблемами ' \
       'разрешения коллизий имён между родительскими классами и с возможным повторным ' \
       'наследованием от одного и того же класса в иерархии. В Python методы вызываются ' \
       'согласно порядку разрешения методов (MRO), который основан на алгоритме ' \
       'C3-линеаризации, в обычных случаях при написании программ не требуется ' \
       'знать принцип работы данного алгоритма, понимание же может потребоваться ' \
       'при создании нетривиальных иерархий классов.'
import string

my_list = text.split()

for i in range(len(my_list)):
    my_list[i] = my_list[i].strip(string.punctuation).lower()

my_list = list(filter(None, my_list))

set_list = set(my_list)

my_dict = {key: my_list.count(key) for (value, key) in enumerate(my_list)}

sort_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

for i in range(LIMIT):
    print('слово   "', list(sort_dict.keys())[i], '"   встречается', list(sort_dict.values())[i], 'раз(а)')
