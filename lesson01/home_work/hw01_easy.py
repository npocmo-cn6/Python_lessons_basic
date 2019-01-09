
__author__ = 'Кобзев Илья'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

print('Lesson 1 Easy task 1')
number = int(input('Введите целое число - '))
if number:
    text = str(number)
    # Вариант для цикла while
    print('Цикл While Loop')
    n = 0
    while n < len(text):
        print(text[n])
        n += 1

    # Вариант для цикла for
    print('Цикл For Loop')
    n = 0
    for n in text:
        print(n)
else:
    print('Некорректный ввод данных!')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

print('Lesson 1 Easy task 2')
a = float(input('Введите значение переменной a - '))
b = float(input('Введите значение переменной b - '))
c = float(a + b)
a = float(c - a)
b = float(c - a)
print('Новое значение переменной a = ', a)
print('Новое значение переменной b = ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Lesson 1 Easy task 3')
age = int(input("Сколько Вам лет? - "))
if age > 17:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')