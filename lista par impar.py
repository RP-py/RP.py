#eliminar impar mostrar par
lista_numeros = []
for i in range(1,6):
    numeros = int(input("Ingresa cinco numeros: "))
    if numeros % 2 == 0:
        lista_numeros.append(numeros)
print(lista_numeros)