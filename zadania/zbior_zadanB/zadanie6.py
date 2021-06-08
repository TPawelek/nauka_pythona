def four_finder(*args):
    counter = 0
    print(args)
    for i in args:
        if i == 4:
            counter += 1
    print("W podanej liscie liczba 4 wystepuje {} razy.".format(counter))


four_finder(4, 5, 6, 8, 7, 4, 5, 6, 4, 3)
