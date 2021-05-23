def draw_tree():
    high = int(input("Podaj liczbe galezi: "))
    j = 1
    for i in range(high):
        print(('*' * j).center(high+(high-1)))
        j = j + 2


draw_tree()
