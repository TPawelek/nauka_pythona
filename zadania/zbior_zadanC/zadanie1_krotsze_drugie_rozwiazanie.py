rzym = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L",

        40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

x = input("Podaj liczbę całkowitą:")
x = int(x)
x_sorted = sorted(rzym)
x_sorted.reverse()
score = ""
for key in x_sorted:
        while key <= x:
                score += rzym[key]
                x -= key
print(score)
