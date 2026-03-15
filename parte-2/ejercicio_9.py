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
# T(n) = T(n-3) + n^3
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 1
# c = 3
# f(n) = n^3
# g(n) = n^3
# -------------------------------------------------------------------------
# expansión de la recurrencia
# T(n) = T(n-3) + n^3
# T(n-3) = T(n-6) + (n-3)^3
# sustituyendo
# T(n) = T(n-6) + (n-3)^3 + n^3
# continuando
# T(n) = T(n-9) + (n-6)^3 + (n-3)^3 + n^3
# T(n) = T(0) + 3^3 + 6^3 + 9^3 + ... + n^3
# -------------------------------------------------------------------------
# suma resultante
# hay aproximadamente n/3 términos
# la suma de cubos crece proporcional a n^4
# -------------------------------------------------------------------------
# orden de crecimiento
# T(n) = θ(n^4)
# -------------------------------------------------------------------------
# resultado final
# t(n) = θ(n^4)
# -------------------------------------------------------------------------

def T(n):
    if n <= 1:
        return 1
    return T(n-3) + n**3

for i in range(1,16):
    print(f" n = {i} => t(n) = {T(i)}")