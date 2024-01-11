import random

num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    return n == int(n) and 1 <= n <= 100


my_num = int(input())

while my_num != num:
    if is_valid(my_num) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        if my_num < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif my_num > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
    my_num = int(input())

print('Вы угадали, поздравляем!')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
