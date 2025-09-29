lista_nombres = []
for i in range(5):
    nombres = str(input("ingresa un nombre: "))
    lista_nombres.append(nombres)
print (lista_nombres)
def inversa():
    lista_nombres.reverse()
    print(lista_nombres)
def contar_nombre():
    max_nombre = ""
    max_repeticiones = 0
    nombres_contados = []

    for nombres in lista_nombres:
        if nombres not in nombres_contados:
            repeticiones = lista_nombres.count(nombres)
            if repeticiones > max_repeticiones:
                max_repeticiones = repeticiones
                max_nombre = nombres
            nombres_contados.append(nombres)

    if max_repeticiones > 1:
        print(f"El nombre que más se repite es {max_nombre} con {max_repeticiones} repeticiones.")
inversa()
contar_nombre()

numeros = [8,2,4,3,1,6,5,7,9]
print(numeros)
def ordenar_lista():
    numeros.sort()
    print(f"los numeros ordenados son {numeros}")
def mayor_menor():
    mayor = max(numeros)
    menor = min(numeros)
    print(f"el numero mayor es {mayor} y el menor es {menor}")
def eliminar():
    numeros.pop()
    print(numeros)
def insertar():
    numeros.insert(1, 99)
    print(numeros)
ordenar_lista()
mayor_menor()
eliminar()
insertar()