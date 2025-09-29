
"Crea un programa con una función que calcule el cuadrado de un valor dado (por teclado o directamente)."

def cuadrado():
    numero = int(input("numero al cuadrado: "))
    print("Numero al cuadrado: ",numero ** 2)
    return numero ** 2

cuadrado() 

"Un programa con una función que reciba una lista, la procese y nos devuelva una nueva lista con cada elemento multiplicado por dos."

def lista(a):
    Lista = []
    for i in a:
        Lista.append(i * 2)
        print(Lista)
    return Lista
Lista = [12,23,44]
lista(Lista)

"Crea una calculadora. Puedes usar los menús que vimos en las estructuras de control y cada operación ha de ser una función."

def suma():
   num1 = int(input("Escribe un numero: "))
   num2 = int(input("Esribe otro numero: "))
   Suma = num1 + num2
   print(Suma)
   return Suma

def resta():
     num1 = int(input("Escribe un numero: "))
     num2 = int(input("Esribe otro numero: "))
     Resta = num1 - num2
     print(Resta)
     return Resta

def multi():
    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Esribe otro numero: "))
    Multi = num1*num2
    print(Multi)
    return Multi

def divi():
    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Esribe otro numero: "))
    Divi = num1/num2
    print(Divi)
    return Divi

def poten():
    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Esribe otro numero: "))
    Poten = num1**num2
    print(Poten)
    return Poten
suma()
resta()
multi()
divi()
poten()