import random


def gen_number(min, max):
    return random.randint(min, max)


def draw(*args):
    num = gen_number(0,len(args)-1)
    print(num)
    for i in range(0, len(args)):
        if num == i:
            print('Wygral: ' + str(args[i]))


draw('Justi', 'Tomek', 'Tymka')


