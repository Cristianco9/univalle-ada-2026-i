#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 5
# Teorema Maestro Recursiones Divisoras
"""
    T(n) = 
        f(n) -> si 0 <= n < n indice 0
        a*T(n/b)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = 7T(n/4) + n^2
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 7
# b = 4
# f(n) = n^2
# g = n^2
# -------------------------------------------------------------------------
# n^(log base (b)^a)
# n(log base 4^7) => (log base 4^7) ≈ 1.40
# n^1.40
# -------------------------------------------------------------------------
# comparación
# f(n) = θ(n^2)
# n^2 crece más rápido que n^1.40
# por lo tanto:
# f(n) = θ(n^(log base b^a + ε))
# se aplica el caso 3
# -------------------------------------------------------------------------
# t(n) = θ(f(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) =  θ(n^2)
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return 7 * T(n//4) + n**2

for i in [1,4,16,64,256]:
    print(f" n = {i} => t(n) = {T(i)}")