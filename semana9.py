#ejercicio 1
def calcular_sueldo():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

    sueldo_lunes = 120

    sueldos = []

    sueldos.append(sueldo_lunes)

    for i in range(1, 5):  
        sueldo_nuevo = (2 * sueldos[i-1]) - sueldo_lunes + 34
        sueldos.append(sueldo_nuevo)

   
    for i in range(len(dias)):
        print(dias[i] + ":", sueldos[i])


#ejercicio 2

def calcular_horas():

    a= int(input("Dame los minutos para hacerlos en horas "))
    print(f"El numero de horas es el siguiente :{a/60}")


#ejercicio 3

def biblioteca():

    venta = 38
    libros = 8
    compra = 90

    dineroventa = (3 * compra) - (0.25 * compra) + (0.30 * compra)

    ganacia = venta * dineroventa

def autolavado():
    auto=70
    taxi=auto*1.3
    vagoneta=taxi+(auto*0.2)
    camioneta=vagoneta+(auto*0.2)
    camion=camioneta+(taxi*0.2)+(auto*0.1)

    print(f"{auto},  {taxi},  {vagoneta},  {camioneta},  {camion}")
    print(f"venta de ayer camiones: {camion*5} ,vagonetas:{vagoneta*5} y taxi {taxi*4}")
    print((camion*5)+(vagoneta*5)+(taxi*4))

def calificaciones():
    calificaciones = []
    while True:
        calificacion = int(input("Ingresa una calificación (entero) (-1 para salir): "))
        if calificacion == -1:
            print("Ciclo detenido.")
            break
        calificaciones.append(calificacion)


    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Promedio: {promedio}, Calificación más alta: {max(calificaciones)}, Calificación más baja: {min(calificaciones)}")
    else:
        print("No se ingresaron calificaciones.")

def tienda():
    compra = 0
    
    while True:
        cantidad = int(input("Ingresa la cantidad del producto (o -1 para finalizar): "))
        if cantidad == -1:
            break
        precio = float(input("Ingresa el precio del producto: "))
        
        compra += cantidad * precio
    
    impuesto = compra * 0.12
    
    pagar = compra + impuesto
    
    print(f"Total de la compra: ${compra:.2f}")
    print(f"Impuesto (12%): ${impuesto:.2f}")
    print(f"Total a pagar: ${pagar:.2f}")

def convertir_dinero():
    cambioEuro = 0.93  # 1 USD = 0.93 EUR
    cambioPeso = 18.52  # 1 USD = 18.52 MXN
    
    usd = float(input("Ingresa la cantidad en dólares (USD): "))
    
    euros = usd * cambioEuro
    peso = usd * cambioPeso
    
    print(f"{usd} USD es equivalente a {euros:.2f} EUR.")
    print(f"{usd} USD es equivalente a {peso:.2f} MXN.")


import random

def adivina_el_numero():
    ale = random.randint(1, 100)
    
    print("¡Bienvenido al juego de adivinanza de números!")
    print("La computadora ha pensado en un número entre 1 y 100.")
    
    intentos = 0
    
    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1
        
        if intento < ale:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > ale:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break  




calcular_sueldo()
calcular_horas()
biblioteca()
autolavado()
calificaciones()
tienda()
convertir_dinero()
adivina_el_numero()
