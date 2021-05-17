samochody = ['syeran','poloneza']
ilosc = [3,5]

for idx in range( len(samochody)):
    print("idx: {0} {1}".format(idx, samochody[idx]))
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))
    print('----------------------------')

#zadanie zmieione
imiona = ['Justyna','Kasia','Alicja','Seweryn']
ilosc_osob = [2,4,1,5]

for i in range(len(imiona)):
    print("Imie {0} {1}".format(i+1,imiona[i]))
    print("W klasie " + str(ilosc_osob[i]) + " osoby maja na imie " + imiona[i])
