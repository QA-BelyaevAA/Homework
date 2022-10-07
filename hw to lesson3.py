# # 3.1 Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0], end=', ')
# print(my_list[2][1], end=', ')
# print(my_list[2][2], end=' ')
#
# # 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(sum(filter(lambda x:isinstance(x, int), list_1)))
#
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])
#
#
# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list1 = ['cat', 'dog', 'horse', 'cow']
# list1 = tuple(list1)
# print(list1)
# print(type(list1))
#
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = tuple(input('Введите имена через запятую: ').split(','))
# family_2 = tuple(input('Введите имена через запятую: ').split(','))
# if len(family_1) > len(family_2):
#     print(family_1)
# elif len(family_1) < len(family_2):
#     print(family_2)
# else:
#     print('Equal')
#
#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# film = {
#     'title': 'Terminator_2',
#     'director': 'Jame Cameron',
#     'year': 1995,
#     'budget': 500000,
#     'main actor': 'Arnold Schwarzneger',
#     'slogan': 'I"ll be back'
#
# }
# print(film)
# print(film.keys())
# print(film.values())
# print(film.items())
#
# # 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# print(set(list_1))
#
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# # #
#

