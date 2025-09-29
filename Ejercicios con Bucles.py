#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

repetida = str(input("escribe la palabra que se va a repetir diez veces: "))
for i in range(0,10):
    print(repetida)

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Cuantos años tiene la creatura?: "))
contaredad = 0
for i in range(0,edad):
    contaredad += 1
    print("los años cumplidos son: ",contaredad)

#Escribir un programa que pida al usuario un número entero positivo y muestre porpantalla todos los números impares desde 1 hasta ese número separados por comas.

impar = int(input("Escribe un numero entero positivo: "))
for i in range(1, impar + 1, 2):
    print(i)

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

cuenta = int(input("Ingresa un numero positivo entero: "))
for i in range(cuenta, -1, -1):
    print(i, end=", ")

#Ejercicio 5

capital = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual (%): "))
anos = int(input("Número de años: "))

for i in range(1, anos + 1):
    capital *= 1 + interes / 100
    print(i, capital)

#Ejercicio 6

num = int(input("Ingrese un número entero pofabo: "))

for i in range(1, num + 1):
    print("*" * i)

#Ejercicio 7

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j)

#Ejercicio 8

num = int(input("Ingrese un número entero: "))
for i in range(1, num + 1, 2):
    print(*range(i, 0, -2))

#Ejercicio 9

contraseña = "Lirili Larila"

while True:
    contra = input("Introduce la contraseña: ")
    if contra == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, acuerdate wey")


#Ejercicio 10

primo = int(input("Pon un numero: "))
if primo // 2 == 0:
    print("EL numero es primo")
else:
    print("Tu numero no es primo.")

#Ejercicio 11

palabra = input("Ingrese una palabra: ")

i = 0
for letra in palabra:
    i += 1

while i > 0:
    i -= 1
    print(palabra[i])

#Ejercicio 12

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

ola = 0
for l in frase:
    if l == letra:
        ola += 1

print(ola)

#Ejercicio 13

while True:
    texto = input("introduce un texto: ")
    if texto == "salir":
        break
    print(texto)
