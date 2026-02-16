#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

import time
from typing import List

# Ejercicio 3.1 - Comparar búsqueda lineal vs binaria
def busqueda_lineal(lista: List[int], valor: int) -> int:
    """
    Implementa búsqueda lineal en una lista.
    
    Args:
        lista (List[int]): Lista de enteros
        valor (int): Valor a buscar
        
    Returns:
        int: Índice del elemento o -1 si no se encuentra
    """
    # COMPLEJIDAD TEMPORAL: O(n)
    # En el peor caso, se necesita revisar cada elemento de la lista.
    # COMPLEJIDAD ESPACIAL: O(1)
    # Solo se usan variables auxiliares
    # recorre la lista
    for i in range(len(lista)):
        # compara cada elemento con el valor buscado
        if lista[i] == valor:
            # si se encuentra el valor, retornar su índice
            return i
    # Si no se encuentra el elemento, retornar -1
    return -1

def busqueda_binaria(lista: List[int], valor: int) -> int:
    """
    Implementa búsqueda binaria en una lista ordenada.
    
    Args:
        lista (List[int]): Lista de enteros ordenada
        valor (int): Valor a buscar
        
    Returns:
        int: Índice del elemento o -1 si no se encuentra
    """
    # COMPLEJIDAD TEMPORAL: O(log n)
    # En cada paso, se divide el espacio de búsqueda a la mitad.
    # COMPLEJIDAD ESPACIAL: O(1)
    # Solo se usan variables auxiliares
    izquierda = 0
    derecha = len(lista) - 1
    
    # recorre la lista mientras el índice izquierdo sea menor o igual al derecho
    while izquierda <= derecha:
        # calcula el índice medio
        medio = (izquierda + derecha) // 2
        
        # compara el elemento medio con el valor buscado
        if lista[medio] == valor:
            # retorna el índice del elemento si se encuentra
            return medio
        # si el valor buscado es mayor que el elemento medio, se busca en la mitad derecha
        elif lista[medio] < valor:
            izquierda = medio + 1
        # si el valor buscado es menor que el elemento medio, se busca en la mitad izquierda
        else:
            derecha = medio - 1
            
    # Si no se encuentra el elemento, retornar -1
    return -1

def medir_tiempo(funcion, lista, valor, repeticiones=500) -> float:
    """
    Mide el tiempo de ejecución de una función.
    
    Args:
        funcion: Función a medir
        lista: Lista de enteros
        valor: Valor a buscar
        repeticiones: Número de repeticiones para promediar el tiempo
        
    Returns:
        float: Tiempo promedio de ejecución en segundos
    """
    inicio = time.perf_counter()
    
    for _ in range(repeticiones):
        funcion(lista, valor)
        
    fin = time.perf_counter()
    
    tiempo_promedio = ((fin - inicio) / repeticiones) * 1000  # Convertir a milisegundos
        
    return tiempo_promedio

tamaños = [1000, 10000, 100000]

print(f"==================================================================")
print(f"==============COMPARACIÓN BÚSQUEDA LINEAL VS BINARIA==============")
print(f"{'n':>10} | {'Lineal (ms)':>15} | {'Binaria (ms)':>15}")
print(f"==================================================================")

for n in tamaños:
    
    # Crear una lista ordenada de tamaño n
    lista = list(range(1, n + 1))
    # Buscar el último elemento para el peor caso
    valor_a_buscar = n  + 1
    
    tiempo_lineal = medir_tiempo(busqueda_lineal, lista, valor_a_buscar)
    tiempo_binario = medir_tiempo(busqueda_binaria, lista, valor_a_buscar)
    
    print(f"{n:>10} | {tiempo_lineal:>15.4f} | {tiempo_binario:>15.4f}")
    
print(f"==================================================================")

# Conclusión:
# La búsqueda lineal es O(n) el tiempo crece proporcionalmente al tamaño de la lista.
# La búsqueda binaria es O(log n) el tiempo crece mucho más lentamente, incluso para listas grandes.
# Para listas grades, la binaria es mucho más eficiente.