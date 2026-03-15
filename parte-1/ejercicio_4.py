#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 4
# Teorema Maestro Recursiones Divisoras
"""
    T(n) = 
        f(n) -> si 0 <= n < n indice 0
        a*T(n/b)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = 5T(n/2) + n^3
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 5
# b = 2
# f(n) = n^3
# g = n^3
# -------------------------------------------------------------------------
# n^(log base (b)^a)
# n(log base 2^5) => (log base 2^5) = 2.32
# -------------------------------------------------------------------------
# comparación
# f(n) = θ(n^3)
# n^3 crece más rápido que n^2.32
# por lo tanto:
# f(n) = θ(n^(log base b^a + ε))
# se aplica el caso 3
# -------------------------------------------------------------------------
# t(n) = θ(f(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) =  θ(n^3)
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return 5 * T(n//2) + n**3

for i in [1,2,4,8,16,32,64,128]:
    print(f" n = {i} => t(n) = {T(i)}")