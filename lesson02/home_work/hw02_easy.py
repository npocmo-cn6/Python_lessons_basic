# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Lesson 2 - Easy - Task 1")
fruit_list = ["яблоко", "банан", "киви", "арбуз"]
i = 1

for n in fruit_list:
    print("{}. {:>6}".format(i, n))
    i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("Lesson 2 - Easy - Task 2")
first_list = ["яблоко", "картофель", "банан", "огурец", "киви", "томат", "арбуз"]
second_list = ["яблоко", "банан", "киви", "арбуз", "тыква"]
print(f"Elements of the first list: {first_list}")
print(f"Elements of the second list: {second_list}")
first_set = set(first_list)
second_set = set(second_list)
print(f"Next elements will be removed from the first list: {first_set & second_set}")
first_list = [first_set - second_set]
print(f"Elements of updated first list: {first_list}\n")


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Lesson 2 - Easy - Task 3")
# Способ с дополнительным массивом
# Задаем начальный список целых чисел. Пусть будет от 1 до 100
num_list = list(range(1, 101))
new_list = []
for n in num_list:
    if n % 2 == 0:
        new_list.append(n / 4)
    else:
        new_list.append(n * 2)
print(new_list)

# Способ с одним массивом и с проверкой типа элемента массива перед арифметическими операциями.
# Задаем начальный список целых чисел. Пусть будет от 1 до 100
num_list = list(range(1, 101))
# Добавим 101 элеметом строку для проверки контроля
num_list.append("test")
for n in range(len(num_list)):
    # Убедимся, что работаем с числом
    if type(num_list[n]) == int or type(num_list[n]) == float:
        if num_list[n] % 2 == 0:
            num_list[n] = num_list[n] / 4
        else:
            num_list[n] = (num_list[n]) * 2
    else:
        print(f"Element #{n+1} is not a number - {num_list[n]}")
print(num_list)
