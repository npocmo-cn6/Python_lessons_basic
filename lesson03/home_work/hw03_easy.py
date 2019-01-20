# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def num_round(number, ndigits):
    # Проверяем, что в аргументе передали числа
    if type(number) == int or type(number) == float:
        # Вычисляем целую часть
        left_num = int(number)
        # Вычисляем дробную часть
        right_num = str(number).find('.') + 1
        right_num = str(number)[right_num:ndigits+2]
        # Создаем список из дробной части
        right_num_list = []
        for chr in right_num:
            right_num_list.append(int(chr))
        # Индекс элемента в списке, нужен для цикла округления
        rtl_index = len(right_num) - 1
        # Цикл округления, берем цифры начиная с конца списка
        # и округляем их по правилу >5 -> 1, <=5 -> 0
        # Работаем не с нулевым элементом в списке (он же является
        # десятой частью дроби)
        while rtl_index > 0:
            # Если число больше 5, то к предшествующему числу добавляем 1
            # Удаляем ненужный элемент после округления
            # Если меньше 5, то просто удаляем элемент округляя до 0
            if right_num_list[rtl_index] > 5:
                right_num_list[rtl_index-1] = right_num_list[rtl_index-1] + 1
                right_num_list.pop()
            else:
                right_num_list.pop()
            rtl_index -= 1
        # Дошли до нулевого элемента - округляем его
        if right_num_list [0] > 5:
            left_num += 1
        else:
            pass
    else:
        print('Аргументы передаваемые в функцию должны быть числами')
    return left_num

print(num_round(2.1234567, 5))
print(num_round(2.1999967, 5))
print(num_round(2.9999967, 3))
print(num_round(5.59999967, 1)) # Результат: 5
print(num_round(5.59999967, 3)) # Результат: 6

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

from functools import reduce

def lucky_ticket(ticket_number):
    if type(ticket_number) == int and ticket_number > 99999:
        left = str(ticket_number)[:3]
        right = str(ticket_number)[3:]
        ls = reduce(lambda a, x: int(a) + int(x),left)
        rs = reduce(lambda a, x: int(a) + int(x),right)
    else:
        return 'Ошибка, введите число больше 99999'
    if ls == rs:
        return 'Счастливый билет!'
    else:
        return 'Обычный билет'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
