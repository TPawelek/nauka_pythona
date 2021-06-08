start_punkt = [0, 0]
step_count = 0
word = ''

while word != 'q':
    print('-' * 61)
    print('                      Liczba Krokow: ' + str(tuple(start_punkt)))
    print('-' * 61)
    word = input("1.Wpisz 'UP' oraz liczbe krokow"
                 "\n2.Wpisz 'DOWN' oraz liczbe krokow"
                 "\n3.Wpisz 'LEFT' oraz liczbe krokow"
                 "\n4.Wpisz 'RIGHT' oraz liczbe krokow"
                 "\n5.Wpisz 'q' aby zakonczyc: ")
    try:
        step_count = int(word[len(word) - 1])
    except ValueError:
        print()
    up = word.upper().startswith('UP')
    down = word.upper().startswith('DOWN')
    left = word.upper().startswith('LEFT')
    right = word.upper().startswith('RIGHT')

    if up:
        start_punkt[0] += step_count
    elif down:
        start_punkt[0] -= step_count
    elif left:
        start_punkt[1] += step_count
    elif right:
        start_punkt[1] -= step_count

s_start_punkt = str(start_punkt)
print(round(float(s_start_punkt.
    replace("-","").
    replace(",", ".").
    replace(" ", "").
    replace("[", "").
    replace("]", ""))))
