inicio = int(input("ingresa el numero de inicio: "))
fin = int(input("ingresa el numero final: "))
p1 = input("ingresa una palabra: ")
p2 = input("ingresa otra palabra: ")

for i in range(inicio, fin + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{p1} {p2}")
    elif i % 3 == 0:
        print(f"{p1}")
    elif i % 5 == 0:
        print(f"{p2}")

