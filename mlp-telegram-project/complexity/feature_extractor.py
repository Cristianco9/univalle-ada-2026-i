"""
Convierte un snippet de código Python en un vector de features numéricas
que el MLP puede procesar para clasificar su complejidad algorítmica.

Features extraídas (vector de 16 dimensiones):
  0  → num_for_loops          : cantidad total de bucles for
  1  → num_while_loops        : cantidad total de bucles while
  2  → max_nesting_depth      : profundidad máxima de anidamiento
  3  → has_recursion          : 1 si la función se llama a sí misma
  4  → num_recursive_calls    : cuántas veces se llama a sí misma
  5  → has_sort               : 1 si usa .sort() o sorted()
  6  → has_binary_search      : 1 si hay patrón while + mid
  7  → num_function_calls     : total de llamadas a funciones
  8  → num_lines              : líneas de código no vacías
  9  → has_divide_by_2        : 1 si hay división entera //2
  10 → sequential_loops       : bucles for/while NO anidados
  11 → has_hash_access        : 1 si hay acceso a dict/list por clave
  12 → nested_loop_depth_2    : 1 si hay exactamente 2 niveles anidados  ← NUEVO
  13 → has_sort_plus_loop     : 1 si hay sort() Y un bucle juntos        ← NUEVO
  14 → recursive_divide       : 1 si hay recursión + división por 2      ← NUEVO
  15 → loop_inside_sort_ctx   : bucles dentro de contexto de ordenamiento ← NUEVO

Cambios v2:
  - FEATURE_SIZE: 12 → 16
  - Feature 12: discrimina O(n²) con exactamente 2 bucles anidados
  - Feature 13: discrimina O(n log n) con sort + bucle secuencial
  - Feature 14: discrimina O(n log n) merge sort (recursión + //2)
  - Feature 15: detecta bucles dentro de funciones que también usan sort
"""

import ast
import numpy as np

FEATURE_SIZE = 16


class FeatureExtractor(ast.NodeVisitor):

    def __init__(self):
        self.for_loops       = 0
        self.while_loops     = 0
        self.max_depth       = 0
        self._depth          = 0
        self.recursive_calls = 0
        self.function_names: set[str] = set()
        self.has_sort            = False
        self.has_binary_search   = False
        self.total_calls         = 0
        self.has_divide_by_2     = False
        self.has_hash_access     = False
        self._loop_depths: list[int] = []

        # ── Nuevas features v2 ────────────────────────────────────────────
        # Profundidades exactas de anidamiento detectadas
        self._nesting_levels: list[int] = []
        # Si hay sort() en el mismo scope que un bucle
        self.has_sort_in_function = False
        self._current_fn_has_sort = False
        self._current_fn_has_loop = False

    def visit_FunctionDef(self, node):
        self.function_names.add(node.name)
        # Guardar contexto anterior
        prev_sort = self._current_fn_has_sort
        prev_loop = self._current_fn_has_loop
        self._current_fn_has_sort = False
        self._current_fn_has_loop = False
        self.generic_visit(node)
        # Si esta función tiene sort Y bucle → feature 13
        if self._current_fn_has_sort and self._current_fn_has_loop:
            self.has_sort_in_function = True
        # Restaurar contexto
        self._current_fn_has_sort = prev_sort
        self._current_fn_has_loop = prev_loop

    def visit_AsyncFunctionDef(self, node):
        self.function_names.add(node.name)
        self.generic_visit(node)

    def _enter_loop(self, node):
        self._depth += 1
        self._loop_depths.append(self._depth)
        self._nesting_levels.append(self._depth)
        self._current_fn_has_loop = True
        if self._depth > self.max_depth:
            self.max_depth = self._depth
        self.generic_visit(node)
        self._depth -= 1

    def visit_For(self, node):
        self.for_loops += 1
        self._enter_loop(node)

    def visit_While(self, node):
        self.while_loops += 1
        self._check_binary_search(node)
        self._enter_loop(node)

    def _check_binary_search(self, node):
        src = ast.unparse(node)
        keywords = ("mid", "lo", "hi", "left", "right", "low", "high")
        if sum(k in src for k in keywords) >= 3 and "//" in src:
            self.has_binary_search = True

    def visit_Call(self, node):
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

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.FloorDiv):
            if isinstance(node.right, ast.Constant) and node.right.value == 2:
                self.has_divide_by_2 = True
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.has_hash_access = True
        self.generic_visit(node)

    def detect_recursion(self, tree):
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
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
            self.recursive_calls = max(self.recursive_calls, count)

    def sequential_loops(self):
        return sum(1 for d in self._loop_depths if d == 1)

    # ── Nuevas features v2 ────────────────────────────────────────────────

    def nested_loop_depth_2(self):
        """
        1 si hay bucles anidados a exactamente 2 niveles de profundidad
        y NO hay bucles a 3+ niveles → discrimina O(n²) vs O(n³).
        """
        has_depth_2 = any(d == 2 for d in self._nesting_levels)
        has_depth_3 = any(d >= 3 for d in self._nesting_levels)
        return float(has_depth_2 and not has_depth_3)

    def has_sort_plus_loop(self):
        """
        1 si hay sort/sorted Y al menos un bucle secuencial (profundidad 1)
        en la misma función → patrón típico de O(n log n).
        """
        has_seq_loop = any(d == 1 for d in self._loop_depths)
        return float(self.has_sort and has_seq_loop)

    def recursive_divide(self):
        """
        1 si hay recursión Y división por 2 → patrón merge sort / O(n log n).
        """
        return float(self.recursive_calls >= 1 and self.has_divide_by_2)


