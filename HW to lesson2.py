# Задание 2.1
#  # Напишите программу, которая проверяет здоровье персонажа в игре.
#  # Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
# hp = int(input('Insert hp of personage: '))
# if hp <= 0:
#  print(False)
# else:
#  print(True)

# Задание 2.2
# Напишите программу, которая проверяет является ли введенное число четным. Если да,
# выведите на экран текст “Четное”,а иначе - “Нечетное”
# num = int(input('Введите число: '))
# if num % 2 == 0:
#  print('Четное')
# else:
#  print('Нечетное')

# Задание 2.3
# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Високосный')
# else:
#     print('Невисокосный')
# year = int(input('Введите год: '))            вариант из "ответов"
# if not year%4 and year%100 or not year%400:
#     print('Високосный')
# else:
#     print('Невисокосный')

# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью inpit()
# text = input('Введите текст: ')
# i = int(input('Введите количество повторов: '))
# for i in range(i):
#     print(text)
# text = input('Введите текст: ')
# i = int(input('Введите количество повторов: '))
# x = 1
# while x <= i:
#     print(text)
#     x = x+1
# text = input('Введите текст: ')                           вариант из "ответов"
# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)


