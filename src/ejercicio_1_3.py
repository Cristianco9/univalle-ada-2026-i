#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# El Rigor Matemático (Criterio del Límite)

# lim n→∞ f(n)/g(n) = 0 => f(n) es O(g(n))

# ejercicio 1.3
# Determina la relación asintótica entre f(n) = n! (factorial de n) y g(n) = 2^n. 
# ¿Cuál crece más rápido?
# Ayuda: Piensa en qué sucede con la fracción a medida que n se vuelve muy grande.

def factorial(n):
    """Calcula el factorial de n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def g(n):
    """Función g(n) = 2^n"""
    return 2 ** n

def limite(n):
    """Calcula el límite de f(n)/g(n) cuando n tiende a infinito"""
    if g(n) == 0:
        # Evitar división por cero
        return float('inf')
    # Calcular el límite de f(n)/g(n)
    return factorial(n) / g(n)

# Evaluar el límite para diferentes valores de n
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Imprimir los resultados del límite para cada valor de n
for n in lista:
    print(f"n: {n}, f(n)/g(n): {limite(n)}")

# A medida que el valor de n aumenta, el valor de f(n)/g(n) crece sin límite,
# lo que indica que el límite tiende a infinito.
# Por lo tanto, n! crece más rápido que 2^n. Así que, 2^n = O(n!) y n! no es O(2^n).