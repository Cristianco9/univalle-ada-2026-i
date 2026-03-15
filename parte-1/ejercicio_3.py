#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 3
# Teorema Maestro Recursiones Divisoras
"""
    T(n) = 
        f(n) -> si 0 <= n < n indice 0
        a*T(n/b)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = 3T(n/3) + n
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 3
# b = 3
# f(n) = n
# g = n
# -------------------------------------------------------------------------
# n^(log base (b)^a)
# n(log base 3^3) => (log base 3^3) = 1
# n^1 = n
# -------------------------------------------------------------------------
# comparación
# f(n) =  θ(n^log base  b^a)
# se aplica el caso
# t(n) = θ(n^log(base  b^a) * log(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) =  θ(n log(n))
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return 3 * T(n//3) + n

for i in [1,3,9,27,81,243]:
    print(f" n = {i} => t(n) = {T(i)}")
