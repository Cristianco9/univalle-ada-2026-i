#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 6
# Teorema Maestro Recursiones Sustractivas
""" 
    T(n) = 
        f(n) -> si 0 <= n < n indice 0 
        a*T(n-c)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = T(n-1) + n
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 1
# c = 1
# f(n) = n
# g(n) = n
# -------------------------------------------------------------------------
# expansión de la recurrencia
# T(n) = T(n-1) + n
# T(n-1) = T(n-2) + (n-1)
# sustituyendo
# T(n) = T(n-2) + (n-1) + n
# continuando
# T(n) = T(n-3) + (n-2) + (n-1) + n
# T(n) = T(1) + 2 + 3 + ... + n
# -------------------------------------------------------------------------
# suma resultante
# 2 + 3 + ... + n ≈ n(n+1)/2
# -------------------------------------------------------------------------
# orden de crecimiento
# T(n) = θ(n^2)
# -------------------------------------------------------------------------
# resultado final
# t(n) = θ(n^2)
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return T(n-1) + n

for i in [1,2,3,4,5,6,7,8]:
    print(f" n = {i} => t(n) = {T(i)}")