cart = {'ser': 27,
        'mleko': 3,
        'kawa': 30,
        'orzechy': 10,
        'jogurt':  1,
        'woda': 2}

sum_price = 0

for value in cart.values():
    sum_price = sum_price + value

if cart.__contains__('ser') and cart.__contains__('mleko'):
    sum_price = sum_price - (sum_price * 0.10)

print('Wartosc calego koszyka to : ' + str(sum_price) + ' zl')

# Wariacja obliczanie liczby obrazen

hits = {'hit1': 76,
        'hit2': 54,
        'hit3': 54,
        'hit4': 22,
        'hit5': 76,
        'hit6': 26,
        'hit7': 56,
        'hit8': 67}

combo_points = 0
button1 = False
button2 = False
button3 = False
button4 = False
button5 = False
# combo1
if button1 and button2:
    combo_points = hits.get('hit1') + hits.get('hit2')
# combo1
if button1 and button5:
    combo_points = hits.get('hit1') + hits.get('hit5')
# combo2
if button3 and button5:
    combo_points = hits.get('hit7') + hits.get('hit5')
# combo3
if button2 and button3 and button4:
    combo_points = hits.get('hit2') + hits.get('hit7') + hits.get('hit8')
# combo4
if button2 and button3 and button4 and button5:
    combo_points = hits.get('hit2') + hits.get('hit7') + hits.get('hit3')

print(combo_points)
