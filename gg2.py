name = input("Ваше имя")

print(name, ", Hello!")

answer = input("давайте поработаем?(Y/N)")
# if условие_истинности
#    действие_при_истинности
# else:
#     действия_при_неистинности
if answer == 'Y':
    print("Молодец:)")
elif answer == 'N':
    print("БАН!")
else:
    print("Что?")
# pass - пустышка