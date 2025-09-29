tamano = int(input("ingresa el tamaño del arbol: "))
for i in range(tamano):
    espacios = " " * (tamano - i - 1)
    asterisco = "*" * (2 * i + 1)
    print(espacios + asterisco)
palito = " " * (tamano - 1)
print(palito + "|")