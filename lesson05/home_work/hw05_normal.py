﻿import easy

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

end = False

while not end:
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('5. Выход')

    try:
        user_input = int(input("Выберите одно из указанных действий"))
        if user_input == 1:
            easy.GoToFolder()
        elif user_input == 2:
            easy.ListDir()
        elif user_input == 3:
            easy.RemoveFolder()
        elif user_input == 4:
            easy.CreateDir()
        elif user_input == 5:
            end = easy.QuitProgram()
        else:
            end = easy.QuitProgram()
    except:
        end = easy.QuitProgram()




