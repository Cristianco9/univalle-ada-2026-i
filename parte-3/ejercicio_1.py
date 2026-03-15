#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 1
# Divide y Vencerás
# Suma de un arreglo
"""
Dividir el arreglo en dos partes, sumar cada mitad recursivamente
y luego sumar los resultados.
"""
def suma_divide_venceras(arr, inicio, fin):

    if inicio == fin:
        return arr[inicio]

    mitad = (inicio + fin) // 2

    izquierda = suma_divide_venceras(arr, inicio, mitad)
    derecha = suma_divide_venceras(arr, mitad + 1, fin)

    return izquierda + derecha


arreglo = [1,2,3,4,5,6,7,8]

resultado = suma_divide_venceras(arreglo, 0, len(arreglo)-1)

print("----- SUMA DE ARREGLO (DIVIDE Y VENCERÁS) -----")
print("Arreglo:", arreglo)
print("Cantidad de elementos:", len(arreglo))
print("Suma total:", resultado)
print("-----------------------------------------------")