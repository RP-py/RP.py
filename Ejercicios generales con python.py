"ejercicio 1"

def sueldo():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    sueldo_lunes = 120

    sueldos = []

    sueldos.append(sueldo_lunes)

    for i in range(1, 5):  
        sueldo_nuevo = (2 * sueldos[i-1]) - sueldo_lunes + 34
        sueldos.append(sueldo_nuevo)

   
    for i in range(len(dias)):
        print(dias[i] + ":", sueldos[i])


"ejercicio 2"

def horas():

    horas = int(input("cantidad de minutos a convertir en horas: "))
    horas = horas / 60
    print(f"El numero de horas es :{horas}")


"ejercicio 3"

def biblioteca():

    venta = 38
    libros = 8
    compras = 90

    ventas = (3 * compras) - (0.25 * compras) + (0.30 * compras)

    ganacias = venta * ventas

"ejercicio 4"

def autolavado():
    auto=70
    taxi=auto*1.3
    vagoneta=taxi+(auto*0.2)
    camioneta=vagoneta+(auto*0.2)
    camion=camioneta+(taxi*0.2)+(auto*0.1)

    print(f" {auto}, {taxi}, {vagoneta},  {camioneta},  {camion}")
    print(f"venta de ayer de camiones: {camion*5} ,de vagonetas: {vagoneta*5} y de taxi: {taxi*4}")
    print("el costo total es: ",(camion*5)+(vagoneta*5)+(taxi*4))

"ejercicio 5"

def calificaciones():
    calificaciones = []
    while True:
        calificacion = int(input("Ingresa las calificaiones, escribe un numero negativo para salir: "))
        if calificacion <= -1:
            print("saliste.")
            break
        calificaciones.append(calificacion)


    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Promedio: {promedio}, Calificación más alta: {max(calificaciones)}, Calificación más baja: {min(calificaciones)}")
    else:
        print("no se ingresó ninguna calificación")

"ejercicio 6"

def tiendita():
    compra = 0
    
    while True:
        cantidad = int(input("ingresa la cantidad que quieres comprar o un numero negativo para terminar: "))
        if cantidad <= -1:
            break
        precio = float(input("ingresa el precio del producto: "))
        
        compra += cantidad * precio
    
    impuesto = compra * 0.12
    
    pagar = compra + impuesto
    
    print(f"Total de la compra: ${compra}")
    print(f"Impuesto del 12%: ${impuesto}")
    print(f"Total a pagar: ${pagar}")

"ejercicio 7"

def dinero():
    euro = 0.93  
    peso = 18.52  
    
    dolares = float(input("ingresa la cantidad en dolares: "))
    
    euros = dolares * euro
    peso = dolares * peso
    
    print(f"{dolares} dolares es equivalente a {euros} euros.")
    print(f"{dolares} dolares es equivalente a {peso} pesos.")

"ejercicio 8"

import random

def adivinarnumero():
    alazar = random.randint(1, 100)
    
    print("juguemos a adivinar un numero")
    print("intenta adivinar el numero en el que pienso")
    
    intentos = 0
    
    while True:
        intento = int(input("adivina el numero: "))
        intentos += 1
        
        if intento < alazar:
            print("frio")
        elif intento > alazar:
            print("caliente")
        else:
            print("le atinaste al numero, que pro")
            break  




sueldo()
horas()
biblioteca()
autolavado()
calificaciones()
tiendita()
dinero()
adivinarnumero()



