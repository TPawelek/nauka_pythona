def counter():
    global int_word
    balance = 0
    word = ''

    while word != 'q':
        print('--------------------------------------------------------------')
        print('                      STAN KONTA: ' + str(balance))
        print('--------------------------------------------------------------')
        word = input("1.Wpisz '+' oraz kwote, aby wplacic pieniadze"
                     "\n2.Wpisz '-' oraz kwote, aby wyplacic pieniadze"
                     "\n3.Wpisz 'q' aby zakonczyc: ")
        try:
            int_word = int(word[1::])
        except ValueError:
            print()

        check_plus = word.startswith('+')
        check_minus = word.startswith('-')

        if check_plus:
            balance += int_word
            print(balance)
        elif check_minus:
            balance -= int_word
            print(balance)


counter()
