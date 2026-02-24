#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Objetivo: Demostrar el crecimiento asintótico de funciones mediante límites y 
# analizar/escribir algoritmos eficientes en Python.

# Implementación
# En esta parte debes escribir código que cumpla con las restricciones de 
# eficiencia solicitadas.

# ejercicio 3.1
# Escribe una función en Python llamada interseccion(lista1, lista2) que devuelva 
# los elementos comunes.

import time


# usando bucles anidados (O(n^2))
def implementacion_1(lista1, lista2):
    """Función para encontrar elementos comunes entre 
        dos listas usando bucles anidados"""

    elementos_comunes = []

    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                elementos_comunes.append(lista1[i])
                
    # print("Elementos comunes usando bucles anidados (O(n^2)):")
    print(elementos_comunes)



# usando conjuntos (O(n)) set
def implementacion_2(lista1, lista2):
    """Función para encontrar elementos comunes entre 
        dos listas usando conjuntos (set)"""

    set_lista1 = set(lista1)
    set_lista2 = set(lista2)
    elementos_comunes_set = set_lista1.intersection(set_lista2)
    # print("Elementos comunes usando conjuntos (O(n)):")
    print(list(elementos_comunes_set))

# Listas de datos
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2 = [4, 7, 10, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

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
    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    fn(*args, **kwargs) # ejecuta la función lambda
    fin = time.perf_counter()
    
    tiempo_ejecucion = (fin - inicio) * 1_000_000 
    print(f'{m}')
    print(f'Tiempo de ejecución: {tiempo_ejecucion:.6f}')
    print(f"==================================================================")


calcular_tiempo("Intersección usando bucles anidados (O(n^2))", implementacion_1, lista1, lista2)
calcular_tiempo("Intersección usando conjuntos (O(n))", implementacion_2, lista1, lista2)

# Documentación
# La versión con conjuntos (set) es más rápida porque:
# 1. La complejidad de búsqueda en un conjunto es O(1) en promedio, mientras que 
# en una lista es O(n).

# 2. Al convertir las listas a conjuntos, se eliminan duplicados automáticamente 
# y se optimiza la operación de intersección.

# 3. El algoritmo resultante tiene complejidad temporal O(n + m), donde n y m son
# las longitudes de las listas, en lugar de O(n * m) para el método con bucles 
# anidados.