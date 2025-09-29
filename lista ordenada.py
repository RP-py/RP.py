lista = [2,3,1,6,4,10,9,5,8,7]

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)