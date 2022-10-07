# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     # периметр квадрата, площадь квадрата и диагональ квадрата.
# from math import sqrt
# def square(x):
#     return (x + x + x + x, x * x, sqrt(x**2 + x**2))
#     print(square())
#
# x = 7
# print(square(x))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
# employee(last_name='Popov', name='Max', age=40, position='web developer')
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     # положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))
#
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# my_list = [20, -3, 15, 2, -1, -21]
# from functools import reduce
# print(reduce(lambda x, y: x*y, my_list))
#
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     # Примените эти функции в качестве методов в другом файле.

from my_calc import *
prod_res = prod(100, 20)
print(prod_res)
div_res1 = divide(45, 9)
print(div_res1)

div_res2 = divide(5, 0)
print(div_res2)

add_res = add(585, 1987)
print(add_res)

remain_res = remain(541, 6)
print(remain_res)

sub_res = subtract(230, 149)
print(sub_res)


def tests():
    assert add(5, 8) == 13, f'Wrong number, actual result is {sum_it(5, 8)}'
    assert prod(10, 6) == 60, f'Wrong number, actual result is {prod(10, 6)}'
    assert divide(10, 0) == "Can't divide by zero", "Shouldn't divide by zero"
    assert subtract(85, 28) == 57,  f'Wrong number, actual result is {subtract(85, 28)}'
    assert remain(9, 4) == 1, f'Wrong number, actual result is {remain(9, 4)}'

tests()