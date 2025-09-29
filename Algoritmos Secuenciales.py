#Saludo Personalizado
nombre = input(" Ingresa tu nombre: ")

print(" ola ", nombre)

#Suma de dos Números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
           
print( " la suma es: ", num1 + num2)

#Cálculo del Área de un Triángulo
base = int(input(" Ingresa la base del triangulo: "))
altura = int(input(" Ingresa la altura del triángulo: "))

area = (base * altura) /2
print( "El area es: ", area)

#Conversión de Dólares a Pesos
dolares = int(input(" Ingresa la cantidad de dolares: "))
pesos = (dolares * 17.5)

print( "La conversión de dolares a pesos es: ", pesos)

#Conversión de Grados Celsius a Fahrenheit
Celsius = int(input( "Ingresa los grados celsius: "))
Farenheit = (Celsius * 9/5) +32

print( "Los grados celsius a farenheit es:  ", Farenheit)

#Calculadora de Edad
edad = int(input( " ingresa tu año de nacimiento: "))
años = (2025 - edad)

print( "Tu edad es: ", años)

#7: Cálculo del Perímetro de un Círculo
radio = int(input( "Ingresa el radio del circulo: "))
perímetro = (2 * 3.1416 * radio)

print( "El perímetro del circulo es: ",perímetro)

#Operaciones Básicas
numero1 = int(input( "Ingresa un numero: "))
numero2 = int(input( "Ingresa otro numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(" La suma de los numeros es: ",suma)
print(" La resta de los numero es: ",resta)
print(" La multiplicación de los numeros es: ",multiplicacion)
print(" La división de los numeros es: ",division)

#Descuento en una Compra
precio = int(input("Ingresa el precio original: "))
descuento = int(input("Ingresa el porcentaje de descuento: "))

precio = precio - precio *  descuento / 100
print("El precio con descuento aplicado sería: ",precio)

#Promedio de Tres Calificaciones
calificacion1 = int(input("Ingresa la primera calificación: "))
calificacion2 = int(input("Ingresa la segunda calificación: "))
calificacion3 = int(input("Ingresa la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) /3
print("El promedio es: ", promedio)     