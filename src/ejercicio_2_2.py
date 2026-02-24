#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# Análisis de algoritmos
# Analiza los siguientes fragmentos de código en Python. Para cada uno, identifica:
# Mejor Caso, Peor Caso la Notación Big O.

# ejercicio 2.2
# Fragmento de código 2
# El salto de índices
def algoritmo_misterioso(n):
    """Analiza el crecimiento de 'i' """
    i = 1
    operaciones = 0
    while i < n:
        operaciones += 1
        i *= 2
    return operaciones

# Mejor caso: O(1)
# Si n es menor o igual a 1, el bucle no se ejecuta y solo se realiza una operación.
n = 1
operaciones = algoritmo_misterioso(n)
print(f"Mejor caso - n: {n}, Operaciones: {operaciones}")

# Peor caso: O(log n)
# Si n es mayor que 1, el bucle se ejecuta logarítmicamente, ya que 'i' se 
# multiplica por 2 en cada iteración.
n = 16
operaciones = algoritmo_misterioso(n)
print(f"Peor caso - n: {n}, Operaciones: {operaciones}")

# Conclusión
# Complejidad temporal:
# Mejor caso: O(1)
# Peor caso: O(log n)
# Notación Big O: O(log n)