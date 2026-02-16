#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

import time
from typing import List, Tuple

# Ejercicio 2.1 - Búsqueda lineal
def busqueda_lineal(lista: List[int], valor: int) -> Tuple[int, int]:
    """
    Implementa búsqueda lineal en una lista.
    
    Args:
        lista (List[int]): Lista de enteros
        valor (int): Valor a buscar
        
    Returns:
        Tuple[int, int]: (índice del elemento o -1, número de comparaciones)
    """
    # COMPLEJIDAD TEMPORAL: O(n)
    # En el peor caso, se necesita revisar cada elemento de la lista.
    # COMPLEJIDAD ESPACIAL: O(1)
    # Solo se usan variables auxiliares
    
    comparaciones = 0
    
    for i in range(len(lista)):
        # Por cada iteración el contador incrementa en 1
        comparaciones += 1
        # si se encuentra el valor, retornar su índice y el número de comparaciones
        if lista[i] == valor:
            return i, comparaciones
    # Si no se encuentra el elemento, retornar -1 y el número de comparaciones            
    return -1, comparaciones

# función para analizar los casos de la búsqueda lineal
def analizar_casos(n: int):
    """
    Analiza los casos de la búsqueda lineal: mejor caso, caso promedio y peor caso.
    MEJOR CASO = O(1): El elemento se encuentra en la primera posición.
    CASO PROMEDIO = O(n): El elemento se encuentra en la mitad de la lista.
    PEOR CASO = O(n): El elemento no se encuentra en la lista.
    
    :param n: tamaño de la lista
    :type n: int
    """
    lista = list(range(1, n + 1))

    print("\n")
    print(f"==================================================================")
    print(f"ANÁLISIS BÚSQUEDA LINEAL PARA n = {n}")
    print(f"==================================================================")

    # MEJOR CASO (O(1))
    valor_mejor = lista[0]

    indice, comparaciones = busqueda_lineal(lista, valor_mejor)

    print("\n--- MEJOR CASO ---")
    print(f"Valor buscado: {valor_mejor}")
    print(f"Índice encontrado: {indice}")
    print(f"Comparaciones: {comparaciones}")
    print("Complejidad: O(1)")

    # CASO PROMEDIO (O(n))
    valor_promedio = lista[n // 2]

    indice, comparaciones = busqueda_lineal(lista, valor_promedio)

    print("\n--- CASO PROMEDIO ---")
    print(f"Valor buscado: {valor_promedio}")
    print(f"Índice encontrado: {indice}")
    print(f"Comparaciones: {comparaciones}")
    print("Complejidad: O(n)")

    # PEOR CASO (O(n))
    valor_peor = n + 100  # No existe

    indice, comparaciones = busqueda_lineal(lista, valor_peor)

    print("\n--- PEOR CASO ---")
    print(f"Valor buscado: {valor_peor}")
    print(f"Índice encontrado: {indice}")
    print(f"Comparaciones: {comparaciones}")
    print("Complejidad: O(n)")
    

# ejecución de la función para analizar los casos
analizar_casos(10)
analizar_casos(100)

# La búsqueda binaria es más eficiente porque tiene complejidad O(log n), 
# mientras que la búsqueda lineal es O(n).