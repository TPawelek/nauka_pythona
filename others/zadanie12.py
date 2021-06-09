cart = ['produkt1', 'produkt2', 'produkt3', 'produkt4', 'produkt5', 'produkt6']
price_list = [27, 230, 65, 110, 356, 140]
min_Price = 0
sum_price = sum(price_list)

r1 = False  # jesli wiecej niz 3 rzeczy to 5% rabatu
r2 = False  # jesli wartosc koszyka wieksza niz 500 zl to 10 % rabatu
r3 = False  # najtanszy produkt gratis
r4 = True  # co trzeci produkt gratis

# R1
if len(cart) >= 3 and r1 is True and r2 is False:
    sum_price = sum_price - (sum_price * 0.05)
    r1 = True
    r2 = False
    print(sum_price)
# R2
elif sum(price_list) >= 500 and r2 is True and r1 is False:
    sum_price = sum_price - (sum_price * 0.10)
    r1 = False
    r2 = True
    print(sum_price)
# R3
elif len(cart) >= 1 and r3 is True:
    min_Price = min(price_list)
    sum_price = sum_price - min_Price
    print(sum_price)
# R4
elif len(cart) >= 3 and r4 is True:
    for idx in range(2, len(cart), 3):
        sum_price = sum_price - (price_list[idx])
    print(sum_price)
