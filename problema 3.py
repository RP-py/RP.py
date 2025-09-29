lista = [3, 2, 5, 1, 4]
listA = len(lista)
for i in range(listA):
    for j in range(listA - 1 - i):
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp
print("lista ordenada:", lista)