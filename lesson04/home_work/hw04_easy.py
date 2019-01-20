import random
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst = [random.randrange(1,11) for _ in range(10)]
lst2 = [lst[i] * lst[i] for i, _ in enumerate(lst)]
print(lst)
print(lst2)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst1 = ['apple', 'banana', 'orange', 'lemon', 'fig']
lst2 = ['orange', 'mango', 'kiwi', 'fig', 'lemon']
lst3 = [lst1[i] for i, fruit_lst1 in enumerate(lst1) for j, fruit_lst2 in enumerate(lst2) if lst1[i] == lst2[j]]


print(lst3)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

lst1 = [random.randrange(-100,111) for _ in range(20)]
print(lst1)
lst2 = [lst1[i] for i, num in enumerate(lst1) if (num % 3 == 0 and num > 0 and num % 4 != 0)]
print(lst2)