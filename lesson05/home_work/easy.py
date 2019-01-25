import os


def ListDir():
    print(os.listdir())

def GoToFolder():
    folder = input('Введите имя каталога в который необходимо перейти:')
    if os.path.exists(folder):
        print('Успешно перешел')
    else:
        print('Каталог не найден')

def RemoveFolder():
    folder = input('Введите имя каталога который необходимо удалить:')
    if os.path.exists(folder):
        if os.path.isdir(folder):
            os.rmdir(folder)
            print('Каталог удален')
        else:
            print('Указанный объект является файлом, удаление запрещено')
    else:
        print('Каталог не найден')

def CreateDir():
    folder = input('Введите имя каталога который необходимо создать:')
    if not os.path.exists(folder):
        os.mkdir(folder)
        print('Каталог создан')
    else:
        print('Данный каталог уже создан')

def QuitProgram():
    return True