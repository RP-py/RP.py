# Pide al usuario ingresar números enteros (uno a la vez). La entrada debe detenerse cuando se
# ingrese un número negativo y al final se debe imprimir la suma de todos los números positivos
# ingresados.

suma=0


while True:
    num1 =int(input("dame un numero "))


    if num1 >=0 :
        suma= suma+num1
    else:
        break

print(suma)
#0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# Solicita al usuario ingresar 10 números e imprime cuál es el mayor de ellos.

lista=[]

print("ingresa 10 numeros")

for i in range(0,10):
    valor=int(input("ingresa un numero"))
    lista.append(valor)

print(f"el numero mas grande es el : {max(lista)}")


palabra =str( input("dame una palabra "))
a=0

for letra in palabra:
    a +=1

print(f"la palabra tiene {a} letras")

numero=int(input("dame un nuemero"))

while True:
    if numero == 1 or numero == 0:
        break    
    else:
         numero = numero/2

if numero == 0:
    print("inpar")
else :
    print("par")

num=int(input("dame un numero "))
contador=0
for i in range(1,num+1):
    if i%3 == 0:
        contador +=1
print(contador)


n=int(input("dame un numero limite para la serie fibonacci"))

lista = [0, 1]
for i in range(2, n):
    lista.append(lista[len(lista)-1] + lista[len(lista)-2])
print(lista)