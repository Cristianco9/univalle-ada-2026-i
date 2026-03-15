#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 5
"""
Implementa el algoritmo Merge Sort para ordenar un arreglo. Escribe la recurrencia 
que lo define y resuélvela.
"""
# -------------------------------------------------------------------------
# Recurrencia
# T(n) =
#   θ(1)              si n = 1
#   2T(n/2) + n       si n > 1
# -------------------------------------------------------------------------
# Teorema Maestro
# a = 2
# b = 2
# f(n) = n
# -------------------------------------------------------------------------
# cálculo
# n^(log₂2) = n
# -------------------------------------------------------------------------
# comparación
# f(n) = θ(n)
# caso 2
# T(n) = θ(n log n)
# -------------------------------------------------------------------------
# resultado
# T(n) = θ(n log n)
# -------------------------------------------------------------------------
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2

    izquierda = merge_sort(arr[:mitad])
    derecha = merge_sort(arr[mitad:])

    return merge(izquierda, derecha)


def merge(izq, der):

    resultado = []
    i = 0
    j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado


# prueba
arreglo = [38, 27, 43, 3, 9, 82, 10]

ordenado = merge_sort(arreglo)

print("----- MERGE SORT -----")
print("Arreglo original:", arreglo)
print("Arreglo ordenado:", ordenado)
print("----------------------")