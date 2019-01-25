import os
import sys
from shutil import copyfile

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('Задача-1')
for i in range(1,10):
    dir_path = os.path.join(os.getcwd(),'dir_{}'.format(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Директория {} уже создана'.format(dir_path))
print(os.listdir())
for i in range(1,10):
    dir_path = os.path.join(os.getcwd(),'dir_{}'.format(i))
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Директории {} не существует'.format(dir_path))
print(os.listdir())

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\n Задача-2')
dir_list = os.listdir()
cur_dir = os.getcwd()
print('Список папок в деректории со скриптом:')
for d in dir_list:
    dir_path = os.path.join(cur_dir,d)
    if os.path.isdir(dir_path):
        print(dir_path)
    else:
        pass
o = map(print,os.path.join(cur_dir,y) for y in dir_list)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('\n Задача-3')
copyfile(os.path.realpath(__file__),os.path.realpath(__file__)+'-copy')
print(os.listdir())