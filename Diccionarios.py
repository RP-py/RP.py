Agenda = {
    "Angela": "449-1234",
    "Brian": "449-5678",
    "Carlitos": "449-8765"
}
nombre = input("Que nombre vas a buscar?")
if nombre in Agenda:
    print(f"el numero de {nombre} es {Agenda[nombre]}")
else:
    print(f"{nombre} no encontrado")

calificaciones = {
    "matematicas": 8.5,
    "lengua": 9.0,
    "ciencias": 7.5,
}
suma = sum(calificaciones.values())
promedio = suma / len(calificaciones)
print(f"el promedio de {calificaciones} es {promedio}")

productos = {
    "leche": 19,
    "pan": 7.50,
    "huevo": 50,
    "queso": 120,
    "carne": 200,
}
producto = input("que producto vas a buscar? ")
if producto in productos:
    print(f"el precio de {producto} es {productos[producto]}")
else:
    print(f"{producto} no fue eencontrado")

persona = {
    "nombre": "Pancho", "edad": 30, "ciudad": "Aguascalientes"
}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")