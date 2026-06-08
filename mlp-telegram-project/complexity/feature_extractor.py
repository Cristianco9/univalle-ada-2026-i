"""
Módulo responsable de extraer características estructurales
(features) a partir de código fuente Python utilizando el
Árbol de Sintaxis Abstracta (AST).

Estas características son utilizadas como entrada para la
Red Neuronal Multicapa (MLP) encargada de clasificar la
complejidad algorítmica de un programa.

El extractor analiza patrones frecuentemente asociados
a distintas complejidades asintóticas, tales como:

- Bucles for
- Bucles while
- Anidamiento de ciclos
- Recursividad
- Ordenamientos
- Búsqueda binaria
- División por 2
- Accesos indexados
- Relación entre llamadas y tamaño del código

Las características extraídas son posteriormente
normalizadas al intervalo [0,1] para facilitar el
proceso de entrenamiento y predicción del modelo.

Features Generadas
------------------

1.  Cantidad de bucles for
2.  Cantidad de bucles while
3.  Profundidad máxima de anidamiento
4.  Presencia de recursividad
5.  Número de llamadas recursivas
6.  Uso de ordenamiento
7.  Patrón de búsqueda binaria
8.  Número total de llamadas
9.  Líneas efectivas de código
10. División por 2
11. Bucles secuenciales
12. Accesos indexados/hash
13. Doble anidamiento
14. Sort + Loop
15. Recursión + División
16. Sort dentro de función iterativa
17. Relación for/total loops
18. Triple anidamiento
19. Llamadas por línea
20. Dos llamadas recursivas

Autores:
    Cristian Cortes
    Katherine Arboleda

Proyecto:
    Clasificador Inteligente de Complejidad Algorítmica
    mediante Redes Neuronales Multicapa (MLP)
"""

# ============================================================================
# IMPORTACIONES
# ============================================================================

# Permite analizar código Python mediante AST.
import ast

# Biblioteca utilizada para construir el vector numérico final.
import numpy as np


# ============================================================================
# CONFIGURACIÓN GENERAL
# ============================================================================

# Número total de características producidas por el extractor.
FEATURE_SIZE = 20


# ============================================================================
# EXTRACTOR DE FEATURES
# ============================================================================

