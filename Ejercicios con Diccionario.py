# Ejercicio 1
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
moneda = input("Introduce una divisa: ")
if moneda in divisas:
    print("Símbolo:", divisas[moneda])
else:
    print("Divisa no encontrada")

# Ejercicio 2
persona = {}
persona['nombre'] = input("Introduce tu nombre: ")
persona['edad'] = input("Introduce tu edad: ")
persona['direccion'] = input("Introduce tu dirección: ")
persona['telefono'] = input("Introduce tu teléfono: ")
print(persona['nombre'], "tiene", persona['edad'], "años, vive en", persona['direccion'], "y su número de teléfono es", persona['telefono'])

# Ejercicio 3
frutas = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input("¿Qué fruta quieres? ")
kilos = float(input("¿Cuántos kilos? "))
if fruta in frutas:
    precio = frutas[fruta] * kilos
    print("Precio:", precio)
else:
    print("Fruta no disponible")

# Ejercicio 4
meses = {
    '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
    '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
    '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
}
fecha = input("Introduce una fecha (dd/mm/aaaa): ")
dia, mes, anio = fecha.split('/')
print(dia, "de", meses[mes], "de", anio)

# Ejercicio 5
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for asignatura, creditos in asignaturas.items():
    print(asignatura, "tiene", creditos, "créditos")
    total += creditos
print("Total de créditos:", total)

# Ejercicio 6
persona = {}
while True:
    clave = input("Introduce un dato (nombre, edad, sexo, etc.) o escribe 'salir' para terminar: ")
    if clave == 'salir':
        break
    valor = input(f"Introduce el valor para {clave}: ")
    persona[clave] = valor
    print(persona)

# Ejercicio 7
cesta = {}
while True:
    articulo = input("Introduce un artículo o escribe 'salir' para terminar: ")
    if articulo == 'salir':
        break
    precio = float(input("Introduce el precio: "))
    cesta[articulo] = precio
print("Lista de la compra")
total = 0
for articulo, precio in cesta.items():
    print(articulo, precio)
    total += precio
print("Total:", total)

# Ejercicio 8
entrada = input("Introduce palabras en formato español:inglés: ")
pares = entrada.split(',')
diccionario = {}
for par in pares:
    esp, ing = par.split(':')
    diccionario[esp] = ing
frase = input("Escribe una frase en español: ")
palabras = frase.split()
traducida = []
for palabra in palabras:
    if palabra in diccionario:
        traducida.append(diccionario[palabra])
    else:
        traducida.append(palabra)
print(" ".join(traducida))

# Ejercicio 9
facturas = {}
cobrado = 0
while True:
    opcion = input("¿Quieres añadir, pagar o salir? ")
    if opcion == 'añadir':
        numero = input("Número de factura: ")
        coste = float(input("Coste: "))
        facturas[numero] = coste
    elif opcion == 'pagar':
        numero = input("Número de factura a pagar: ")
        if numero in facturas:
            cobrado += facturas.pop(numero)
    elif opcion == 'salir':
        break
    pendiente = sum(facturas.values())
    print("Cobrado:", cobrado)
    print("Pendiente:", pendiente)

# Ejercicio 10
clientes = {}
while True:
    opcion = input("1. Añadir 2. Eliminar 3. Mostrar 4. Listar 5. Preferentes 6. Salir: ")
    if opcion == '1':
        nif = input("Introduce NIF: ")
        nombre = input("Introduce nombre: ")
        direccion = input("Introduce dirección: ")
        telefono = input("Introduce teléfono: ")
        correo = input("Introduce correo: ")
        preferente = input("¿Es preferente (s/n)? ") == 's'
        clientes[nif] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'preferente': preferente}
    elif opcion == '2':
        nif = input("Introduce NIF: ")
        if nif in clientes:
            del clientes[nif]
    elif opcion == '3':
        nif = input("Introduce NIF: ")
        if nif in clientes:
            print(clientes[nif])
    elif opcion == '4':
        for nif, datos in clientes.items():
            print(nif, datos['nombre'])
    elif opcion == '5':
        for nif, datos in clientes.items():
            if datos['preferente']:
                print(nif, datos['nombre'])
    elif opcion == '6':
        break
