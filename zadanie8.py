imiona = ['Tomek','Ewa','Michal', 'Monika', 'Konrad']

print(imiona[0])
print(imiona[1])
print(imiona[2])

for i in imiona:
    print(i)

for j in range(0,3):
    print("idx: "+ str(j) +" : " + imiona[j])

print("--------------------")
print(" +".join(imiona))
arr = "a,b,,c,d,e,,f,g".split(',,')
print(arr)
