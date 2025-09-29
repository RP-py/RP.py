dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

numero = int(input("Introduce un número del 1 al 7: "))

if 1 <= numero <= 7:
    print("El día correspondiente es:", dias_semana[numero - 1])
else:
    print("Número fuera de rango. Debe estar entre 1 y 7.")

tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
concatenada = tupla_1 + tupla_2
print(concatenada * 3)
print("la longitud de la tupla concatenada es: ", len(concatenada))

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("EL numero mayor es: ", max(numeros))
print("El numero menor es: ", min(numeros))
print("La suma de los numeros es: ", sum(numeros))