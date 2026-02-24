#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# Implementación
# En esta parte debes escribir código que cumpla con las restricciones de 
# eficiencia solicitadas.

# ejercicio 3.2
# El desafío del crecimiento exponencial
# Escribe una función recursiva para calcular el número de Fibonacci: 
# F(n) = F(n-1) + F(n-2). Analiza por qué esta implementación simple es O(2^n).
# Pregunta técnica: Si n=50, ¿por qué tu computadora probablemente se bloquee al 
# intentar calcularlo?

import time

def fibonacci(n):
    """Función recursiva para calcular el número de Fibonacci"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def calcular_tiempo(m: str, fn, *args, **kwargs):
    """
    Función para calcular el tiempo de ejecución de otra función
    
    :param m: descripción de la función a ejecutar
    :type m: str
    :param fn: función a ejecutar
    :param args: parámetro 1
    :param kwargs: parámetro 2
    """
    
    print(f"==================================================================")
    print(f'{m}')
    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    resultado = fn(*args, **kwargs) # ejecuta la función lambda
    fin = time.perf_counter()
    
    tiempo_ejecucion = (fin - inicio) * 1_000_000 
    
    print(f'Resultado: {resultado}')
    print(f'Tiempo de ejecución: {tiempo_ejecucion:.6f}')
    print(f"==================================================================")



# Prueba la función con n=50
n = 50
calcular_tiempo(f"Calculando Fibonacci({n})", fibonacci, n)

# Análisis de eficiencia:
# La implementación recursiva simple de Fibonacci tiene complejidad O(2^n)
# porque cada llamada genera dos nuevas llamadas recursivas,
# formando un árbol de ejecución exponencial.
#
# El problema no es la profundidad de la recursion (que es n),
# sino la enorme cantidad de llamadas repetidas.
#
# Para n = 50, el número total de llamadas es extremadamente grande
# (del orden de millones), lo que provoca tiempos de ejecución muy altos.