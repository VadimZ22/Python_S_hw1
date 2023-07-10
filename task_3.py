# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint



num = randint(0, 1000)
count = 10
user_num = -1
for i in range(10):
    user_num = int(input(f'Угадайте число от 1 до 1000, у Вас {count} попыток: '))
    if user_num == num:
        print('Вы угадали!')
        break
    else:
        if num > user_num:
            print('Больше!')
        else:
            print('Меньше!')
        count -=1

if num != user_num:
    print('Вы проиграли(')


