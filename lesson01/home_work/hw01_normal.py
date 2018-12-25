import math
__author__ = 'Кобзев Илья'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('Lesson 1 Normal task 1')
number = int(input('Введите целое число - '))
if number:
    text = str(number)

    # Вариант для цикла while
    print('Цикл While Loop')
    n = 0
    max_num = 0
    while n < len(text):
        if max_num < int(text[n]):
            max_num = int(text[n])
        else:
            pass
        n += 1
    print('Самая большая цифра в числе ', number, ' - ', max_num)

    # Вариант для цикла for
    print('Цикл For Loop')
    n = 0
    max_num = 0
    for n in text:
        if max_num < int(n):
            max_num = int(n)
        else:
            pass
    print('Самая большая цифра в числе ', number, ' - ', max_num)
else:
    print('Некорректный ввод данных!')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('Lesson 1 Normal task 2')
a = float(input('Введите значение переменной a - '))
b = float(input('Введите значение переменной b - '))
a, b = b, a
print('Новое значение переменной a = ', a)
print('Новое значение переменной b = ', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Lesson 1 Normal task 3')
print('Квадратное уравнение вида ax^2 + bx + c = 0')
a = 1
while True:
    a = int(input('Задайте коэффициент a = '))
    if a:
        break
    else:
        print('a не может равняться нулю')
        continue

b = int(input('Задайте коэффициент b = '))
c = int(input('Задайте коэффициент c = '))
d = b ** 2 - 4 * a * c
print('Дискриминант уравнения равен = ', d)

if d < 0:
    print('Уравнение ', a, '* x^2 +', b, '* x +', c, ' = 0 не имеет решения')
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print('Уравнение ', a, '* x^2 +', b, '* x +', c, ' = 0 имеет один корень: x = ', x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('Уравнение ', a, '* x^2 +', b, '* x +', c, ' = 0 имеет два корня: x1 = ', x1, ', x2 = ', x2)