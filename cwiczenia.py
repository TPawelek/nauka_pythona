


cart = {'ser': 27,
        'mleko' : 3,
        'kawa': 30,
        'orzechy': 10,
        'jogurt': 1,
        'woda': 2}

min_Price = 0
sum_price = 0

r1 = False # jesli wiecej niz 3 rzeczy to 5% rabatu
r2 = False # jesli wartosc koszyka wieksza niz 500 zl to 10 % rabatu
r3 = False  # najtanszy produkt gratis
r4 = True # co trzeci produkt gratis

    #R1
if len(cart) >= 3 and r1 == True and r2 == False:
    sum_price = sum_price - (sum_price * 0.05)
    r1 == True
    r2 == False
    print(sum_price)
    #R2
elif sum(price_list) >= 500 and r2 == True and r1 == False:
    sum_price = sum_price - (sum_price * 0.10)
    r1 == False
    r2 == True
    print(sum_price)
    #R3
elif len(cart) >=1 and r3 == True:
    min_Price = min(price_list)
    sum_price = sum_price - min_Price
    print(sum_price)
    #R4
elif len(cart) >=3 and r4 == True:
    for idx in range (2, len(cart), 3):
        sum_price = sum_price - (price_list[idx])
    print(sum_price)