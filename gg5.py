import os
from typing import Union

import psutil
import sys
import shutil
import getpass


def duplicate_file(filename):       # в нужном месте программы:
    if os.path.isfile(filename):    # имя_функции(аргументы)
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("файл ", newfile, "был успешно создан")
            return True
        else:
            print("Возникли траблы")
            return False


def sys_info():
    print("Вот что я знаю о системе")
    print("Количество процессоров", psutil.cpu_count())
    print("Платформа: ", sys.platform )
    print("Кодировка файловой системы ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь :", os.getlogin())


def del_dublicats(dirname):
    file_list = os.listdir(dirname )
    double_count = 0

    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            double_count += 1
            print("Файл", fullname, "был успешно удалён")
    return double_count


name = input("Ваше имя:")

print(name, ", Hello!")

answer = ''
while answer != 'Q':
    answer = input("Информацию сударь?(Y/N/Q)")
    if answer == 'Y':
        print("отлично сударь")
        print("я могу:")
        print(" [1] - вывести список файлов")
        print(" [2] - вывести информацию о системе")
        print(" [3] - вывести список процессов")
        print(" [4] - продублировать файлы в текущей директории")
        print(" [5] - продублировать выбранные файлы")
        print(" [6] - удаление файлов .dupl")
        do = int(input("укажите номер действия"))

        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущий директории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif do == 5:
            print("=Дублирование указанного файла=")
            filename = input("укажите имя файла:")
            duplicate_file(filename)
        elif do == 6:
            print("Удаление файлов с расширение .dupl")
            dirname = input("Укажите имя директории (текущая директория(.)):")
            count = del_dublicats(dirname)
            print("--Удаленно файлов:", count)
        else:
            pass
    elif answer == 'N':
        print("БАН!")
    elif answer == 'Q':
        print("Программа завершена")
    else:
        print("Что?")
# type, dir, help.
# def имя_функции(аргументы):
#     тело_функции
#     return результат
