lista = [1, 2, 3, 5, 6, 7]
for i in range(len(lista) - 1):
    if lista[i + 1] != lista[i] + 1:
        print("El número faltante es:", lista[i] + 1)
        break

list = [1, 2, 3, 4, 5]
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == 6:
            print("La suma de", list[i], "y", list[j], "es 6")
