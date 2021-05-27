def numbers():
    numbers_list = (input('Podaj liczby po przecinku: '))
    num = ()
    numbers_list = numbers_list.split(',')
    for i in numbers_list:
        num = num + tuple(i)

    print(numbers_list)
    print(num)


numbers()
