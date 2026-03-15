#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 2
# Teorema Maestro Recursiones Divisoras
"""
    T(n) = 
        f(n) -> si 0 <= n < n indice 0
        a*T(n/b)+g(n) -> si n >= n indice 0
"""
# -------------------------------------------------------------------------
# T(n) = 4T(n/2) + n^2
# -------------------------------------------------------------------------
# prueba de escritorio
# a = 4
# b = 2
# f(n) = n^2
# g = n^2
# -------------------------------------------------------------------------
# n^(log base (b)^a)
# n(log base 2^4) => (log base 2^4) = 2
# n^2 = n^2
# -------------------------------------------------------------------------
# comparación
# f(n) =  θ(n^log base b^a)
# se aplica el caso
# t(n) = θ(n^log(base b^a) * log(n))
# -------------------------------------------------------------------------
# resultado final
# t(n) =  θ(n^2 log(n))
# -------------------------------------------------------------------------
def T(n):
    if n <= 1:
        return 1
    return 4 * T(n//2) + n**2

for i in [1,2,4,8,16,32,64,128]:
    print(f" n = {i} => t(n) = {T(i)}")