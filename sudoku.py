def mostrar(tablero):
    for i in range(9):
        for j in range(9):
            valor = tablero[i][j]
            print(valor if valor != 0 else ".", end=" ")
        print()

def es_valido(tablero, fila, col, num):
    for i in range(9):
        if tablero[fila][i] == num:
            return False
    for i in range(9):
        if tablero[i][col] == num:
            return False
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False
    return True

def encontrar_vacio(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return None

def solucion(tablero):
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True
    fila, col = vacio
    for num in range(1, 10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            if solucion(tablero):
                return True
            tablero[fila][col] = 0
    return False

def tablero_inicial():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

def copiar(tablero):
    copia = []
    for fila in tablero:
        nueva = []
        for valor in fila:
            nueva.append(valor)
        copia.append(nueva)
    return copia

def contar_vacios(tablero):
    contador = 0
    for fila in tablero:
        for valor in fila:
            if valor == 0:
                contador += 1
    return contador

def verificar(tablero):
    for fila in range(9):
        for col in range(9):
            num = tablero[fila][col]
            if num != 0:
                tablero[fila][col] = 0
                if not es_valido(tablero, fila, col, num):
                    return False
                tablero[fila][col] = num
    return True

def obtener_solucion():
    tablero = tablero_inicial()
    copia = copiar(tablero)
    if verificar(copia):
        si = solucion(copia)
        if si:
            return copia
    return None

solucion = obtener_solucion()
if solucion:
    mostrar(solucion)
else:
    print("no se pudo resolver")