class FeatureExtractor(ast.NodeVisitor):
    """
    Recorre un Árbol de Sintaxis Abstracta (AST)
    y calcula métricas estructurales asociadas
    al comportamiento algorítmico del código.

    La clase extiende ast.NodeVisitor para visitar
    automáticamente los distintos nodos presentes
    en el árbol sintáctico.

    Attributes
    ----------
    for_loops : int
        Cantidad de bucles for detectados.

    while_loops : int
        Cantidad de bucles while detectados.

    max_depth : int
        Máxima profundidad de anidamiento observada.

    recursive_calls : int
        Cantidad de llamadas recursivas.

    has_sort : bool
        Indica si existe uso de sort() o sorted().

    has_binary_search : bool
        Indica si se detecta un patrón compatible
        con búsqueda binaria.

    total_calls : int
        Número total de llamadas a funciones.

    has_divide_by_2 : bool
        Detecta expresiones del tipo // 2.

    has_hash_access : bool
        Detecta accesos mediante índices o claves.
    """

    def __init__(self):
        """
        Inicializa todos los contadores y banderas
        utilizadas durante el recorrido del AST.
        """

        self.for_loops = 0
        self.while_loops = 0

        self.max_depth = 0
        self._depth = 0

        self.recursive_calls = 0

        self.function_names: set = set()

        self.has_sort = False
        self.has_binary_search = False

        self.total_calls = 0

        self.has_divide_by_2 = False
        self.has_hash_access = False

        self._loop_depths: list = []
        self._nesting_levels: list = []

        self._current_fn_has_sort = False
        self._current_fn_has_loop = False

        self.has_sort_in_function = False

        self._max_recursive_calls_in_one_fn = 0

    # =====================================================================
    # FUNCIONES
    # =====================================================================

    def visit_FunctionDef(self, node):
        """
        Procesa funciones tradicionales.

        Registra el nombre de la función y determina
        si dentro de ella coexisten operaciones de
        ordenamiento y ciclos iterativos.
        """

        self.function_names.add(node.name)

        prev_sort = self._current_fn_has_sort
        prev_loop = self._current_fn_has_loop

        self._current_fn_has_sort = False
        self._current_fn_has_loop = False

        self.generic_visit(node)

        if self._current_fn_has_sort and self._current_fn_has_loop:
            self.has_sort_in_function = True

        self._current_fn_has_sort = prev_sort
        self._current_fn_has_loop = prev_loop

    def visit_AsyncFunctionDef(self, node):
        """
        Procesa funciones asíncronas.
        """

        self.function_names.add(node.name)

        self.generic_visit(node)

    # =====================================================================
    # BUCLES
    # =====================================================================

    def _enter_loop(self, node):
        """
        Gestiona la entrada y salida de un bucle.

        Actualiza niveles de profundidad y registra
        información sobre anidamiento.
        """

        self._depth += 1

        self._loop_depths.append(self._depth)
        self._nesting_levels.append(self._depth)

        self._current_fn_has_loop = True

        if self._depth > self.max_depth:
            self.max_depth = self._depth

        self.generic_visit(node)

        self._depth -= 1

    def visit_For(self, node):
        """
        Detecta bucles for.
        """

        self.for_loops += 1

        self._enter_loop(node)

    def visit_While(self, node):
        """
        Detecta bucles while.

        Además verifica si corresponde
        a un patrón de búsqueda binaria.
        """

        self.while_loops += 1

        self._check_binary_search(node)

        self._enter_loop(node)

    # =====================================================================
    # BÚSQUEDA BINARIA
    # =====================================================================

    def _check_binary_search(self, node):
        """
        Detecta heurísticamente implementaciones
        de búsqueda binaria.

        Se buscan nombres típicos como:

        - low
        - high
        - left
        - right
        - mid

        junto con una división entera por dos.
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

    # =====================================================================
    # LLAMADAS A FUNCIONES
    # =====================================================================

    def visit_Call(self, node):
        """
        Cuenta llamadas a funciones y detecta
        operaciones de ordenamiento.
        """

        self.total_calls += 1

        if isinstance(node.func, ast.Attribute):

            if node.func.attr in ("sort", "sorted"):

                self.has_sort = True
                self._current_fn_has_sort = True

        if isinstance(node.func, ast.Name):

            if node.func.id == "sorted":

                self.has_sort = True
                self._current_fn_has_sort = True

        self.generic_visit(node)

    # =====================================================================
    # OPERACIONES ARITMÉTICAS
    # =====================================================================

    def visit_BinOp(self, node):
        """
        Detecta divisiones enteras por dos.

        Este patrón suele aparecer en algoritmos
        Divide y Vencerás y búsqueda binaria.
        """

        if isinstance(node.op, ast.FloorDiv):

            if (
                isinstance(node.right, ast.Constant)
                and node.right.value == 2
            ):
                self.has_divide_by_2 = True

        self.generic_visit(node)

    # =====================================================================
    # ACCESOS INDEXADOS
    # =====================================================================

    def visit_Subscript(self, node):
        """
        Detecta expresiones del tipo:

            arr[i]
            dict[key]

        utilizadas frecuentemente en estructuras
        indexadas o tablas hash.
        """

        self.has_hash_access = True

        self.generic_visit(node)

    # =====================================================================
    # RECURSIVIDAD
    # =====================================================================

    def detect_recursion(self, tree):
        """
        Analiza todas las funciones definidas
        y determina si realizan llamadas
        recursivas sobre sí mismas.
        """

        for node in ast.walk(tree):

            if not isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
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

            self._max_recursive_calls_in_one_fn = max(
                self._max_recursive_calls_in_one_fn,
                count
            )

    # =====================================================================
    # FEATURES DERIVADAS
    # =====================================================================

    def sequential_loops(self):
        """
        Cuenta ciclos presentes al primer nivel.

        Indicador útil para diferenciar
        ciclos secuenciales de anidados.
        """

        return sum(
            1
            for d in self._loop_depths
            if d == 1
        )

    def nested_loop_depth_2(self):
        """
        Detecta específicamente doble anidamiento.

        Retorna:
            1.0 -> existe profundidad 2
            0.0 -> caso contrario
        """

        has_2 = any(
            d == 2
            for d in self._nesting_levels
        )

        has_3 = any(
            d >= 3
            for d in self._nesting_levels
        )

        return float(has_2 and not has_3)

    def has_triple_nest(self):
        """
        Detecta anidamientos de profundidad
        tres o superior.
        """

        return float(
            any(d >= 3 for d in self._nesting_levels)
        )

    def has_sort_plus_loop(self):
        """
        Detecta coexistencia de ordenamiento
        y bucles iterativos.
        """

        has_seq = any(
            d == 1
            for d in self._loop_depths
        )

        return float(
            self.has_sort and has_seq
        )

    def recursive_divide(self):
        """
        Detecta patrones Divide y Vencerás.

        Requiere:
        - Recursividad
        - División por 2
        """

        return float(
            self.recursive_calls >= 1
            and self.has_divide_by_2
        )

    def loop_count_ratio(self):
        """
        Calcula la proporción:

            for / (for + while)

        Valor útil para caracterizar
        el estilo iterativo del algoritmo.
        """

        total = self.for_loops + self.while_loops

        if total == 0:
            return 0.5

        return self.for_loops / total

    def calls_per_line(self, num_lines):
        """
        Calcula densidad de llamadas
        por línea efectiva de código.
        """

        if num_lines == 0:
            return 0.0

        return min(
            self.total_calls / num_lines,
            2.0
        ) / 2.0

    def has_two_recursive_calls(self):
        """
        Detecta funciones con exactamente
        dos llamadas recursivas.

        Patrón típico de algoritmos como:

        - Fibonacci
        - Merge Sort
        - Árboles binarios
        """

        return float(
            self._max_recursive_calls_in_one_fn == 2
        )


# ============================================================================
# EXTRACCIÓN DE FEATURES
# ============================================================================

def extract_features(code: str) -> np.ndarray:
    """
    Extrae y normaliza las características
    estructurales de un fragmento de código Python.

    Parameters
    ----------
    code : str
        Código fuente a analizar.

    Returns
    -------
    numpy.ndarray

        Vector de 20 características
        normalizadas en el rango [0,1].

    Notes
    -----
    Si el código contiene errores sintácticos,
    se retorna un vector de ceros.
    """

    try:

        tree = ast.parse(code)

    except SyntaxError:

        return np.zeros(FEATURE_SIZE)

    ext = FeatureExtractor()

    ext.visit(tree)

    ext.detect_recursion(tree)

    # ------------------------------------------------------------------
    # Conteo de líneas efectivas
    # ------------------------------------------------------------------

    num_lines = sum(
        1
        for line in code.splitlines()
        if line.strip()
        and not line.strip().startswith("#")
    )

    # ------------------------------------------------------------------
    # Vector de características sin normalizar
    # ------------------------------------------------------------------

    raw = np.array([

        ext.for_loops,
        ext.while_loops,
        ext.max_depth,

        float(ext.recursive_calls > 0),
        ext.recursive_calls,

        float(ext.has_sort),
        float(ext.has_binary_search),

        ext.total_calls,

        num_lines,

        float(ext.has_divide_by_2),

        ext.sequential_loops(),

        float(ext.has_hash_access),

        ext.nested_loop_depth_2(),

        ext.has_sort_plus_loop(),

        ext.recursive_divide(),

        float(ext.has_sort_in_function),

        ext.loop_count_ratio(),

        ext.has_triple_nest(),

        ext.calls_per_line(num_lines),

        ext.has_two_recursive_calls(),

    ], dtype=float)

    # ------------------------------------------------------------------
    # Factores máximos para normalización
    # ------------------------------------------------------------------

    max_vals = np.array([

        10, 10, 5,
        1, 5,
        1, 1,
        20,
        50,
        1,
        10,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1

    ], dtype=float)

    # ------------------------------------------------------------------
    # Normalización y recorte
    # ------------------------------------------------------------------

    return np.clip(
        raw / max_vals,
        0.0,
        1.0
    )