estudiantes = []
estudiantes_dict = {}

nombre = input("Nombre: ")
grupo = input("Grupo: ")
materias = set(input("Materias (separadas por comas): ").split(','))

est = (nombre, grupo, materias)
estudiantes.append(est)

estudiantes_dict[nombre] = (grupo, materias)

for e in estudiantes:
    print("Nombre:", e[0], "| Grupo:", e[1], "| Materias:", ', '.join(e[2]))

buscar = input("Buscar estudiante por nombre: ")
if buscar in estudiantes_dict:
    g, m = estudiantes_dict[buscar]
    print("Grupo:", g, "| Materias:", ', '.join(m))
else:
    print("No encontrado")

materias_unicas = set()
for g, m in estudiantes_dict.values():
    materias_unicas.update(m)

print("Materias únicas:", ', '.join(materias_unicas))
