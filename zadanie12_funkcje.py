cart = ['produkt1', 'produkt2', 'produkt3', 'produkt4', 'produkt5', 'produkt6']
price_list = [27, 230, 65, 110, 356, 140]
min_Price = 0
sum_price = sum(price_list)

r1 = False  # jesli wiecej niz 3 rzeczy to 5% rabatu
r2 = False  # jesli wartosc koszyka wieksza niz 500 zl to 10 % rabatu
r3 = False  # najtanszy produkt gratis
r4 = True  # co trzeci produkt gratis


# R1
def discound_r1(self):
    global r1
    global r2
    global sum_price

    if len(cart) >= 3 and r1 is True and r2 is False:
        sum_price = sum_price - (sum_price * 0.05)
        r1 = True
        r2 = False
        print(sum_price)


# R2
def discound_r2():
    global r1
    global r2
    global sum_price

    if sum(price_list) >= 500 and r2 is True and r1 is False:
        sum_price = sum_price - (sum_price * 0.10)
        r1 = False
        r2 = True
        print(sum_price)


# R3
def discound_r3():
    global r3
    global sum_price
    global min_Price

    if len(cart) >= 1 and r3 is True:
        min_Price = min(price_list)
        sum_price = sum_price - min_Price
        print(sum_price)


# R4
def discound_r4():
    global r4
    global sum_price

    if len(cart) >= 3 and r4 is True:
        for idx in range(2, len(cart), 3):
            sum_price = sum_price - (price_list[idx])
    print(sum_price)


discound_r4()
