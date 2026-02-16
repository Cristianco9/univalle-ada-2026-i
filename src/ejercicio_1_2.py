#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

import time
import math
from typing import List, Tuple, Dict
import random

## Ejercicio 1.2 - Operación O(n)

def busqueda_binaria(lista: List[int], valor: int) -> Tuple[int, int]:
    """
    Implementa búsqueda binaria en una lista ordenada.
    
    Args:
        lista (List[int]): Lista ordenada de enteros
        valor (int): Valor a buscar
        
    Returns:
        Tuple[int, int]: (índice del elemento o -1, número de comparaciones)
    """
    # COMPLEJIDAD TEMPORAL: O(log n)
    # En cada iteración, el espacio de búsqueda se reduce a la mitad.
    # el número máximo de iteraciones es O(log n).
    # COMPLEJIDAD ESPACIAL: O(1)
    # Solo se usan variables auxiliares
    
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0
    
    while izquierda <= derecha:
        # Calcular el punto medio
        medio = (izquierda + derecha) // 2
        comparaciones += 1
        
        # Verificar si se encontró el elemento
        if lista[medio] == valor:
            return medio, comparaciones
        # Si el valor es menor, buscar en la mitad izquierda
        elif lista[medio] < valor:
            izquierda = medio + 1
        # Si el valor es mayor, buscar en la mitad derecha
        else:
            derecha = medio - 1
            
    # Si no se encuentra el elemento, retornar -1
    return -1, comparaciones


# Análisis de casos

# mejor caso: el valor se encuentra en el medio de la lista
def analizar_mejor_caso(n: int) -> Dict:
    """
    Analiza el MEJOR CASO: elemento en el centro.
    MEJOR CASO = O(1): Solo se necesita 1 comparación.

    Args:
        n (int): Tamaño de la lista
        
    Returns:
        Dict: Información del análisis
    """
    
    lista = list(range(1, n + 1))
    medio = n // 2
    valor_buscar = lista[medio]  # Elemento en el centro

    inicio = time.perf_counter()
    indice, comparaciones = busqueda_binaria(lista, valor_buscar)
    fin = time.perf_counter()

    tiempo_us = (fin - inicio) * 1_000_000

    return {
        'n': n,
        'caso': 'MEJOR',
        'valor_buscado': valor_buscar,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'tiempo_us': tiempo_us,
        'log_n_teorico': math.log2(n) if n > 0 else 0
    }
    
# Peor caso: el valor no existe en la lista
def analizar_peor_caso_no_existe(n: int) -> Dict:
    """
    Analiza el PEOR CASO: elemento no existe en la lista.
    PEOR CASO = O(log n): Se recorren todos los niveles del árbol binario.

    Args:
        n (int): Tamaño de la lista
        
    Returns:
        Dict: Información del análisis
    """
    lista = list(range(1, n + 1))
    valor_buscar = n + 100  # Valor que no existe

    inicio = time.perf_counter()
    indice, comparaciones = busqueda_binaria(lista, valor_buscar)
    fin = time.perf_counter()

    tiempo_us = (fin - inicio) * 1_000_000

    return {
        'n': n,
        'caso': 'PEOR (no existe)',
        'valor_buscado': valor_buscar,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'tiempo_us': tiempo_us,
        'log_n_teorico': math.log2(n) if n > 0 else 0
    }
    
# Peor caso: el valor se encuentra en el extremo (inicio o fin)
def analizar_peor_caso_extremo(n: int) -> Dict:
    """
    Analiza el PEOR CASO: elemento en el extremo (inicio o fin).
    PEOR CASO = O(log n): Se recorren todos los niveles del árbol binario.

    Args:
        n (int): Tamaño de la lista
        
    Returns:
        Dict: Información del análisis
    """
    lista = list(range(1, n + 1))
    valor_buscar = lista[0]  # Elemento en el inicio

    inicio = time.perf_counter()
    indice, comparaciones = busqueda_binaria(lista, valor_buscar)
    fin = time.perf_counter()

    tiempo_us = (fin - inicio) * 1_000_000

    return {
        'n': n,
        'caso': 'PEOR (extremo)',
        'valor_buscado': valor_buscar,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'tiempo_us': tiempo_us,
        'log_n_teorico': math.log2(n) if n > 0 else 0
    }

# arreglo de números para analizar los casos
valores_n = [10, 100, 1000, 10000]

# Ejecutar análisis para cada valor de n a través de un ciclo y mostrar los 
# resultados de cada caso.
for n in valores_n:
    print("\n")
    print(f"==================================================================")
    print(f"ANÁLISIS PARA n = {n}")
    print(f"==================================================================")

    resultado_mejor = analizar_mejor_caso(n)
    resultado_peor_no_existe = analizar_peor_caso_no_existe(n)
    resultado_peor_extremo = analizar_peor_caso_extremo(n)

    print("\n--- MEJOR CASO ---")
    for clave, valor in resultado_mejor.items():
        print(f"{clave}: {valor}")

    print("\n--- PEOR CASO (NO EXISTE) ---")
    for clave, valor in resultado_peor_no_existe.items():
        print(f"{clave}: {valor}")

    print("\n--- PEOR CASO (EXTREMO) ---")
    for clave, valor in resultado_peor_extremo.items():
        print(f"{clave}: {valor}")
        
# la búsqueda binaria es eficiente para listas ordenadas, 
# con una complejidad de O(log n) en el peor caso.

# al crecer la lista, las comparaciones aumentan muy poco, ya que en cada paso 
# reduce el problema a la mitad.