#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 7
"""
Búsqueda en una matriz ordenada Dada una matriz 𝑛×𝑛 donde cada fila y cada columna
están ordenadas ascendentemente, diseña un algoritmo basado en Divide y Vencerás 
para encontrar un número en la matriz en tiempo subcuadrático.
"""
# -------------------------------------------------------------------------
# Recurrencia
#
# T(n) =
#   T(n-1) + 1
#
# en cada paso se elimina una fila o una columna
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# resultado
#
# T(n) = θ(n)
#
# mejor que revisar toda la matriz
# θ(n²)
# -------------------------------------------------------------------------
def buscar_matriz(matriz, x):

    n = len(matriz)

    fila = 0
    col = n - 1

    while fila < n and col >= 0:

        if matriz[fila][col] == x:
            return True, fila, col

        elif matriz[fila][col] > x:
            col -= 1

        else:
            fila += 1

    return False, -1, -1


# prueba
matriz = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10,13,14,17]
]

x = 9

encontrado, i, j = buscar_matriz(matriz, x)

print("---- BÚSQUEDA EN MATRIZ ----")
print("Número buscado:", x)

if encontrado:
    print("Encontrado en posición:", (i, j))
else:
    print("No encontrado")

print("-----------------------------")