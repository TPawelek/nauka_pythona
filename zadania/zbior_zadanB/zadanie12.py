def counter():
    word = input("Wpisz cos: ").replace(' ', '')
    number_counter = 0
    letter_counter = 0
    print(word)
    for i in word:
        b = i.isalpha()
        if b:
            letter_counter += 1
        else:
            number_counter += 1
    print('LITERY: ' + str(letter_counter))
    print('LICZBY: ' + str(number_counter))


counter()
