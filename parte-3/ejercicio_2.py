#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 2
"""
Dividir el arreglo en dos mitades.
Encontrar el mínimo y máximo de cada mitad y luego compararlos.
"""
def min_max_divide_venceras(arr, inicio, fin):

    if inicio == fin:
        return arr[inicio], arr[inicio]

    if fin == inicio + 1:
        if arr[inicio] < arr[fin]:
            return arr[inicio], arr[fin]
        else:
            return arr[fin], arr[inicio]

    mitad = (inicio + fin) // 2

    min1, max1 = min_max_divide_venceras(arr, inicio, mitad)
    min2, max2 = min_max_divide_venceras(arr, mitad + 1, fin)

    minimo = min(min1, min2)
    maximo = max(max1, max2)

    return minimo, maximo

arreglo = [34, 12, 7, 89, 45, 2, 100, 23]

minimo, maximo = min_max_divide_venceras(arreglo, 0, len(arreglo)-1)

print("----- MIN Y MAX (DIVIDE Y VENCERÁS) -----")
print("Arreglo:", arreglo)
print("Cantidad de elementos:", len(arreglo))
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("-----------------------------------------")