
haslo1 = 'secret'
haslo2 = 'haslo'

print(haslo1.replace(haslo1[1:(len(haslo1)-1)], ('*'*(len(haslo1)-2))))
print(haslo2.replace(haslo2[1:(len(haslo2)-1)], ('*'*(len(haslo2)-2))))
