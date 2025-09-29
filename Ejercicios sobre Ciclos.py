"Ejercicio 1: Suma de los primeros 50 números"

x = 0
suma = 1
while x <= 50:
    suma = suma + x
    x += 1

print("la suma de los primeros 50 números es: ",suma)

"Ejercicio 2: Contar números impares"

numusuario = int(input("Ingresa un numero: "))
contador = 0
for numero in range(1, numusuario + 1):
    if numero % 2 == 1:
        contador += 1

print ("los numeros impares son: ",contador)

"Ejercicio 3: Factorial de un número"

numpositivo = int(input("Ingresa un numero entero positivo: "))
if numpositivo >= 0:
    factorial = 1
    for i in range(1,numpositivo + 1):
        factorial = factorial * i
    print ("El factorial de: ",numpositivo, "es: ",factorial)

else:
    print("No se puede calcular el factorial")

"Ejercicio 4: Contador de dígitos en un número"

contador = 0
numentero = int(input("Ingresa un numero entero: "))

while numentero > 0:
    numentero = numentero // 10
    contador += 1
print ("El numero tiene estos digitos: ",contador)

"Ejercicio 5: Sumar solo números positivos"

num = 1
suma = 0
while num > 0:
    num = int(input("Ingresa un numero: "))
    if num > 0:
        suma = suma + num
print("La suma de los numeros es: ",suma)

"Ejercicio 6: Encontrar el mayor número"


lista=[]

print("ingresa 10 numeros")

for i in range(0,10):
    valor=int(input("ingresa un numero: "))
    lista.append(valor)

print(f"el numero mas grande es el : {max(lista)}")


"Ejercicio 7: Contar letras en una palabra"

texto = str(input("Ingresa un texto: "))

cuenta = 0
for letra in texto:
        cuenta += 1
print("La cantidad de letras es: ",cuenta)

"Ejercicio 8: Detectar si un número es primo"

primo = int(input("Introduce un número: "))
division = 0

for i in range(1, primo + 1):
    if primo % i == 0:
        division = division + 1
if division == 2:
    print("El numero es primo")
else:
    print ("El numero no es primo")

"Ejercicio 9: Contador de múltiplos"

multi = int(input("Ingresa el numero: "))
a = 1
b = 0
while a <= multi:
    if a % 3 == 0:
        b = b + 1
    a = a + 1
print("La cantidad de numeros que son multiplos de 3 es: ",b)

"Ejercicio 10: Banderas en búsqueda de números negativos"

band_negativa = False  

for i in range(10):
    num = int(input(f"Ingrese el numero: "))
    if num < 0:
        band_negativa = True

if band_negativa:
    print("Se ingresó al menos un número negativo.")
else:
    print("Todos los números ingresados son positivos o cero.")

"Ejercicio 11: Suma de números hasta que el usuario decida detenerse"

suma_total = 0  
while True:
    entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
    
    if entrada.lower() == "fin":  
        break  
    
    numero = float(entrada)  
    suma_total += numero 

print(f"La suma total de los números ingresados es: {suma_total}")

"Ejercicio 12: Imprimir una secuencia de asteriscos"


asteriscos = int(input("Introduce el numero para convertir en asteriscos: "))
for _ in range(asteriscos):
    print("*")

"Ejercicio 13: Acumulador de temperaturas"

temperaturas = 0  
dias = 7  


for i in range(dias):
    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
    temperaturas += temp  


promedio = temperaturas / dias


print("El promedio de temperaturas es: ",promedio)

"Ejercicio 14: Números divisibles entre 5 y 7"

division = int(input("Ingresa un numero: "))
divisible = 0
for numero in range(1, division + 1):
    if numero % 5 == 0 or numero % 7 == 0:
        divisible += 1
print("La cantidad de numeros divisbles entre 5 y 7 son: ",divisible)

"Ejercicio 15: Simulación de inicio de sesión con bandera"


usuario_correcto = "admin"
contrasena_correcta = "123"

acceso_concedido = False

intentos = 0
while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        acceso_concedido = True
        break  
    
    intentos += 1
    print("Incorrecto, vuelve a intentar")

if acceso_concedido:
    print("Acceso concedido.")
else:
    print("Acceso denegado. Se agotaron los intentos.")

"Ejercicio 16: Inversión de un número"

numero = int(input("Ingrese un número entero: "))  
invertido = 0  
while numero > 0:
    digito = numero % 10  
    invertido = invertido * 10 + digito  
    numero = numero // 10 

print("El número invertido es: ",invertido)

"Ejercicio 17: Secuencia de Fibonacci"

n=int(input("escribe el numero limite para la serie fibonacci: "))

lista = [0, 1]
for i in range(2, n):
    lista.append(lista[len(lista)-1] + lista[len(lista)-2])
print(lista)

"Ejercicio 18: Validar entrada de usuario"

while True:
    num1100 = int(input("Ingrese un número entre 1 y 100: "))
    
    if 1 <= num1100 <= 100:
        print("El número ingresado es: ",num1100)
        break  
    else:
        print("Número fuera de rango. Intente nuevamente.")


"Ejercicio 19: Contar palabras en una frase"

frase = input("Ingrese una frase: ")  
palabras = 0 
en_palabra = False  

for caracter in frase:
    if caracter != " " and not en_palabra:
        palabras += 1  
        en_palabra = True  
    
    if caracter == " ":
        en_palabra = False 

print("La frase tiene esta cantidad de palabras: ",palabras)

"Ejercicio 20: Detectar palíndromos"

palabra = input("Ingrese una palabra para verificar si es palindroma: ")  
es_palindromo = True 

i = 0  
j = 0  

for caracter in palabra:
    j += 1  


while i < j // 2:
    if palabra[i] != palabra[j - i - 1]:  
        es_palindromo = False  
        break 
    i += 1  

if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
