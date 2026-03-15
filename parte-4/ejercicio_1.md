El algoritmo es:

```c
int misteri (int n) {
    int f = 1;
    for (int i = 2; i <= n; ++i)
        f *= i;
    return f;
}
```

## ¿Qué hace el algoritmo?

1. Inicializa `f = 1`.
2. Recorre un ciclo desde `i = 2` hasta `n`.
3. En cada iteración multiplica `f` por `i`.

Esto produce:

f = 1 × 2 × 3 × 4 × ... × n

Por lo tanto el algoritmo **calcula el factorial de n**.

n! = 1 × 2 × 3 × ... × n

---

## Ejemplo

Si `n = 5`

```
f = 1
f = 1*2 = 2
f = 2*3 = 6
f = 6*4 = 24
f = 24*5 = 120
```

Resultado:

```
5! = 120
```

---

## Coste en función de n

El ciclo `for` se ejecuta desde `2` hasta `n`.

Número de iteraciones:

n - 1

Cada iteración realiza una operación constante (multiplicación).

Entonces:

T(n) = c(n-1)

En notación asintótica:

T(n) = Θ(n)

---

## Resultado final

**Qué hace el algoritmo**

Calcula el **factorial de n (n!)**

**Complejidad temporal**

Θ(n)

**Complejidad espacial**

Θ(1)