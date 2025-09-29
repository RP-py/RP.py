#quitar repetidos
lista = [1,1,2,3,4,5,6,7,8,9]
eliminar = []
for numero in lista:
    if lista.count(numero) == 1:
        eliminar.append(numero)
print(eliminar)
    