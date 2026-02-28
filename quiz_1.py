#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Quiz-1
# 02-28-2026

# Implementación y diseño de algoritmos
# Escribe una función (puedes usar C++ o pseudocódigo estructurado) que reciba 
# como parámetros un arreglo de números enteros y el tamaño de dicho arreglo.

# Tu objetivo es que la función cumpla con dos requisitos:

# 1. Debe imprimir en pantalla todas las combinaciones posibles de pares de 
# números del arreglo
# (por ejemplo, si el arreglo es [1, 2], debe imprimir 1-1, 1-2, 2-1, 2-2).

# 2. El algoritmo debe tener una complejidad temporal asintótica exacta de O(n^2) 
# en el peor de los casos

# explica brevemente en un par de líneas por qué la estructura que diseñaste 
# garantiza una complejidad de O(n^2).

# arreglo de números
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Longtid del arreglo
size = len(n)

def fn(arr, n):
    """
    función que imprime los pares ordenados de los números del arreglo

    Params:

    arr : array<int>
    n : int

    returns: none
    """
    # Ciclo principal
    # Recorre el desde 0 hasta la longitud del arreglo
    for i in range(n):
        # Ciclo aninado
        # En cada interación imprime la posición de [i] - [j]
        for j in range(n):
            print(f"{arr[i]} - {arr[j]}")

# Ejecución:
fn(n, size)


# Conclusión:
# Es de notación O(n^2) ya que se requiere dos ciclos aninados para poder
# realizar el conteo de pares, el primer ciclo se encarga de recorrer el primer
# elemento del arreglo el cual es (1) y el segundo ciclo recorre cada uno de los
# siguientes valores del arreglo, es decir, desde 1 hasta 9
# [1, 2, 3, 4, 5, 6, 7, 8, 9] y así sucesivamente por cada valor del ciclo.
