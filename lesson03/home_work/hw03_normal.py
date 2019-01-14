# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fibonacci(n, m):
    row = []
    for i in range(n, m + 1):
        row.append(fib(i))
    return row


print(fibonacci(4, 6))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    print(origin_list)


sort_to_max([1, 7, -20, 2.5, 20.5, -110, 457, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter1(func, arr):
    arr = []
    for i in arr:
        if func(i):
            arr.append(i)
    return arr


print(filter1((lambda x: x < 5), [2, 3, 4, 5, 6, 7]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def para(a, b, c, d):
    e = []
    e.append((a[0] + c[0]) / 2)
    e.append((a[1] + c[1]) / 2)
    f = []
    f.append((b[0] + d[0]) / 2)
    f.append((b[1] + d[1]) / 2)
    print('Координаты середин диагоналей параллелограмма: e = {}, f = {}'.format(e, f))
    if e[0] == f[0] and e[1] == f[1]:
        print('Данные точки являются вершинами параллелограмма')
    else:
        print('Данные точки не являются вершинами параллелограмма')


para([2, 4], [-3, 7], [-6, 6], [-1, 3])  # Параллелограмм
para([2, 4], [-3, 7], [-6, 6], [-5, 3])  # Другая фигура
