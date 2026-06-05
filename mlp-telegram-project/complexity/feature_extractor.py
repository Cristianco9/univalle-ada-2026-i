"""
feature_extractor.py
--------------------

Módulo encargado de realizar el análisis estático de algoritmos escritos
en Python mediante la inspección de su Árbol de Sintaxis Abstracta (AST).

El objetivo principal de este componente es transformar un fragmento
de código fuente en un vector numérico de características (features)
que represente patrones estructurales relacionados con la complejidad
algorítmica.

Estas características son utilizadas posteriormente como entrada para
la Red Neuronal Multicapa (MLP), encargada de clasificar la complejidad
temporal estimada del algoritmo.

Características extraídas:
--------------------------
1. Número de bucles for.
2. Número de bucles while.
3. Profundidad máxima de anidamiento.
4. Presencia de recursividad.
5. Cantidad de llamadas recursivas.
6. Uso de algoritmos de ordenamiento.
7. Detección de búsqueda binaria.
8. Número total de llamadas a funciones.
9. Cantidad de líneas de código.
10. División entre dos (patrón logarítmico).
11. Bucles secuenciales.
12. Accesos mediante índices o estructuras hash.

Proceso general:
----------------
Código Python
      │
      ▼
 AST Parser
      │
      ▼
 Feature Extraction
      │
      ▼
 Vector de 12 Features
      │
      ▼
 MLP Classifier

Tecnologías utilizadas:
-----------------------
- Python AST
- NumPy
- Static Code Analysis

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import ast
import numpy as np

FEATURE_SIZE = 12


class FeatureExtractor(ast.NodeVisitor):
    """
    Analizador de características basado en el patrón Visitor del módulo AST.

    Recorre cada nodo del árbol sintáctico abstracto generado a partir
    de un algoritmo Python y registra métricas relacionadas con patrones
    de complejidad computacional.

    Attributes
    ----------
    for_loops : int
        Cantidad de bucles for detectados.

    while_loops : int
        Cantidad de bucles while detectados.

    max_depth : int
        Profundidad máxima de anidamiento de bucles.

    recursive_calls : int
        Número de llamadas recursivas encontradas.

    function_names : set
        Conjunto de funciones declaradas.

    has_sort : bool
        Indica si se detectó uso de sort() o sorted().

    has_binary_search : bool
        Indica si se detectó un patrón de búsqueda binaria.

    total_calls : int
        Cantidad total de llamadas a funciones.

    has_divide_by_2 : bool
        Indica si existe división entera por dos.

    has_hash_access : bool
        Indica acceso mediante índices o estructuras hash.
    """

    def __init__(self):
        """
        Inicializa todas las métricas utilizadas durante el recorrido
        del árbol sintáctico.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        self.for_loops = 0
        self.while_loops = 0
        self.max_depth = 0
        self._depth = 0
        self.recursive_calls = 0
        self.function_names: set[str] = set()
        self.has_sort = False
        self.has_binary_search = False
        self.total_calls = 0
        self.has_divide_by_2 = False
        self.has_hash_access = False

        # Profundidades de los bucles detectados
        self._loop_depths: list[int] = []

    def visit_FunctionDef(self, node):
        """
        Registra funciones declaradas dentro del código analizado.

        Parameters
        ----------
        node : ast.FunctionDef
            Nodo correspondiente a una definición de función.
        """

        self.function_names.add(node.name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        """
        Registra funciones asíncronas declaradas dentro del código.

        Parameters
        ----------
        node : ast.AsyncFunctionDef
            Nodo correspondiente a una función asíncrona.
        """

        self.function_names.add(node.name)
        self.generic_visit(node)

    def _enter_loop(self, node):
        """
        Gestiona la profundidad de anidamiento de bucles.

        Parameters
        ----------
        node : ast.AST
            Nodo correspondiente al bucle visitado.
        """

        self._depth += 1
        self._loop_depths.append(self._depth)

        if self._depth > self.max_depth:
            self.max_depth = self._depth

        self.generic_visit(node)
        self._depth -= 1

    def visit_For(self, node):
        """
        Detecta y contabiliza estructuras iterativas for.

        Parameters
        ----------
        node : ast.For
            Nodo correspondiente al bucle for.
        """

        self.for_loops += 1
        self._enter_loop(node)

    def visit_While(self, node):
        """
        Detecta y contabiliza estructuras iterativas while.

        Parameters
        ----------
        node : ast.While
            Nodo correspondiente al bucle while.
        """

        self.while_loops += 1
        self._check_binary_search(node)
        self._enter_loop(node)

    def _check_binary_search(self, node):
        """
        Detecta heurísticamente patrones asociados a búsqueda binaria.

        Parameters
        ----------
        node : ast.While
            Nodo correspondiente al bucle analizado.
        """

        src = ast.unparse(node)

        keywords = (
            "mid",
            "lo",
            "hi",
            "left",
            "right",
            "low",
            "high"
        )

        if sum(k in src for k in keywords) >= 3 and "//" in src:
            self.has_binary_search = True

    def visit_Call(self, node):
        """
        Detecta llamadas a funciones y operaciones de ordenamiento.

        Parameters
        ----------
        node : ast.Call
            Nodo correspondiente a una llamada de función.
        """

        self.total_calls += 1

        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ("sort", "sorted"):
                self.has_sort = True

        if isinstance(node.func, ast.Name):
            if node.func.id == "sorted":
                self.has_sort = True

        self.generic_visit(node)

    def visit_BinOp(self, node):
        """
        Detecta operaciones binarias relevantes para el análisis.

        Actualmente identifica divisiones enteras entre dos,
        patrón asociado frecuentemente a algoritmos O(log n).

        Parameters
        ----------
        node : ast.BinOp
            Nodo correspondiente a una operación binaria.
        """

        if isinstance(node.op, ast.FloorDiv):
            if isinstance(node.right, ast.Constant):
                if node.right.value == 2:
                    self.has_divide_by_2 = True

        self.generic_visit(node)

    def visit_Subscript(self, node):
        """
        Detecta accesos indexados sobre estructuras de datos.

        Parameters
        ----------
        node : ast.Subscript
            Nodo correspondiente a acceso indexado.
        """

        self.has_hash_access = True
        self.generic_visit(node)

    def detect_recursion(self, tree):
        """
        Detecta llamadas recursivas dentro de funciones declaradas.

        Parameters
        ----------
        tree : ast.Module
            Árbol sintáctico completo.

        Time Complexity
        ---------------
        O(n)
        """

        for node in ast.walk(tree):

            if not isinstance(
                node,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef
                )
            ):
                continue

            fn_name = node.name

            count = sum(
                1
                for child in ast.walk(node)
                if (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Name)
                    and child.func.id == fn_name
                )
            )

            self.recursive_calls = max(
                self.recursive_calls,
                count
            )

    def sequential_loops(self):
        """
        Calcula la cantidad de bucles secuenciales.

        Returns
        -------
        int
            Número de bucles detectados en profundidad 1.
        """

        return sum(
            1
            for d in self._loop_depths
            if d == 1
        )


