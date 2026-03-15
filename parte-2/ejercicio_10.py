#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 8
# Teorema Maestro Recursiones Sustractivas
""" 
    T(n) = 
        f(n) -> si 0 <= n < n indice 0 
        a*T(n-c)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = T(n-2) + n (log(n))
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 1
# c = 2
# f(n) = n log(n)
# g(n) = n log(n)
# -------------------------------------------------------------------------
# expansión de la recurrencia
# T(n) = T(n-2) + n log(n)
# T(n-2) = T(n-4) + (n-2) log(n-2)
# sustituyendo
# T(n) = T(n-4) + (n-2)log(n-2) + nlog(n)
# continuando
# T(n) = T(n-6) + (n-4)log(n-4) + (n-2)log(n-2) + nlog(n)
# T(n) = T(0) + 2log(2) + 4log(4) + 6log(6) + ... + nlog(n)
# -------------------------------------------------------------------------
# suma resultante
# hay aproximadamente n/2 términos
# cada término es proporcional a n log(n)
# suma aproximada:
# Σ n log(n)  ≈  n^2 log(n)
# -------------------------------------------------------------------------
# orden de crecimiento
# T(n) = θ(n^2 log(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) = θ(n^2 log(n))
# -------------------------------------------------------------------------

import math

def T(n):
    if n <= 1:
        return 1
    return T(n-2) + n * math.log(n)

for i in range(1,16):
    print(f" n = {i} => t(n) = {T(i)}")