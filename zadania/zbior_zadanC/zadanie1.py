class Conventer:
    tysiace = 0
    setki = 0
    dziesiatki = 0
    jednosci = 0
    input_number = 0

    def get_numbers(self):

        input_number = input("Podaj liczbe do zamiany: ")
        input_number = int(input_number)
        self.input_number = input_number
        if input_number > 9999:
            t = str(input_number)
            t = int(t[:2])
            self.tysiace = t
            s = str(input_number)
            s = int(s[2])
            self.setki = s
            d = str(input_number)
            d = int(d[3])
            self.dziesiatki = d
            j = str(input_number)
            j = int(j[4])
            self.jednosci = j
        elif input_number > 999:
            t = str(input_number)
            t = int(t[0])
            self.tysiace = t
            s = str(input_number)
            s = int(s[1])
            self.setki = s
            d = str(input_number)
            d = int(d[2])
            self.dziesiatki = d
            j = str(input_number)
            j = int(j[3])
            self.jednosci = j
        elif input_number > 99:
            s = str(input_number)
            s = int(s[0])
            self.setki = s
            d = str(input_number)
            d = int(d[1])
            self.dziesiatki = d
            j = str(input_number)
            j = int(j[2])
            self.jednosci = j

        elif input_number > 9:
            d = str(input_number)
            d = int(d[0])
            self.dziesiatki = d
            j = str(input_number)
            j = int(j[1])
            self.jednosci = j
        elif input_number > 0:
            self.jednosci = input_number

        # print("Liczba tysiecy: " + str(self.tysiace))
        # print("Liczba setek: " + str(self.setki))
        # print("Liczba dziesiatek: " + str(self.dziesiatki))
        # print("Liczba jednosci: " + str(self.jednosci))

    def change_numbers(self):
        tysiace_r = ''
        setki_r = ''
        dziesiatki_r = ''
        jednostki_r = ''
        num = {'1': 'I',
               '4': 'IV',
               '5': 'V',
               '9': 'IX',
               '10': 'X',
               '40': 'XL',
               '50': 'L',
               '90': 'XC',
               '100': 'C',
               '400': 'CD',
               '500': 'D',
               '900': 'CM',
               '1000': 'M',
               }
        # Przypisywanie tysiecy
        if self.tysiace > 0:
            tysiace_r = num["1000"] * self.tysiace
        # Przypisywanie setek
        if 0 < self.setki < 4:
            setki_r = num["100"] * self.setki
        elif self.setki == 4:
            setki_r = num["400"]
        elif self.setki == 5:
            setki_r = num["500"]
        elif 5 < self.setki < 9:
            setki_r = num["500"] + num["100"] * (self.setki - 5)
        elif self.setki == 9:
            setki_r = num["900"]
        # Przypisywanie dziesiatek
        if 0 < self.dziesiatki < 4:
            dziesiatki_r = num["10"] * self.dziesiatki
        elif self.dziesiatki == 4:
            dziesiatki_r = num["40"]
        elif self.dziesiatki == 5:
            dziesiatki_r = num["50"]
        elif 5 < self.dziesiatki < 9:
            dziesiatki_r = num["50"] + num["10"] * (self.dziesiatki - 5)
        elif self.dziesiatki == 9:
            dziesiatki_r = num["90"]
        # Przypisywanie jednosci
        if 0 < self.jednosci < 4:
            jednostki_r = num["1"] * self.jednosci
        elif self.jednosci == 4:
            jednostki_r = num["4"]
        elif self.jednosci == 5:
            jednostki_r = num["5"]
        elif 5 < self.jednosci < 9:
            jednostki_r = num["5"] + num["1"] * (self.jednosci - 5)
        elif self.jednosci == 9:
            jednostki_r = num["9"]

        wynik = tysiace_r + setki_r + dziesiatki_r + jednostki_r
        print(f"Liczba: {self.input_number} to w zapisie rzymskim {wynik}")


obiekt1 = Conventer()
obiekt1.get_numbers()
obiekt1.change_numbers()
# MMMMMDCLXXVIII