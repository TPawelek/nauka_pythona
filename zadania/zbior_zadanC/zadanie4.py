class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for i in self.lyrics:
            print(i)


song = Songs(["Sto lat, sto lat! ",
              "Niech zyje, zyje nam!",
              "Nieeech zyje naaam!"])

song.sing()
