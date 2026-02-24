#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# El Rigor Matemático (Criterio del Límite)

# lim n→∞ f(n)/g(n) = 0 => f(n) es O(g(n))

# ejercicio 1.1
# Demostrar que f(n) = 7n^2 + 5n + 2 es O(n^2)
def f(n):
    """Función f(n) = 7n^2 + 5n + 2"""
    return 7 * n ** 2 + 5 * n + 2

def g(n):
    """Función g(n) = n^2""" 
    return n ** 2

def limite(n):
    """Calcula el límite de f(n)/g(n) cuando n tiende a infinito"""
    return f(n) / g(n)

# Evaluar el límite para diferentes valores de n
lista = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

# Imprimir los resultados del límite para cada valor de n
for n in lista:
    print(f"n: {n}, f(n)/g(n): {limite(n)}")


# A medida que el valor de n aumenta, el valor de f(n)/g(n) se acerca a 7, 
# lo que indica que el límite es 7. Por lo tanto, f(n) es O(n^2).