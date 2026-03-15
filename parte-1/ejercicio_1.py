#!/usr/bin/env python
# Author : Cristianco9 cristian_cortes_ortiz@hotmail.com

# Ejercicio 1 
# Teorema Maestro Recursiones Divisoras
""" 
    T(n) = 
        f(n) -> si 0 <= n < n indice 0 
        a*T(n/b)+g(n) -> si n >= n indice 0
""" 
# ------------------------------------------------------------------------- 
# T(n) = 2T(n/2) + n 
# ------------------------------------------------------------------------- 
# prueba de escritorio 
# a = 2 
# b = 2 
# f(n) = n 
# g = n 
# ------------------------------------------------------------------------- 
# n^(log base (b)^a)
# n(log base 2^2) => (log base 2^2) = 1
# n^1 = n
# -------------------------------------------------------------------------
# comparación
# f(n) = θ(n^log base b^a)
# se aplica el caso
# t(n) = θ(n^log(base b^a) * log(n)) 
# ------------------------------------------------------------------------- 
# resultado final 
# t(n) = θ(n(log(n))
# -------------------------------------------------------------------------
def T(n): 
    if n <= 1: 
        return 1 
    return 2 * T(n//2) + n 
        
for i in [1,2,4,8,16,32,64,128]: 
    print(f" n = {i} => t(n) = {T(i)}")