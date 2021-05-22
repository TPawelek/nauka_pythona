class Pies:

    gatunek = 'pies domowy'
    Liczba = 14

    def __init__(self, rasa, imie, wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):

        print('hau,hau')

    def prezentuj_psa(self):

        print('rasa to : ' + self.rasa)


reksio = Pies('owczarek', 'gubi', '8')

print(Pies.Liczba)

reksio.prezentuj_psa()
