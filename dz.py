print("Привет хозяин")
name = input("Ваше имя:")

print(name, ", Hello!")

answer = input('давайте поработаем?(Y/N)')
if answer == 'Y':
    print('Здорово! чем желаете заняться?')
    print('a) запишемся на курс по программированию')
    print('b) почитаем книгу Вирта')
    print('c) посмотрим видео на ютубе')
answer_2 = input("Выбирай")
if answer_2 == 'a':
    print('Заходи на GeekBrains или stepik')
elif answer_2 == 'b':
    print("Беги скачивать книгу!")
elif answer_2 == 'c':
    print('Всё-таки лучше запишись на курс')

elif answer == 'N':
    print('Советую подумать ещё раз:)')

else:
    print('Неизвестный ответ')