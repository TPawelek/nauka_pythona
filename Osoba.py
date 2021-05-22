class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam si " + self.imie + " " + self.nazwisko


class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.indeks = numer_indeksu

    def podaj_numer_indeksu(self):

        return self.indeks


student = Student('Tomasz', 'Pawelek', 432394)
print(student.przedstaw_sie())
