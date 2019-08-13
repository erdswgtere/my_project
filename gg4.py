import os
import psutil
import sys
import shutil
import getpass
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
            print("Вот что я знаю о системе")
            print("Количество процессоров", psutil.cpu_count())
            print("Платформа: ", sys.platform)
            print("Кодировка файловой системы ", sys.getfilesystemencoding())
            print("Текущая директория: ", os.getcwd())
            print("Текущий пользователь :", os.getlogin())
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов в текущий директории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i += 1
        elif do == 5:
            print("Копирование выбранного файла")
            print("Выберите порядковый номер файла")
            file_list = os.listdir()
            a = 1
            for i in file_list:
                print(str(a) + "_" + i)
                a += 1
            for i in file_list:
                print(str(a) + "_" + i)
                a += 1
            item = int(input())
            new_file = file_list[item - 1] + ".dupl"
            shutil.copy(file_list[item - 1], new_file)
        elif do == 6:
            print("Удаление файлов с расширение .dupl")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if file_list[i].rfind(".dupl") != -1:
                    os.remove(file_list[i])
                i += 1
        else:
            pass
    elif answer == 'N':
        print("БАН!")
    elif answer == 'Q':
        print("Программ завершена")
    else:
        print("Что?")
# type, dir, help.
