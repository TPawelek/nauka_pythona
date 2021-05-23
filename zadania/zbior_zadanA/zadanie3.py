def strong(n):
    if n > 1:
        return n * strong(n-1)
    else:
        return 1


n = int(input('Podaj liczbe: '))
print('Silnia wynosi ', strong(n))
