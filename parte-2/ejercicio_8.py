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
# T(n) = T(n-1) + log(n)
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 1
# c = 1
# f(n) = log(n)
# g(n) = log(n)
# -------------------------------------------------------------------------
# expansión de la recurrencia
# T(n) = T(n-1) + log(n)
# T(n-1) = T(n-2) + log(n-1)
# sustituyendo
# T(n) = T(n-2) + log(n-1) + log(n)
# continuando
# T(n) = T(n-3) + log(n-2) + log(n-1) + log(n)
# T(n) = T(1) + log(2) + log(3) + ... + log(n)
# -------------------------------------------------------------------------
# suma resultante
# log(2) + log(3) + ... + log(n)
# = log(n!)
# usando aproximación de Stirling
# log(n!) ≈ n log(n) - n
# -------------------------------------------------------------------------
# orden de crecimiento
# T(n) = θ(n log(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) = θ(n log(n))
# -------------------------------------------------------------------------

import math

def T(n):
    if n <= 1:
        return 1
    return T(n-1) + math.log(n)

for i in range(1,11):
    print(f" n = {i} => t(n) = {T(i)}")