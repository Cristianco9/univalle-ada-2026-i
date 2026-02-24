#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# El Rigor Matemático (Criterio del Límite)

# lim n→∞ f(n)/g(n) = 0 => f(n) es O(g(n))

# ejercicio 1.2
# Demuestra que la función lineal g(n) = n es una cota superior para la función 
# logarítmica f(n) = log(n). Es decir, demuestra que log(n) = O(n).
import math

def f(n):
    """Función f(n) = log(n)"""
    return math.log(n)

def g(n):
    """Función g(n) = n""" 
    return n

def limite(n):
    """Calcula el límite de f(n)/g(n) cuando n tiende a infinito"""
    if n == 0:
        # Evitar división por cero
        return float('inf')
    # Calcular el límite de f(n)/g(n)
    return f(n) / g(n)

# Evaluar el límite para diferentes valores de n
lista = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

# Imprimir los resultados del límite para cada valor de n
for n in lista:
    print(f"n: {n}, f(n)/g(n): {limite(n)}")

# A medida que el valor de n aumenta, el valor de f(n)/g(n) se acerca a 0, 
# lo que indica que el límite es 0. Por lo tanto, log(n) es O(n).