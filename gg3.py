import os
import psutil
import sys
name = input("Ваше имя:")

print(name, ", Hello!")

answer = input("Информацию сударь?(Y/N)")
if answer == 'Y':
    print("отлично сударь")
    print("я могу:")
    print(" [1] - вывести список файлов")
    print(" [2] - вывести информацию о системе")
    print(" [3] - вывести список процессов")
    do = int(input("укажите номер действия"))

    if do == 1:
        print(os.listdir())
    elif do == 2:
        print("[1] - имя текущий дирректории")
        print("[2] - имя ОС")
        print("[3] - авторские права")
        print("[4] - информация об ОС")
        print("[5] - версия python")
        per = int(input("Вбирай нужное"))
        if per == 1:
            print(os.getcwd())
        elif per == 2:
            print(os.name)
        elif per == 3:
            print(sys.copyright)
        elif per == 4:
            print(sys.platform)
        elif per == 5:
            print(sys.version)

    elif do == 3:
        print(psutil.pids())
    else:
        pass

elif answer == 'N':
    print("БАН!")
else:
    print("Что?")
# type, dir, help.
