#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 7
# Teorema Maestro Recursiones Sustractivas
""" 
    T(n) = 
        f(n) -> si 0 <= n < n indice 0 
        a*T(n-c)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = T(n-2) + n^2
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 1
# c = 2
# f(n) = n^2
# g(n) = n^2
# -------------------------------------------------------------------------
# expansión de la recurrencia
# T(n) = T(n-2) + n^2
# T(n-2) = T(n-4) + (n-2)^2
# sustituyendo
# T(n) = T(n-4) + (n-2)^2 + n^2
# continuando
# T(n) = T(n-6) + (n-4)^2 + (n-2)^2 + n^2
# T(n) = T(0) + 2^2 + 4^2 + 6^2 + ... + n^2
# -------------------------------------------------------------------------
# suma resultante
# 2^2 + 4^2 + 6^2 + ... + n^2  ≈  (n/2) términos
# suma proporcional a n^3
# -------------------------------------------------------------------------
# orden de crecimiento
# T(n) = θ(n^3)
# -------------------------------------------------------------------------
# resultado final
# t(n) = θ(n^3)
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return T(n-2) + n**2

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(f" n = {i} => t(n) = {T(i)}")