def extract_features(code: str) -> np.ndarray:
    """
    Convierte un algoritmo Python en un vector de características
    normalizado para ser utilizado por la red neuronal.

    Parameters
    ----------
    code : str
        Código Python a analizar.

    Returns
    -------
    numpy.ndarray
        Vector de 12 características normalizado en [0,1].

    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    try:
        tree = ast.parse(code)

    except SyntaxError:
        return np.zeros(FEATURE_SIZE)

    extractor = FeatureExtractor()

    extractor.visit(tree)
    extractor.detect_recursion(tree)

    num_lines = sum(
        1
        for line in code.splitlines()
        if line.strip()
        and not line.strip().startswith("#")
    )

    raw = np.array([
        extractor.for_loops,
        extractor.while_loops,
        extractor.max_depth,
        float(extractor.recursive_calls > 0),
        extractor.recursive_calls,
        float(extractor.has_sort),
        float(extractor.has_binary_search),
        extractor.total_calls,
        num_lines,
        float(extractor.has_divide_by_2),
        extractor.sequential_loops(),
        float(extractor.has_hash_access),
    ], dtype=float)

    max_vals = np.array([
        10,
        10,
        5,
        1,
        5,
        1,
        1,
        20,
        50,
        1,
        10,
        1,
    ], dtype=float)

    normalized = np.clip(
        raw / max_vals,
        0.0,
        1.0
    )

    return normalized


if __name__ == "__main__":

    test_code = '''
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j]
                )

    return arr
'''

    features = extract_features(test_code)

    names = [
        "for_loops",
        "while_loops",
        "max_depth",
        "has_recursion",
        "recursive_calls",
        "has_sort",
        "has_binary_search",
        "total_calls",
        "num_lines",
        "has_divide_by_2",
        "sequential_loops",
        "has_hash_access"
    ]

    print("Feature vector (bubble_sort):")

    for name, value in zip(names, features):
        print(
            f"  {name:25s} = {value:.3f}"
        )