#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

import tracemalloc
from typing import Generator

# Ejercicio 3.2 - Comparar uso de memoria
# Forma 1: Lista de cuadrados
def cuadrados_lista(n: int) -> list:
    """
    Genera una lista de los cuadrados de los números del 0 al n-1.
    
    Args:
        n (int): Número de elementos
        
    Returns:
        list: Lista de cuadrados
    """
    # COMPLEJIDAD TEMPORAL: O(n)
    # Se necesita iterar n veces para generar la lista.
    # COMPLEJIDAD ESPACIAL: O(n)
    # Se almacena una lista con n elementos.
    return [i**2 for i in range(n)]

# Forma 2:
def cuadrados_generador(n: int) -> Generator[int, None, None]:
    """
    Genera los cuadrados de los números del 0 al n-1 usando un generador.
    
    Args:
        n (int): Número de elementos
    """
    
    # COMPLEJIDAD TEMPORAL: O(n)
    # Se necesita iterar n veces para generar los cuadrados.
    # COMPLEJIDAD ESPACIAL: O(1)
    # No se almacena una lista completa, solo el valor actual.
    for i in range(1, n + 1):
        yield i**2

# función para medir el uso de memoria
def medir_memoria(func, *args) -> int:
    """
    Mide el uso de memoria de una función.
    
    Args:
        func: Función a medir
        *args: Argumentos para la función
    Returns:
        int: Uso de memoria en bytes
    """
    
    tracemalloc.start()

    resultado = func(*args)
    
    memoria_actual, memoria_maxima = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    memoria_pico_mb = memoria_maxima / (1024 * 1024)  # Convertir a MB
    return resultado, memoria_pico_mb

n = 1000000

print(f"==================================================================")
print("COMPARACIÓN DE USO DE MEMORIA ENTRE LISTA Y GENERADOR")
print(f"==================================================================")

# Medir memoria para la lista de cuadrados
_, memoria_lista = medir_memoria(cuadrados_lista, n)
# Medir memoria para el generador de cuadrados
_, memoria_generador = medir_memoria(cuadrados_generador, n)

print(f"\nnúmero de elementos = {n}")
print(f"==================================================================")
print(f"Memoria con lista:      {memoria_lista:.4f} MB")
print(f"Memoria con generador:  {memoria_generador:.4f} MB")
print(f"==================================================================")

# conclusión:
# La lista usa O(n) memoria porque almacena todos los elementos en memoria.
# El generador usa O(1) memoria porque solo mantiene el estado actual y no almacena 
# todos los elementos a la vez.