def extract_features(code: str) -> np.ndarray:
    """
    Recibe código Python como string y retorna un vector numpy de
    FEATURE_SIZE=16 dimensiones normalizado en [0, 1].
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return np.zeros(FEATURE_SIZE)

    extractor = FeatureExtractor()
    extractor.visit(tree)
    extractor.detect_recursion(tree)

    num_lines = sum(
        1 for line in code.splitlines()
        if line.strip() and not line.strip().startswith("#")
    )

    raw = np.array([
        extractor.for_loops,                       # 0
        extractor.while_loops,                     # 1
        extractor.max_depth,                       # 2
        float(extractor.recursive_calls > 0),      # 3
        extractor.recursive_calls,                 # 4
        float(extractor.has_sort),                 # 5
        float(extractor.has_binary_search),        # 6
        extractor.total_calls,                     # 7
        num_lines,                                 # 8
        float(extractor.has_divide_by_2),          # 9
        extractor.sequential_loops(),              # 10
        float(extractor.has_hash_access),          # 11
        extractor.nested_loop_depth_2(),           # 12 ← NUEVO
        extractor.has_sort_plus_loop(),            # 13 ← NUEVO
        extractor.recursive_divide(),              # 14 ← NUEVO
        float(extractor.has_sort_in_function),     # 15 ← NUEVO
    ], dtype=float)

    max_vals = np.array([
        10,   # for_loops
        10,   # while_loops
        5,    # max_depth
        1,    # has_recursion
        5,    # num_recursive_calls
        1,    # has_sort
        1,    # has_binary_search
        20,   # total_calls
        50,   # num_lines
        1,    # has_divide_by_2
        10,   # sequential_loops
        1,    # has_hash_access
        1,    # nested_loop_depth_2   ← binaria
        1,    # has_sort_plus_loop    ← binaria
        1,    # recursive_divide      ← binaria
        1,    # has_sort_in_function  ← binaria
    ], dtype=float)

    return np.clip(raw / max_vals, 0.0, 1.0)


if __name__ == "__main__":
    tests = {
        "bubble_sort O(n²)": """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""",
        "merge_sort O(n log n)": """
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return left + right
""",
        "sorted() O(n log n)": """
def get_median(arr):
    s = sorted(arr)
    return s[len(arr) // 2]
""",
    }

    names = [
        "for_loops", "while_loops", "max_depth", "has_recursion",
        "recursive_calls", "has_sort", "has_binary_search",
        "total_calls", "num_lines", "has_divide_by_2",
        "sequential_loops", "has_hash_access",
        "nested_loop_depth_2", "has_sort_plus_loop",
        "recursive_divide", "has_sort_in_function",
    ]

    for label, code in tests.items():
        print(f"\n── {label} ──")
        f = extract_features(code)
        for name, val in zip(names, f):
            if val > 0:
                print(f"  {name:25s} = {val:.2f}")