def conventer():
    score = 0
    number = input("Podaj wysokosc w stopach i calach po przecinkiu:  ")
    cut_number = number.split(',')
    ft = int(cut_number[0])
    inn = int(cut_number[1])

    score = 30.48 * ft + 2.54 * inn
    print('Wynik to: ' + str(score) + 'cm')


conventer()
