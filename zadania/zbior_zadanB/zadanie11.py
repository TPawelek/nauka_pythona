def matrix_maker():
    line = int(input("Podaj liczbe wierszy: "))
    column = int(input("Podaj Liczbe kolumn: "))
    table = [[i * j for j in range(column)]for i in range(line)]
    print(table)


matrix_maker()
