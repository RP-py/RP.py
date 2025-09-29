numero = int(input("Ingresa un numero: "))
if numero > 0:
  print("El numero es positivo")
elif numero == 0:
  print("El numero es igual a 0")
else:
  print("El numero es negativo")

#Escribe un programa que determine si una persona es mayor de edad (18 años o más) o menor de edad
edad = int(input("Ingresa tu edad: "))
if edad > 17:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

#Escribe un programa que determine si un número ingresado por el usuario es par o impar
num = int(input("Ingresa un numero: "))
if num % 2 == 0:
  print("El numero es par")
else:
  print("el numero es impar")

#Escribe un programa que calcule el precio final de un producto después de aplicar un descuento del 10% si el precio es mayor a $100.
precio = int(input("Ingresa el precio: "))
if precio > 100:
  precio = precio - precio *  10 / 100
  print("El precio con descuento es: ",precio)
else:
  print("No se le puede aplicar descuento")

#Crea un programa que evalúe una calificación y determine el nivel del estudiante.
calificacion = int(input("Ingresa la calificacion: "))
if calificacion > 89:
  print("Excelente")
elif calificacion > 79:
  print("Muy bien")
elif calificacion > 69:
  print("Bien")
elif calificacion > 60:
  print("Suficiente")
else:
  print("Reprobado")

#Escribe un programa que determine si un año ingresado es bisiesto.
bisiesto = int(input("Ingresa el año: "))
if bisiesto % 4 == 0:
  print("El año es bisiesto")
elif bisiesto % 400 == 0:
  print("El año es bisiesto")
else:
  print("El año no es bisiesto")

#Clasificación de Triángulos
valor1 = int(input("Ingresa un valor: "))
valor2 = int(input("Ingresa el segundo valor: "))
valor3 = int(input("Ingresa el tercer valor: "))

if valor1 == valor2 == valor3:
  print("El triangulo es equilatero")
elif valor1 == valor2:
  print("El triangulo es isóceles")
elif valor1 == valor3:
  print("El triangulo es isóceles")
elif valor2 == valor3:
  print("El triangulo es isóceles")
else:
  print("El triangulo es escaleno")

 #Crea un programa que convierta una calificación numérica a su equivalente en letra, según una escala personalizada.
calif = int(input("Ingresa tu calificaion numerica del 1 al 10: "))

if calif == 10:
  print("Tu grado es A")
elif calif == 9:
  print("Tu grado es B")
elif calif == 8:
  print("Tu grado es C")
elif calif == 7:
  print("Tu grado es D")
else:
  print("Tu grado es F")

#Escribe un programa que calcule el costo del boleto de transporte según la edad del pasajero.
años = int(input("Ingresa tu edad: "))
if años < 5:
  print("El costo del boleto es gratis")
elif años > 5:
  print("El costo del boleto es de $10")
elif años > 12:
  print("EL costo del boleto es de $20")
elif años > 59:
  print("EL costo del boleto es de $10")

#Escribe un programa que calcule el impuesto a pagar según el salario anual de una persona.
salario = int(input("Ingresa tu salario anual: "))
if salario < 10000:
 salario = salario * 5 / 100
 print("El impuesto a pagar es: ",salario)
elif salario > 10000:
  salario = salario * 10/ 10
  print("El impuesto a pagar es: ",salario)
elif salario > 50000:
  salario = salario * 20/ 100
  print("El impuesto a pagar es: ",salario)