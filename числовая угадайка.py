import random


def fool_check_lang(n):
    k = n.lower()
    while k != 'en' and k != 'ru' and k != 'анг' and k != 'рус':
        print('Please, enter the valid language (en / ru)', '\n',
              'Пожалуйста, введите подходящий язык (анг / рус)')
        k = input()
    return k


def fool_check_min_max_eng(n, x):
    while int(n) > int(x):
        print('Please, enter the valid numbers, the second one needs to be bigger than the first one')
        n, x = input(), input()
    return int(n), int(x)


def fool_check_min_max_rus(n, x):
    while int(n) > int(x):
        print('Пожалуйста, введите подходящие числа, второе должно быть больше первого')
        n, x = input(), input()
    return int(n), int(x)


def is_valid(n):
    return n == int(n) and minim <= n <= maxim


def eng_ver(my_num, num):
    while my_num != num:
        if is_valid(my_num) == False:
            print(f'Maybe you shoud try an integer in the range from {minim} to {maxim}?')
        else:
            if my_num < num:
                print('Your number is smaller than needed, try again!')
            elif my_num > num:
                print('Your number is bigger than needed, try again!')
        my_num = int(input())


def rus_ver(my_num, num):
    while my_num != num:
        if is_valid(my_num) == False:
            print(f'А может быть все-таки введем целое число в диапазоне от {minim} до {maxim}?')
        else:
            if my_num < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif my_num > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
        my_num = int(input())


print('Добро пожаловать в числовую угадайку\n Welcome to Guess the number')
print('First of all, choose your language: en / ru', '\n',
      'Для начала выбери свой язык: анг / рус')
lang = fool_check_lang(input())

if lang == 'en' or lang == 'анг':
    print('I need two numbers. They will be the minimum and maximum number of your range')
    minim, maxim = fool_check_min_max_eng(input(), input())
    num = random.randint(minim, maxim+1)
    print('I\'ve chosen the number\nEnter your guess:')
    my_num = int(input())
    eng_ver(my_num, num)
    print('Congratulations, you\'ve guessed the number!')
    print('Thank you for playing this Guess the number game. See you...')
else:
    print('Мне понадобятся два числа. Это будет минимальное и максимальное количество в вашем диапазоне')
    minim, maxim = fool_check_min_max_rus(input(), input())
    num = random.randint(minim, maxim+1)
    print('Я выбрал число\nВведите свое предположение:')
    my_num = int(input())
    rus_ver(my_num, num)
    print('Вы угадали, поздравляем!')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
