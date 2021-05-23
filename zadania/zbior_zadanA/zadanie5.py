def first_number():
    number = 2
    while number <= 2:
        number = int(input("Podaj liczbe do sprawdzenia: "))

        print("Podaj liczbe wieksza od 2!")
    for i in range(2, number):
        if number % i == 0:
            return print("Podana liczba nie jest liczba pierwsza !")
        return print("Podana liczba jest liczba pierwsza !")


first_number()
