#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# Análisis de algoritmos
# Analiza los siguientes fragmentos de código en Python. Para cada uno, identifica:
# Mejor Caso, Peor Caso la Notación Big O.

# ejercicio 2.1
# Fragmento de código 1
# buscador de pares
def buscar_par_especifico(lista, objetivo):
    """Busca un par específico en la lista"""
    # Analiza este código
    pasos = 0
    for i in range(len(lista)):
        pasos += 1
        if lista[i] % 2 == 0 and lista[i] == objetivo:
            return True, pasos
    return False, pasos

# Mejor caso: O(1)
# Si el primer elemento de la lista es el par específico que estamos buscando.
lista = [4, 1, 3, 5, 7]
objetivo = 4
resultado, pasos = buscar_par_especifico(lista, objetivo)
print(f"Resultado: {resultado}, Pasos: {pasos}")

# Peor caso: O(n)
# Si el par específico no está presente en la lista o está al final de la lista.
lista = [1, 3, 5, 7, 4]
objetivo = 4
resultado, pasos = buscar_par_especifico(lista, objetivo)
print(f"Resultado: {resultado}, Pasos: {pasos}")

# Conclusión
# Complejidad temporal:
# Mejor caso: O(1)
# Peor caso: O(n)
# Notación Big O: O(n)